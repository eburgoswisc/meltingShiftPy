#!/usr/bin/env python3

from setuptools import *

def main():
    
    setup(name='meltingShiftPy',
          version='0.1',
          description='Python software to process melting shift data',
          url='https://github.com/eburgoswisc/meltingShiftPy',
          author='Emanuel Burgos',
          author_email='eburgos@wisc.edu',
          license='None',
          packages= find_packages(),
          scripts=["bin/meltingShiftPy"],
          install_requires = [
              "pandas",
              "matplotlib"
          ],
          zip_safe=False)
    
if __name__ == "__main__":
    main()