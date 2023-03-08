""" Setup
"""
from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

exec(open("pypi_package_test_leondgarse/version.py").read())
setup(
    name="pypi_package_test_2",
    version=__version__,
    description="pypi_package_test_leondgarse",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/leondgarse/pypi_package_test_leondgarse",
    author="Leondgarse",
    author_email="leondgarse@google.com",
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development",
    ],
    # Note that this is a string of words separated by whitespace, not a list.
    keywords="pypi_package_test_leondgarse",
    packages=find_packages(exclude=[]),
    include_package_data=True,
    install_requires=[],
    python_requires=">=3.6",
    license="Apache 2.0",
)
