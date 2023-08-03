# Targets and their commands

# Run database migrations
mig:
	@echo "Running database migrations..."
	@python manage.py makemigrations
	@python manage.py migrate

# Create superuser for the admin panel
admin:
	@echo "Creating superuser for the admin panel..."
	@./manage.py createsuperuser
	@echo "Superuser created."

# Delete database migrations except __init__.py
unmig:
	@echo "Deleting database migrations except __init__.py..."
	@find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
	@echo "Database migrations deleted."

# Run tests
test:
	@echo "Running tests..."
	@python manage.py test

# Run code linting checks using autopep8
lint:
	@echo "Running code linting checks..."
	@autopep8 . --recursive --in-place --pep8-passes 2000 --exclude venv

# Format code using autopep8 and collect static files
format:
	@echo "Formatting code using autopep8..."
	@autopep8 . --recursive --in-place --pep8-passes 2000 --exclude=venv
	@echo "Checking for static files..."
	@if exist empower/root/static (echo "Static files found. Running collectstatic..." & python manage.py collectstatic --noinput) else (echo "No static files found.")

# Phony targets (do not create files with these names)
.PHONY: mig admin unmig test lint format
