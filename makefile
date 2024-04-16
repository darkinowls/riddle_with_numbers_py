ai:
	alembic init -t async migrations

ar:
	alembic revision --autogenerate -m "migration"

au:
	alembic upgrade head

ad:
	alembic downgrade -1

# for alembic
##############

tests:
	pytest --cov .

server:
	uvicorn app.main:app --reload --host 0.0.0.0 --port 8001

lint:
	cd .. && pylint riddle_with_numbers_py

.PHONY: tests lint server ar ai au ad


