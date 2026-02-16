# 🧪 Testing Guide - Quality Toolkit

## Overview

Complete test suite to validate all quality-toolkit features.

## 📋 Prerequisites

```bash
# Install dependencies
pip install -r requirements.txt
```

## 🚀 Running Tests

### Method 1: Complete Test Script (Recommended)

```bash
python run_tests.py
```

This script runs all tests and displays a detailed report with:
- ✅ Number of successful tests
- ❌ Number of failures
- 💥 Number of errors
- 📊 Success rate
- 🔍 Problem details

### Method 2: Via Makefile

```bash
# All tests
make test

# Quick tests (imports only)
make test-quick

# Specific tests
make test-imports    # Test module imports
make test-sftp       # Test SFTP service
make test-api        # Test API functions
make test-compat     # Test Python compatibility
```

### Method 3: Individual tests with unittest

```bash
# All tests
python -m unittest discover tests -v

# A specific test file
python -m unittest tests.test_imports -v
python -m unittest tests.test_sftp -v
python -m unittest tests.test_api_functions -v
python -m unittest tests.test_python_compat -v

# A specific test class
python -m unittest tests.test_sftp.TestSftpService -v

# A specific test
python -m unittest tests.test_sftp.TestSftpService.test_sftp_init -v
```

## 📁 Test Structure

```
tests/
├── __init__.py                  # Test package initialization
├── test_imports.py              # Module import tests (7 tests)
├── test_sftp.py                 # SFTP service tests with Paramiko (4 tests)
├── test_api_functions.py        # API functions tests (4 tests)
└── test_python_compat.py        # Python compatibility tests (3 tests)
```

**Total: 22 tests**

## 🧪 Test Types

### 1. Import Tests (`test_imports.py`)
Verifies that all modules can be imported:
- ✅ SFTP Service
- ✅ PostgreSQL Service
- ✅ MSSQL Service
- ✅ SSO Service
- ✅ API Functions
- ✅ Local Functions
- ✅ UI Functions

### 2. SFTP Tests (`test_sftp.py`)
Unit tests with mocks for SFTP service:
- ✅ Connection initialization
- ✅ File upload
- ✅ File listing
- ✅ Connection closure

### 3. API Tests (`test_api_functions.py`)
HTTP request function tests:
- ✅ Successful request
- ✅ Request with parameters
- ✅ Retry mechanism
- ✅ Custom status codes

### 4. Compatibility Tests (`test_python_compat.py`)
Verifies Python compatibility:
- ✅ Minimum version (Python >= 3.10)
- ✅ Maximum version (Python <= 3.13)
- ✅ Required modules availability

## 📊 Test Report

Example output:

```
================================================================================
          🧪 QUALITY-TOOLKIT - COMPLETE TEST SUITE
================================================================================

➤ 📊 System Information
--------------------------------------------------------------------------------
Python version: 3.10.16
Number of tests found: 22

➤ 🚀 Running Tests
--------------------------------------------------------------------------------
✅ test_import_services_sftp ... ok
✅ test_sftp_init ... ok
✅ test_send_api_request_success ... ok
...

➤ 📈 Results Summary
--------------------------------------------------------------------------------
Tests run: 22
✅ Passed: 22
✅ Failures: 0
✅ Errors: 0

Success rate: 100.0%

                 🎉 ALL TESTS PASSED! 🎉
```

## ⚙️ Configuration

Tests use:
- **unittest**: Standard Python testing framework
- **unittest.mock**: Mocking to isolate tests
- No external test dependencies required

## 🔍 Debugging

For more verbosity:

```bash
# Verbose mode
python -m unittest discover tests -v

# Very verbose mode with script
python run_tests.py  # Already configured in verbose mode
```

## 📝 Adding New Tests

1. Create a new `test_*.py` file in the `tests/` folder
2. Import `unittest`
3. Create a class inheriting from `unittest.TestCase`
4. Add methods starting with `test_`

Example:

```python
import unittest

class TestMyModule(unittest.TestCase):
    def test_my_function(self):
        """Test my function"""
        result = my_function()
        self.assertEqual(result, expected_value)
```

## ✅ Pre-Commit Checklist

```bash
# 1. Run all tests
python run_tests.py

# 2. Verify no errors
# Success rate must be 100%

# 3. Commit if everything is green ✅
```

## 🐛 Troubleshooting

### Module import error
```bash
# Verify dependencies are installed
pip install -r requirements.txt
```

### Failing tests
```bash
# Check Python version
python --version  # Must be >= 3.10

# Re-run a specific test in verbose mode
python -m unittest tests.test_sftp.TestSftpService.test_sftp_init -v
```

## 📚 Resources

- unittest documentation: https://docs.python.org/3/library/unittest.html
- unittest.mock documentation: https://docs.python.org/3/library/unittest.mock.html
- Testing best practices: https://docs.python-guide.org/writing/tests/

## 🎯 Goals

- ✅ **Complete coverage**: All main modules are tested
- ✅ **Fast tests**: Execution in < 1 second
- ✅ **Isolated tests**: Use of mocks to avoid external dependencies
- ✅ **CI/CD ready**: Compatible with continuous integration pipelines

---

**Note**: These are unit tests that don't require real connections (database, SFTP, API). They use mocks to simulate behaviors.

