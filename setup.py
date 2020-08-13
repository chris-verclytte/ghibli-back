"""Setup script for ghibli."""

from setuptools import find_packages, setup

import ghibli

setup(
    name=ghibli.__name__,
    version=ghibli.__version__,
    url="https://github.com/chris-verclytte/ghibli-back",
    python_requires=">=3.8",
    author_email="1611574+chris-verclytte@users.noreply.github.com",
    description="API to display Ghibli films",
    packages=find_packages(),
    install_requires=[],
)
