import pathlib

from setuptools import setup, find_packages

from jhu_handshake_data_tools import __version__, __author__, __email__

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="jhu_handshake_data_tools",
    version=__version__,
    description="A library for cleaning and working with majors from JHU's Handshake environment",
    long_description=README,
    url="https://github.com/cedwards036/JHUHandshakeDataTools",
    author=__author__,
    author_email=__email__,
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(),
    include_package_data=True
)
