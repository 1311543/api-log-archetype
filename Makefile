help:
	@echo "clean - remove all build, test, coverage and Python artifacts"
	@echo "clean-pyc - remove Python file artifacts"
	@echo "clean-build - remove wrapped file"
	@echo "clean-test - remove test and coverage artifacts"
	@echo "push - clear and push s3 bucket"
	@echo "test - run tests quickly with the default Python"
	@echo "build - package"

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
	aws s3 cp index.html s3://repository-python-archetype/
	aws s3 cp dist s3://repository-python-archetype/ --recursive
	make refresh

refresh:
	pip uninstall belcorp --yes
	python -m pip install belcorp --extra-index-url https://repository-python-archetype.s3.us-east-2.amazonaws.com/index.html

build: clean
	zip -r aws_services.zip *
	mkdir ./wrapper
	cp aws_services.zip ./wrapper
	rm -f aws_services.zip
	aws s3 cp wrapper s3://belc-bigdata-functional-dlk-qas/analitico/py/dlk_arquetipos_core/ --recursive
	rm -R wrapper

