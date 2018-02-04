default: package
package:
	python setup.py sdist
	python setup.py bdist_wheel
test-upload:
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*
test-install:
	pip install --index-url https://test.pypi.org/simple/ unicorn-hat-sim
upload:
	twine upload dist/*