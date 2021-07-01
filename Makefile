PYTHON=python

.PHONY:
	clean
	test-report
	install
	run
	test

.DEFAULT_GOAL: test


install:
	$(PYTHON) -m pip install -r requirements.txt

test:
	coverage run -m unittest
	@test-report

run:
	$(PYTHON) -m src

clean:
	fdfind -I cache . -x rm -rf

test-report:
	coverage report

test-html-report:
	coverage html
	xdg-open /home/snsm/documents/code/automation/packages/task_manager/htmlcov/index.html
