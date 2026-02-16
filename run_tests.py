#!/usr/bin/env python3
"""
Complete test script for quality-toolkit
Runs all tests and generates a detailed report
"""
import sys
import unittest
import os

# Colors for terminal
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'
BOLD = '\033[1m'


def print_header(text):
    """Display a styled header"""
    print(f"\n{BLUE}{BOLD}{'=' * 80}{RESET}")
    print(f"{BLUE}{BOLD}{text.center(80)}{RESET}")
    print(f"{BLUE}{BOLD}{'=' * 80}{RESET}\n")


def print_section(text):
    """Display a section"""
    print(f"\n{YELLOW}{BOLD}➤ {text}{RESET}")
    print(f"{YELLOW}{'-' * 80}{RESET}")


def run_tests():
    """Run all tests"""
    print_header("🧪 QUALITY-TOOLKIT - COMPLETE TEST SUITE")

    # System information
    print_section("📊 System Information")
    print(f"Python version: {sys.version}")
    print(f"Python path: {sys.executable}")
    print(f"Working directory: {os.getcwd()}")

    # Test discovery and execution
    print_section("🔍 Test Discovery")

    # Find all tests
    loader = unittest.TestLoader()
    start_dir = 'tests'

    if not os.path.exists(start_dir):
        print(f"{RED}❌ 'tests' directory not found{RESET}")
        return False

    suite = loader.discover(start_dir, pattern='test*.py')

    # Count tests
    test_count = suite.countTestCases()
    print(f"Number of tests found: {test_count}")

    # Run tests
    print_section("🚀 Running Tests")
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    # Results summary
    print_section("📈 Results Summary")

    total = result.testsRun
    failures = len(result.failures)
    errors = len(result.errors)
    skipped = len(result.skipped)
    success = total - failures - errors - skipped

    print(f"\n{BOLD}Tests run:{RESET} {total}")
    print(f"{GREEN}{BOLD}✅ Passed:{RESET} {success}")

    if failures > 0:
        print(f"{RED}{BOLD}❌ Failures:{RESET} {failures}")
    else:
        print(f"{GREEN}✅ Failures: 0{RESET}")

    if errors > 0:
        print(f"{RED}{BOLD}💥 Errors:{RESET} {errors}")
    else:
        print(f"{GREEN}✅ Errors: 0{RESET}")

    if skipped > 0:
        print(f"{YELLOW}⏭️  Skipped:{RESET} {skipped}")

    # Success rate
    if total > 0:
        success_rate = (success / total) * 100
        print(f"\n{BOLD}Success rate:{RESET} {success_rate:.1f}%")

        if success_rate == 100:
            print(f"\n{GREEN}{BOLD}{'🎉 ALL TESTS PASSED! 🎉'.center(80)}{RESET}")
        elif success_rate >= 80:
            print(f"\n{YELLOW}{BOLD}{'⚠️  Most tests passed'.center(80)}{RESET}")
        else:
            print(f"\n{RED}{BOLD}{'❌ Many tests failed'.center(80)}{RESET}")

    # Failure details
    if failures > 0 or errors > 0:
        print_section("🔴 Problem Details")

        if failures:
            print(f"\n{RED}{BOLD}Failures:{RESET}")
            for test, traceback in result.failures:
                print(f"\n{RED}Test: {test}{RESET}")
                print(traceback)

        if errors:
            print(f"\n{RED}{BOLD}Errors:{RESET}")
            for test, traceback in result.errors:
                print(f"\n{RED}Test: {test}{RESET}")
                print(traceback)

    print_header("END OF TESTS")

    return result.wasSuccessful()


if __name__ == '__main__':
    success = run_tests()
    sys.exit(0 if success else 1)


