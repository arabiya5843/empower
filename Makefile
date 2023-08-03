mig:
	@echo "Running database migrations..."
	@python manage.py makemigrations
	@python manage.py migrate

admin:
	@echo "Creating superuser for the admin panel..."
	@./manage.py createsuperuser
	@echo "Superuser created."

unmig:
	@echo "Deleting database migrations except __init__.py..."
	find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
	@echo "Database migrations deleted."

test:
	@echo "Running tests..."
	@python manage.py test

lint:
	@echo "Running code linting checks..."
	@autopep8 . --recursive --in-place --pep8-passes 2000 --exclude venv

format:
	@echo "Formatting code using autopep8..."
	@pylint . --ignore=venv --exclude migrations --disable=W0613,W0511
