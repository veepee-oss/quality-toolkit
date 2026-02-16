#!/bin/bash
# Quick environment and tests verification script

echo "======================================================================"
echo "       🔍 QUALITY-TOOLKIT VERIFICATION"
echo "======================================================================"
echo ""

# Check Python
echo "➤ Python version:"
python --version
echo ""

# Check main dependencies
echo "➤ Installed dependencies:"
pip list | grep -E "(paramiko|psycopg2|requests|selenium|playwright|pytds)" || echo "⚠️  Some dependencies are missing"
echo ""

# Check that the module can be imported
echo "➤ Module import test:"
python -c "import quality_toolkit; print('✅ quality_toolkit imported successfully')" || echo "❌ Import error"
echo ""

# Run tests
echo "======================================================================"
echo "       🧪 RUNNING TESTS"
echo "======================================================================"
echo ""
python run_tests.py

# Display final result
exit_code=$?
echo ""
if [ $exit_code -eq 0 ]; then
    echo "======================================================================"
    echo "       ✅ VERIFICATION COMPLETED SUCCESSFULLY"
    echo "======================================================================"
else
    echo "======================================================================"
    echo "       ❌ PROBLEMS WERE DETECTED"
    echo "======================================================================"
fi

exit $exit_code

