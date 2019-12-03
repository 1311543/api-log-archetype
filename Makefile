help:
	@echo "clean - remove all build, test, coverage and Python artifacts"
	@echo "clean-pyc - remove Python file artifacts"
	@echo "clean-build - remove wrapped file"
	@echo "clean-test - remove test and coverage artifacts"
	@echo "install - clear and push s3 bucket"
	@echo "refresh - remove previos python library and install the newest"
	@echo "wheel - package proyect"

clean: clean-build clean-pyc

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr belcorp.egg-info/

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +
install:
	pip install --upgrade -r requirements.txt

wheel: clean
	python setup.py sdist bdist_wheel
	aws s3 cp belc_log.html s3://repository-python-archetype/
	aws s3 cp dist s3://repository-python-archetype/ --recursive
	make refresh

refresh:
	pip uninstall belc_log --yes
	python -m pip install belc_log --extra-index-url https://repository-python-archetype.s3.us-east-2.amazonaws.com/belc_log.html
