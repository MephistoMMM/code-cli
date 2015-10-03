#!/usr/bin/env python3

from setuptools import setup, find_packages

with open('./codevs/requirements.md') as f:
    reqs = f.read().splitlines()

setup(name='codevs',
    version='0.5',
      description='CodeVs Tool Set',
      keywords=[],
      author='codevs',
      author_email='mephistommm@gmail.com',
      url='',

      package_data={
      },
      packages=find_packages(exclude=['*.test.*']),
      include_package_data=True, # can leave this?

      zip_safe=False,
      install_requires=reqs,

      entry_points={
            'console_scripts': [
                'codevs = codevs.cli.main:main'
            ]
      },
      classifiers=(
            'Programming Language :: Python',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.4',
      ), 
      data_files = [
      ],
)
