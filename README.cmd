# AI Health Assistant

A complete AI-powered health assistant application that combines health chat and prescription reading capabilities. Built with React frontend and Flask backend.

## Features

- **Interactive Health Chat**: AI chatbot that answers health-related questions
- **Prescription OCR Reader**: Upload and extract text from prescription images
- **Medical Term Simplification**: Converts medical jargon into plain language
- **Medication Database**: Information about common medications
- **Symptom Guidance**: General advice for common symptoms
- **Beautiful UI**: Modern, responsive interface with Tailwind CSS

## Project Structure

```
AI_Health_Assistant/
├── backend/
│   ├── app.py                    # Flask server with API endpoints
│   ├── chatbot.py                # Health chatbot logic
│   ├── prescription_reader.py    # OCR and prescription analysis
│   ├── utils.py                  # Helper functions
│   ├── data/
│   │   └── health_data.csv      # Health knowledge database
│   ├── uploads/                  # Uploaded prescription images
│   ├── requirements.txt          # Python dependencies
│   └── README.md                # Backend documentation
├── src/
│   ├── components/
│   │   ├── ChatInterface.tsx    # Chat UI component
│   │   └── PrescriptionReader.tsx # Prescription upload UI
│   ├── App.tsx                  # Main React app
│   └── ...
└── README.md                     # This file
```

## Prerequisites

- Node.js (v16 or higher)
- Python 3.8 or higher
- Tesseract OCR

### Installing Tesseract OCR

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

## Quick Start

### 1. Install Frontend Dependencies

```bash
npm install
```

### 2. Install Backend Dependencies

```bash
cd backend
pip install -r requirements.txt
cd ..
```

### 3. Start the Backend Server

Open a terminal and run:

```bash
cd backend
python app.py
```

The backend will start on `http://localhost:5000`

### 4. Start the Frontend Development Server

Open another terminal and run:

```bash
npm run dev
```

The frontend will start on `http://localhost:5173`

### 5. Open Your Browser

Navigate to `http://localhost:5173` to use the application.

## Usage Guide

### Health Chat
1. Click on the "Health Chat" tab
2. Type your health-related question
3. Press Enter or click Send
4. Get AI-powered responses with general health information

**Example Questions:**
- "What should I do for a headache?"
- "How much water should I drink daily?"
- "Tell me about ibuprofen"
- "What are symptoms of diabetes?"

### Prescription Reader
1. Click on the "Prescription Reader" tab
2. Click to upload a prescription image (PNG, JPG, JPEG, or PDF)
3. Click "Read Prescription" to extract text
4. View extracted text and analysis including:
   - Detected medications
   - Dosage instructions
   - Important warnings
   - Simplified medical terms

## API Endpoints

The backend provides these REST API endpoints:

- `GET /api/health` - Health check
- `POST /api/chat` - Send chat messages
- `POST /api/upload-prescription` - Upload prescription image
- `POST /api/analyze-prescription` - Analyze prescription text

See `backend/README.md` for detailed API documentation.

## Customization

### Adding Health Knowledge

Edit `backend/data/health_data.csv` to add custom health information:

```csv
category,keyword,response
symptoms,migraine,Migraines are severe headaches...
medications,aspirin,Aspirin is a pain reliever...
```

### Adding Medications

Edit the `medication_database` in `backend/prescription_reader.py`.

## Technology Stack

**Frontend:**
- React 18
- TypeScript
- Tailwind CSS
- Vite
- Lucide React (icons)

**Backend:**
- Flask (web framework)
- Tesseract OCR (text extraction)
- Pillow (image processing)
- Flask-CORS (cross-origin requests)

## Important Notes

- This application provides general health information only
- Always consult healthcare professionals for medical advice
- OCR accuracy depends on image quality
- Maximum upload file size: 16MB
- Supported formats: PNG, JPG, JPEG, PDF

## Troubleshooting

### Backend won't start
- Ensure Python 3.8+ is installed
- Install dependencies: `pip install -r backend/requirements.txt`
- Check if port 5000 is available

### Tesseract not found
- Install Tesseract OCR for your operating system
- Ensure it's added to your system PATH
- Restart terminal after installation

### Frontend can't connect to backend
- Ensure backend is running on port 5000
- Check browser console for CORS errors
- Verify both servers are running

### Upload fails
- Ensure `backend/uploads/` directory exists
- Check file size (max 16MB)
- Verify file format (PNG, JPG, JPEG, PDF)

## Build for Production

### Frontend

```bash
npm run build
```

Built files will be in the `dist/` directory.

### Backend

For production deployment, use a WSGI server like Gunicorn:

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## License

This project is for educational purposes.

## Disclaimer

This application is designed for informational and educational purposes only. It is not a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of your physician or other qualified health provider with any questions you may have regarding a medical condition. Never disregard professional medical advice or delay in seeking it because of something you have read in this application.
