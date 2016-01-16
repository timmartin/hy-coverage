"""
This launcher script is needed because 'coverage run' won't
directly execute Hy scripts. This is only used for testing.
"""

import sys
import hy
import importlib

importlib.import_module(sys.argv[1])
