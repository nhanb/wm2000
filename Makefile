watch-ui:
	find ./src/wm2000/gui/ -name '*.ui' | entr -rc ./scripts/compile-ui-files.py

format:
	ruff check --fix
	ruff format
