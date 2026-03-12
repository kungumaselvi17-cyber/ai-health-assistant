#!/bin/bash

echo "Starting AI Health Assistant Backend..."
echo "======================================="

if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed"
    exit 1
fi

if ! command -v tesseract &> /dev/null; then
    echo "Warning: Tesseract OCR is not installed"
    echo "Please install Tesseract to use prescription reading features"
    echo ""
fi

cd backend

if [ ! -d "uploads" ]; then
    echo "Creating uploads directory..."
    mkdir uploads
fi

if [ ! -d "data" ]; then
    echo "Creating data directory..."
    mkdir data
fi

if [ ! -f "venv/bin/activate" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

echo "Activating virtual environment..."
source venv/bin/activate

echo "Installing dependencies..."
pip install -r requirements.txt

echo ""
echo "Starting Flask server..."
echo "Backend will be available at: http://localhost:5000"
echo "======================================="
python app.py
