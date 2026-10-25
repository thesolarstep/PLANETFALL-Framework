#!/usr/bin/env python3
"""
OPERATION PLANETFALL: Primary Scientific Discovery and Validation CLI Entry Point.
"""

import sys
import os

_src_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "src"))
_pkg_dir = os.path.join(_src_dir, "planetfall")
__path__ = [_pkg_dir]
__package__ = "planetfall"

if _src_dir not in sys.path:
    sys.path.insert(0, _src_dir)

_init_py = os.path.join(_pkg_dir, "__init__.py")
if os.path.exists(_init_py):
    with open(_init_py, "r") as _f:
        _code = _f.read()
    exec(compile(_code, _init_py, "exec"), globals())

from planetfall.cli import main

if __name__ == "__main__":
    main()
