# AI Health Assistant

A simple and easy-to-use AI health chatbot that can read prescriptions and convert medical terminology into plain language.

## Features

- **Health Chat**: Interactive AI chatbot that answers health-related questions
- **Prescription Reader**: Upload prescription images and extract text using OCR
- **Medical Term Simplification**: Converts medical abbreviations and terms into simple language
- **Medication Information**: Get information about common medications
- **Symptom Guidance**: General information about common symptoms

## Project Structure

```
AI_Health_Assistant/
├── app.py                    # Main Flask application
├── chatbot.py                # Health chatbot logic
├── prescription_reader.py    # OCR and prescription analysis
├── utils.py                  # Helper functions
├── data/
│   └── health_data.csv      # Health knowledge database
├── uploads/                  # Uploaded prescription images
├── requirements.txt          # Python dependencies
└── README.md                # This file
```

## Installation

### Prerequisites

- Python 3.8 or higher
- Tesseract OCR installed on your system

#### Install Tesseract OCR

**Windows:**
1. Download from: https://github.com/UB-Mannheim/tesseract/wiki
2. Install and add to PATH

**macOS:**
```bash
brew install tesseract
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get update
sudo apt-get install tesseract-ocr
```

### Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Create necessary directories:
```bash
mkdir -p data uploads
```

## Running the Application

### Start the Backend Server

```bash
python app.py
```

The server will start on `http://localhost:5000`

### Start the Frontend (React)

In a new terminal, from the project root:

```bash
npm install
npm run dev
```

The frontend will start on `http://localhost:5173`

## API Endpoints

### Health Check
- **GET** `/api/health`
- Returns server status

### Chat
- **POST** `/api/chat`
- Body: `{ "message": "your question" }`
- Returns AI health assistant response

### Upload Prescription
- **POST** `/api/upload-prescription`
- Form data with file upload
- Returns extracted text from prescription

### Analyze Prescription
- **POST** `/api/analyze-prescription`
- Body: `{ "text": "prescription text" }`
- Returns detailed analysis with simplified terms

## Usage Examples

### Chat with the Health Assistant

```javascript
fetch('http://localhost:5000/api/chat', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ message: 'What should I do for a headache?' })
})
```

### Upload a Prescription

```javascript
const formData = new FormData();
formData.append('file', prescriptionImage);

fetch('http://localhost:5000/api/upload-prescription', {
  method: 'POST',
  body: formData
})
```

## Important Notes

- This is an educational tool for general health information
- Always consult healthcare professionals for medical advice
- The OCR accuracy depends on image quality
- Supported file formats: PNG, JPG, JPEG, PDF
- Maximum file size: 16MB

## Customization

### Adding Health Knowledge

Edit `data/health_data.csv` to add custom health information:

```csv
category,keyword,response
symptoms,migraine,Migraines are severe headaches...
medications,aspirin,Aspirin is a pain reliever...
```

### Adding Medications

Edit the `medication_database` in `prescription_reader.py` to add more medications.

## Troubleshooting

### Tesseract Not Found
If you get a tesseract error, ensure it's installed and in your PATH.

### CORS Errors
The backend uses Flask-CORS to allow frontend requests. If you change ports, update CORS settings in `app.py`.

### Upload Errors
Ensure the `uploads/` directory exists and has write permissions.

## License

This project is for educational purposes.

## Disclaimer

This application provides general health information only and is not a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of your physician or other qualified health provider with any questions you may have regarding a medical condition.
