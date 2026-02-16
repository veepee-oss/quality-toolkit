# 🎯 Quick Testing Guide - Quality Toolkit

## 🚀 How to test quickly

### Option 1: Complete test (Recommended)
```bash
python run_tests.py
```
✅ Displays a colored and detailed report
✅ 22 tests executed in < 1 second
✅ Success rate displayed

### Option 2: Via Makefile
```bash
make test              # All tests
make test-quick        # Quick tests (imports)
make test-sftp         # SFTP tests only
```

### Option 3: Standard unittest
```bash
python -m unittest discover tests -v
```

## 📊 Expected Result

```
🎉 ALL TESTS PASSED! 🎉

Tests run: 22
✅ Passed: 22
✅ Failures: 0
✅ Errors: 0
Success rate: 100.0%
```

## ✅ What is tested

| Module | Tests | Description |
|--------|-------|-------------|
| **Imports** | 7 | All modules import correctly |
| **SFTP** | 4 | SFTP service with Paramiko works |
| **API** | 4 | HTTP functions with retry work |
| **Python** | 3 | Python 3.10-3.13 compatibility |
| **Integration** | 4 | Complete workflows work |

## 🔧 In case of problems

```bash
# 1. Check Python
python --version  # Must display >= 3.10

# 2. Reinstall dependencies
pip install -r requirements.txt

# 3. Re-run tests
python run_tests.py
```

## 📖 Complete documentation

See `tests/README.md` for more details.

---

**Last update**: 2026-02-16
**Version**: 2.5.6
**Status**: ✅ All tests pass (100%)

