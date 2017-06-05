#!/usr/bin/env python

from distutils.core import setup

with open('requirements.txt') as fp:
    requirements = fp.read().splitlines()

setup(name='deep-belief-network',
      version='1.0.0',
      description='Python implementation of Deep Belief Networks',
      packages=['dbn', 'dbn.tensroflow'],
      install_requires=requirements,
      )
