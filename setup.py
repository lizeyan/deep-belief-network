#!/usr/bin/env python

from setuptools import setup

with open('requirements.txt') as fp:
    requirements = fp.read().splitlines()

setup(name='deep-belief-network',
      version='1.0.1',
      description='Python implementation of Deep Belief Networks',
      packages=['dbn', 'dbn.tensorflow'],
      install_requires=requirements,
      )
