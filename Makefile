include ./Makefile-git.mk
include ./Makefile-aws.mk
include ./Makefile-clean.mk
include ./env.sh

.DEFAULT_GOAL := help

help:
	@echo "push - clean wheel refresh git_wheel"
	@echo "clean - remove all build, test, coverage and Python artifacts"
	@echo "develop - clean wheel refresh"
	@echo "wheel - Execute Generate .wheel binary python application"
	@echo "refresh - remove last version installed and install the newest"
	@echo "clean-build - remove wrapped file"
	@echo "clean-pyc - remove not important generated python files"
	@echo "git - commit and push passing commit message""
	@echo "git-push - commit and push passing commit message and default commit message""
	@echo "test - run unit tests"
	@echo "install - Install Python requirements to install for the first time in any enviroment"
	@echo "aws - Configure Access-key and Secret Key"

push: pep8 clean wheel refresh git-push
	@echo "${HEADER}"
	@echo "Finished Process for project ${PROJECT_NAME}"

develop: clean wheel refresh
	@echo "${HEADER}"
	@echo "Finished Process for project ${PROJECT_NAME}"

wheel:
	@echo "${HEADER}"
	@echo "* Wrapping Binary .wheel for project ${PROJECT_NAME}"
	python3 setup.py sdist bdist_wheel
	aws s3 cp ${PROJECT_NAME}.html s3://${BUCKET_NAME}/
	aws s3 cp dist s3://${BUCKET_NAME}/ --recursive

refresh:
	@echo "${HEADER}"
	@echo "Uninstalling ${PROJECT_NAME} in pip dependencies"
	pip3 uninstall ${PROJECT_NAME} --yes --no-cache-dir
	python3.5 -m pip uninstall ${PROJECT_NAME} --yes --no-cache-dir
	@echo "Installing ${PROJECT_NAME} in pip dependencies"
	#pip3 install ${PROJECT_NAME} --extra-index-url https://repository-python-archetype.s3.us-east-2.amazonaws.com/${PROJECT_NAME}.html
	python3.5 -m pip install ${PROJECT_NAME} --find-link=https://${BUCKET_NAME}.s3.us-east-2.amazonaws.com/${PROJECT_NAME}.html --no-cache-dir

install:
	pip3 install --upgrade -r requirements.txt
	python3 -m pip install --user --upgrade setuptools wheel

test:

pep8:
	pycodestyle ${PROJECT_NAME}
	#pycodestyle ${PROJECT_NAME} --exclude aws/s3.py
