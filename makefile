test:
	pytest --cov .

server:
	uvicorn main:app --reload --host 0.0.0.0 --port 8001

lint:
	cd .. && pylint riddle_with_numbers_py

.PHONY: test lint
