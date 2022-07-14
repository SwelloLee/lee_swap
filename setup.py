# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in lee_swap/__init__.py
from lee_swap import __version__ as version

setup(
	name="lee_swap",
	version=version,
	description="Instance Swapper",
	author="Swello Lee",
	author_email="swellolee@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
