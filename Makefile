sync:
	uv sync

run:
	rm *.db
	uv run python main.py
