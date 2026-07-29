.PHONY: validate build test check stats

validate:
	python3 scripts/superlib.py validate

build:
	python3 scripts/superlib.py build

test:
	python3 -m unittest discover -s tests -v

check: validate test build
	git diff --exit-code -- dist skills/super-library/references/compact.md

stats:
	python3 scripts/superlib.py stats
