#!/bin/sh

echo "👋 Hi, $(whoami)!"
echo "We're glad you're interested in Pytecimalthon."

echo "\n🔍 Checking if Python 3 is installed..."
if command -v python3 >/dev/null 2>&1; then
    python3 --version
else
    echo "❌ Python 3 is not installed. Please install it before proceeding."
    exit 1
fi

echo "✅ Python 3 is available!"

# Clone and install Py3Sh if not already present
if [ ! -d "py3sh" ]; then
    echo "\n📦 Cloning Py3Sh..."
    git clone https://github.com/zimoshi/py3sh || exit 1
    cd py3sh || exit 1
    echo "⚙️ Running Py3Sh installer..."
    python3 py3sh-gem.py || exit 1
    cd ..
else
    echo "✅ Py3Sh already exists."
fi

echo "🔗 Registering 'pyd3' CLI tool via Py3Sh..."
py3sh runner.py pyd3 \$1 \$2 \$3

echo "\n🚀 Setup complete! Try running:"
echo "   pyd3 test.pyd"