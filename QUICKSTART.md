# Quick Start Guide

Follow these simple steps to get your AI Health Assistant running:

## Step 1: Install Tesseract OCR

Choose your operating system:

**Windows:**
- Download installer from: https://github.com/UB-Mannheim/tesseract/wiki
- Run the installer
- Add to PATH when prompted

**macOS:**
```bash
brew install tesseract
```

**Linux:**
```bash
sudo apt-get update
sudo apt-get install tesseract-ocr
```

## Step 2: Install Dependencies

**Frontend:**
```bash
npm install
```

**Backend:**
```bash
cd backend
pip install -r requirements.txt
cd ..
```

## Step 3: Create Required Directories

```bash
cd backend
mkdir -p uploads
cd ..
```

## Step 4: Start the Application

**Terminal 1 - Start Backend:**
```bash
cd backend
python app.py
```

Wait until you see: `Running on http://0.0.0.0:5000`

**Terminal 2 - Start Frontend:**
```bash
npm run dev
```

## Step 5: Open in Browser

Navigate to: http://localhost:5173

## You're Ready!

Now you can:
- Chat with the AI health assistant
- Upload prescriptions to read and analyze
- Get health information and advice

## Need Help?

- Check README.md for detailed documentation
- See backend/README.md for API details
- Ensure both servers are running before using the app
