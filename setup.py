# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
#from pip.req import parse_requirements
import re, ast

# get version from version variable in phtax/init.py
_version_re = re.compile(r'version\s+=\s+(.*)')

with open('requirements.txt') as f:
    install_requires = f.read().strip().split('\n')

with open('phtax/init.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

#requirements = parse_requirements("requirements.txt", session="")

setup(
	name='phtax',
	version=version,
	description='Philippine Tax Reports',
	author='Opensource Solutions Philippines',
	author_email='info@ossph.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires,
	#dependency_links=[str(ir._link) for ir in requirements if ir._link]
)
