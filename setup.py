from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

classifiers = """\
Environment :: Console
Intended Audience :: Developers
License :: OSI Approved :: MIT License
Programming Language :: Python :: 3.4
Topic :: Software Development :: Testing
Development Status :: 3 - Alpha
"""

setup(name="hy_coverage_plugin",
      version="0.0.4",
      description="coverage.py plugin for the Hy language",
      long_description=readme(),
      url="https://github.com/timmartin/hy-coverage",
      author="Tim Martin",
      author_email="tim@asymptotic.co.uk",
      license="mit",
      packages=["hy_coverage_plugin"],
      install_requires=[
          "coverage >= 4.0",
          "Hy >= 0.11.0",
      ],
      classifiers=classifiers.splitlines()
  )
      
