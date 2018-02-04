# Packaging

## Pre-requisites

1. [Pandoc](https://pandoc.org/) - To convert Markdown to Restructured Text (PyPI does not support Markdown for package descriptions)
1. [pypandoc](https://pypi.python.org/pypi/pypandoc/) - Python wrapper for Pandoc
1. [twine](https://pypi.python.org/pypi/twine) - For interacting with PyPI

```sh
pip install pypandoc
pip install twine
```

## Building

Commands are run using [Make](https://www.gnu.org/software/make/).  
_Note: Be sure to update the version number in the `setup.py` file._

Tag the commit for the release. This will cause Github to generate a tarball of the code. Substitue the current version for `1.0.01 below.

```sh
git tag 1.0.0 -m "Initial release for PyPI"
git tags
git push --tags origin master
```

Build the package and upload it to the test version of PyPI

```sh
make package
make test-upload
```

If everything looks OK, upload to the production PyPI feed

```sh
make upload
```
