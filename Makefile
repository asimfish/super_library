.PHONY: validate build eval eval-writing test check stats

validate:
	python3 scripts/superlib.py validate

build:
	python3 scripts/superlib.py build

test:
	python3 -m unittest discover -s tests -v

eval:
	python3 scripts/superlib.py eval-retrieval

eval-writing:
	python3 scripts/superlib.py eval-writing --list --format json >/dev/null

check: validate eval eval-writing test build
	git diff --exit-code -- dist \
		skills/super-library/references/agent-index.md \
		skills/super-library/references/core.md \
		skills/super-library/references/index.json \
		skills/super-library/references/router.json \
		skills/super-library/references/guides \
		skills/super-library/references/routes \
		skills/super-library/assets/tables

stats:
	python3 scripts/superlib.py stats
