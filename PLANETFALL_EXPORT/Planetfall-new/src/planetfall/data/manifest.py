import os
import json
import hashlib
from datetime import datetime

class DatasetManifest:
    """Tracks and registers dataset provenance, checksums, and licensing."""
    
    def __init__(self, manifest_file="data/dataset_manifest.json"):
        self.manifest_file = manifest_file
        self.records = {}
        self.load()

    def load(self):
        if os.path.exists(self.manifest_file):
            try:
                with open(self.manifest_file, "r") as f:
                    self.records = json.load(f)
            except Exception:
                self.records = {}
        else:
            self.records = {}

    def save(self):
        os.makedirs(os.path.dirname(os.path.abspath(self.manifest_file)), exist_ok=True)
        with open(self.manifest_file, "w") as f:
            json.dump(self.records, f, indent=2)

    @staticmethod
    def calculate_sha256(filepath):
        h = hashlib.sha256()
        with open(filepath, "rb") as f:
            while chunk := f.read(65536):
                h.update(chunk)
        return h.hexdigest()

    def register(self, identifier, filepath, source, sector=None, cadence=None, license_str="NASA Open Data / Public Domain", notes=""):
        sha256 = self.calculate_sha256(filepath)
        size = os.path.getsize(filepath)
        record = {
            "identifier": identifier,
            "filepath": filepath,
            "source": source,
            "sector": sector,
            "cadence": cadence,
            "size_bytes": size,
            "sha256": sha256,
            "license": license_str,
            "retrieval_timestamp": datetime.utcnow().isoformat() + "Z",
            "notes": notes
        }
        self.records[identifier] = record
        self.save()
        return record

    def get(self, identifier):
        return self.records.get(identifier)

    def verify(self, identifier):
        rec = self.get(identifier)
        if not rec or not os.path.exists(rec["filepath"]):
            return False, "File missing"
        curr_hash = self.calculate_sha256(rec["filepath"])
        if curr_hash == rec["sha256"]:
            return True, "Checksum matches"
        return False, f"Checksum mismatch: expected {rec['sha256']}, got {curr_hash}"
