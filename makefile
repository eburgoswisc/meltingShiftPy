## Makefile to intall `meltingShiftPy` in the path

install:
	python setup.py install

reset:
	pip uninstall -y meltingShiftPy
	pip install -e .