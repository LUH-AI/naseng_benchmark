#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='naseng_benchmark',
      version='0.1',
      packages=find_packages(include=['naseng_benchmark']),
      install_requires=[
            'botorch',
            'gpytorch'
      ]
)