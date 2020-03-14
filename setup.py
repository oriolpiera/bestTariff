#! /usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(name='besttariff',
    version='0.1',
    description='Best electrical tariff based on your hourly consumption',
    author='Oriol Piera',
    author_email='oriol.piera@somenergia.coop',
    url='https://github.com/oriolpiera/bestTariff',
    license='GPLv3',
    packages=find_packages(exclude=('tests', 'docs')),
    test_suite='tests',
)
