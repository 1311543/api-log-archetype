.PHONY:
clean: clean-build clean-pyc

clean-build:
	@echo "${HEADER}"
	@echo "Cleanning workspace for ${PROJECT_NAME}"
	rm -fr build/
	rm -fr dist/
	rm -fr ${PROJECT_NAME}.egg-info/

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +
	find . -name '*.pytest_cache' -exec rm -fr {} +
	find . -name 'logfile' -exec rm -fr {} +