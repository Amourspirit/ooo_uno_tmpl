#!/usr/bin/env python
import pathlib
from setuptools import setup, find_packages
from src.parser import __version__
PKG_NAME = 'oootmpl'
VERSION = __version__
PKG_MAIN = 'oot'

# The directory containing this file
HERE = pathlib.Path(__file__).parent
# The text of the README file
with open(HERE / "src" / "README.rst") as fh:
    README = fh.read()

PACKAGES = find_packages('src', exclude=[
    '*.tests',
    '*.tests.*'])
# PACKAGES = list(os.walk(str(HERE / 'src')))


# This call to setup() does all the work
setup(
    name=PKG_NAME,
    version=VERSION,
    python_requires='>=3.10.0',
    description="OOO_UNO_TMPL main module",
    long_description_content_type="text/x-rst",
    long_description=README,
    url="https://github.com/Amourspirit/ooo_uno_tmpl",
    author=":Barry-Thomas-Paul: Moss",
    author_email='bigbytetech@gmail.com',
    license="Apache",
    package_dir={'': 'src'},
    packages=PACKAGES,
    keywords=['ooouno', 'uno', 'libreoffice', 'openoffice', 'pyuno'],
    classifiers=[
        "License :: OSI Approved :: Apache License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
    ],
    include_package_data=True,
)
