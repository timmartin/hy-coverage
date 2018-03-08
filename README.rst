.. image:: https://travis-ci.org/timmartin/hy-coverage.svg?branch=master
    :target: https://travis-ci.org/timmartin/hy-coverage

hy_coverage_plugin
==================

A plugin to support the Hy language in coverage.py

Installation
------------

First install the package::

    pip install hy-coverage-plugin

Then add the following to your `.coveragerc`::

    [run]
    plugins = hy_coverage_plugin
