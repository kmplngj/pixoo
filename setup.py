#!/usr/bin/python
"""
    Setup.py file for pixoo package
"""
from setuptools import setup


setup(
    name="pixoo",
    version="0.6.0",
    author="Ron Talman",
    description=(
        "A library to easily communicate with the Divoom Pixoo 64",
        "(and hopefully soon more screens that support Wi-Fi)",
    ),
    license="BSD",
    keywords="pixoo",
    url="https://github.com/SomethingWithComputers/pixoo#readme",
    packages=['pixoo'],
    install_requires=[
        'requests~=2.28.1',
        'Pillow~=9.2.0',
    ],
)
