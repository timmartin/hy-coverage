default: all

all: basic_test hy_test

.PHONY: basic_test hy_test

# A very crude test, we just check that coverage can be run without
# throwing an error. If this fails, it probably indicates an
# environment problem rather than a problem with the code.
basic_test:
	rm -rf htmlcov
	coverage run basic_test.py
	coverage html
	test -f htmlcov/basic_test_py.html


