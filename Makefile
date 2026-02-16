install:
	@python3 -m build
	@pip3 install -e .

test:
	@echo "🧪 Running all tests..."
	@python run_tests.py

test-imports:
	@echo "🧪 Testing imports..."
	@python -m pytest tests/test_imports.py -v

test-sftp:
	@echo "🧪 Testing SFTP service..."
	@python -m pytest tests/test_sftp.py -v

test-api:
	@echo "🧪 Testing API functions..."
	@python -m pytest tests/test_api_functions.py -v

test-compat:
	@echo "🧪 Testing Python compatibility..."
	@python -m pytest tests/test_python_compat.py -v

test-quick:
	@echo "🧪 Quick test (imports only)..."
	@python -m unittest tests.test_imports -v

coverage:
	@echo "📊 Generating coverage report..."
	@python -m pytest tests/ --cov=quality_toolkit --cov-report=html --cov-report=term

.PHONY: install test test-imports test-sftp test-api test-compat test-quick coverage

