PYTHON=python

.PHONY:
	install
	test
	clean

# run
# clean
# setup
.DEFAULT_GOAL: test


install:
	$(PYTHON) -m pip install -r requirements.txt

test:
	$(PYTHON) -m tests -v

run:
	$(PYTHON) -m src

clean:
	fdfind -I cache . -x rm -rf
