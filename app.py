from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os
from chatbot import HealthChatbot
from prescription_reader import PrescriptionReader
from utils import allowed_file, create_upload_folder

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'pdf'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

create_upload_folder(UPLOAD_FOLDER)

chatbot = HealthChatbot()
prescription_reader = PrescriptionReader()

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy', 'message': 'AI Health Assistant is running'}), 200

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_message = data.get('message', '')

        if not user_message:
            return jsonify({'error': 'Message is required'}), 400

        response = chatbot.get_response(user_message)

        return jsonify({
            'response': response,
            'timestamp': chatbot.get_timestamp()
        }), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/upload-prescription', methods=['POST'])
def upload_prescription():
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400

        file = request.files['file']

        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400

        if file and allowed_file(file.filename, ALLOWED_EXTENSIONS):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            extracted_text = prescription_reader.read_prescription(filepath)

            return jsonify({
                'success': True,
                'filename': filename,
                'extracted_text': extracted_text,
                'message': 'Prescription processed successfully'
            }), 200

        return jsonify({'error': 'Invalid file type'}), 400

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/analyze-prescription', methods=['POST'])
def analyze_prescription():
    try:
        data = request.get_json()
        prescription_text = data.get('text', '')

        if not prescription_text:
            return jsonify({'error': 'Prescription text is required'}), 400

        analysis = prescription_reader.analyze_prescription(prescription_text)

        return jsonify({
            'analysis': analysis,
            'timestamp': chatbot.get_timestamp()
        }), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
