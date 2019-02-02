build:
	python setup.py sdist bdist_wheel

upload-pypi:
	python -m twine upload dist/*

upload-test:
	python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*

clean:
	rm -rf dist/*
	rm -rf build/*

test:
	python -m pytest
