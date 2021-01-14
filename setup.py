# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in nasser_app/__init__.py
from nasser_app import __version__ as version

setup(
	name='nasser_app',
	version=version,
	description='Nasser App',
	author='Nasser',
	author_email='info@kcsc.moy',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
