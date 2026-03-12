@echo off
echo Starting AI Health Assistant Backend...
echo =======================================

where python >nul 2>nul
if %errorlevel% neq 0 (
    echo Error: Python is not installed or not in PATH
    pause
    exit /b 1
)

where tesseract >nul 2>nul
if %errorlevel% neq 0 (
    echo Warning: Tesseract OCR is not installed
    echo Please install Tesseract to use prescription reading features
    echo.
)

cd backend

if not exist "uploads" (
    echo Creating uploads directory...
    mkdir uploads
)

if not exist "data" (
    echo Creating data directory...
    mkdir data
)

if not exist "venv\" (
    echo Creating virtual environment...
    python -m venv venv
)

echo Activating virtual environment...
call venv\Scripts\activate.bat

echo Installing dependencies...
pip install -r requirements.txt

echo.
echo Starting Flask server...
echo Backend will be available at: http://localhost:5000
echo =======================================
python app.py

pause
