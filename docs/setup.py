'''
Created on 1 Mar 2017

@author: connorross
'''
from setuptools import setup

setup(name="ledtester",
      version="0.1",
      description="LED Testing for Assignment3 in COMP30670 2017",
      url="",
      author="Connor Ross",
      author_email="connor.ross@ucdconnect.ie",
      licence="GPL3",
      packages=['docs'],
      entry_points={
        'console_scripts':['led_tester=docs.main:main']
        },
      install_requires=[
          'numpy',
      ],
      )
