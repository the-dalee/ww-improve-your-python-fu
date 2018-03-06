# File ./setup.py

from setuptools import setup

setup(name='mynicetools',
      # Put here all requirements of your scripts
      # Pip will install them automatically
      install_requires=['click'],
      version='1.0',
      packages=['greeter'],
      entry_points={
          'console_scripts': [
              'sayhello = greeter.cli:greet',
          ]
      }
    )
