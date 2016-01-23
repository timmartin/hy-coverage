.. image:: https://travis-ci.org/timmartin/hy-coverage.svg?branch=master
    :target: https://travis-ci.org/timmartin/hy-coverage

hy_coverage_plugin
==================

A plugin to support the Hy language in coverage.py

Installation
------------

Add the directory containing the plugin code to your `$PYTHONPATH`, then add the following to your `.coveragerc`:

    [run]
    plugins = hy_coverage_plugin
