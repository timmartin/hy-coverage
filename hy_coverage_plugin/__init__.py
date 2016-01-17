"""
coverage.py plugin for Hy.
"""

from .hy_coverage import HyCoveragePlugin

def coverage_init(reg, options):
    """An init callback that is called on initialisation to register the
    classes provided by this plugin.
    """
    reg.add_file_tracer(HyCoveragePlugin())

