import pathlib

from autohandshake import __version__
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.rst").read_text()

setup(
    name="handshakemajors",
    version=__version__,
    description="A library for cleaning and working with majors from JHU's Handshake environment",
    long_description=README,
    url="https://github.com/cedwards036/HandshakeMajors",
    author="Christopher Edwards",
    author_email="cedwards036@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(),
    include_package_data=True
)
