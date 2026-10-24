build:
	rm -rf dist build *.egg-info
	uv run python -m build
	uv run twine check dist/*
post:
	uv run twine upload dist/*