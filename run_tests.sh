#!/bin/bash
set -e
echo "🚀 Setting up testing environment..."

if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
else
    echo "✅ Virtual environment already exists"
fi

# activate virtual environment
echo "🔌 Activating virtual environment..."
source venv/bin/activate

# install dependencies
echo "📥 Installing dependencies..."
pip install pytest

# run tests
echo "🧪 Testing..."
pytest -v

# Deactivate virtual environment
deactivate

echo "✨ Done!"