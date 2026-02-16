# 📁 Test Structure - Design Decisions

## Directory Structure

```
quality-toolkit/
├── run_tests.py              # Main test runner script (root level)
├── verify.sh                 # Complete verification script (root level)
├── Makefile                  # Build commands with test targets
├── tests/                    # Test directory
│   ├── __init__.py          # Test package marker
│   ├── test_imports.py      # Import tests (7 tests)
│   ├── test_sftp.py         # SFTP service tests (4 tests)
│   ├── test_api_functions.py# API functions tests (4 tests)
│   ├── test_python_compat.py# Python compatibility tests (3 tests)
│   ├── test_integration.py  # Integration tests (4 tests)
│   └── README.md            # Complete test documentation
└── docs/
    ├── TESTING.md           # Quick testing guide
    └── TESTS-QUICK-START.md # Quick start guide
```

## Why Scripts Are At Root Level

### ✅ Advantages of Root-Level Scripts

1. **Simpler Execution**
   ```bash
   python run_tests.py        # Simple and intuitive
   ./verify.sh                # Easy to remember
   ```

2. **No Python Path Issues**
   - Scripts run from root have direct access to `quality_toolkit` module
   - No need to modify `sys.path` or `PYTHONPATH`
   - Works consistently across all environments

3. **Standard Practice**
   - Most Python projects keep test runners at root level
   - Examples: pytest, tox, setup.py test
   - Users expect to find them there

4. **CI/CD Friendly**
   ```yaml
   # .gitlab-ci.yml or .github/workflows/test.yml
   script:
     - python run_tests.py  # Clear and simple
   ```

5. **Make Integration**
   ```makefile
   test:
       python run_tests.py  # Simple path reference
   ```

### ❌ Issues With tests/ Location

1. **Import Problems**
   - Python can't find `quality_toolkit` module when running from `tests/`
   - Requires complex `sys.path` manipulation
   - Different behavior when run from different directories

2. **User Confusion**
   ```bash
   # Doesn't work intuitively:
   cd tests
   python run_tests.py  # ❌ Module not found errors
   
   # Would need to do:
   cd ..
   python tests/run_tests.py  # ✅ Works but less intuitive
   ```

3. **Inconsistent Documentation**
   - Need to explain the correct way to run tests
   - More prone to user errors
   - Harder to troubleshoot

## Test Files Organization

### Test Files (In tests/ Directory) ✅

```
tests/
├── test_*.py    # All test modules belong here
└── README.md    # Test documentation
```

**Why**: Test files need to be discoverable by unittest/pytest and should be isolated from production code.

### Runner Scripts (At Root Level) ✅

```
.
├── run_tests.py    # Test runner script
└── verify.sh       # Verification script
```

**Why**: Runner scripts are tools for users/CI, not tests themselves. They orchestrate test execution.

## Recommended Usage

### For Developers
```bash
# Quick test
python run_tests.py

# Complete verification
./verify.sh

# Via make
make test
```

### For CI/CD
```yaml
test:
  script:
    - pip install -r requirements.txt
    - python run_tests.py
```

### For Contributors
```bash
# Before committing
make test

# Specific test
python -m unittest tests.test_sftp -v
```

## Alternative Approaches (Not Used)

### 1. pytest + setup.py
- Would require additional dependencies
- More complex setup
- Overkill for this project size

### 2. tox
- Good for multi-version testing
- Too heavy for single toolkit
- Not needed for this use case

### 3. Scripts in bin/
- Adds another directory
- Not a standard Python practice
- Would still have path issues

## Conclusion

**Current structure is optimal because:**
- ✅ Simple and intuitive
- ✅ No path complications
- ✅ Standard Python practice
- ✅ CI/CD friendly
- ✅ Easy to document and explain

---

**Last updated**: 2026-02-16  
**Version**: 2.5.6

