import json
import re
from datetime import datetime
import csv
import os

class HealthChatbot:
    def __init__(self):
        self.health_knowledge = self.load_health_data()
        self.conversation_history = []

    def load_health_data(self):
        knowledge_base = {
            'symptoms': {
                'fever': 'Fever is often a sign of infection. Rest, stay hydrated, and monitor your temperature. Seek medical attention if fever exceeds 103°F (39.4°C) or persists for more than 3 days.',
                'headache': 'Headaches can be caused by stress, dehydration, or lack of sleep. Try resting in a quiet, dark room and staying hydrated. If severe or persistent, consult a doctor.',
                'cough': 'A cough can be due to cold, flu, or allergies. Stay hydrated, use a humidifier, and avoid irritants. If it persists for more than 2 weeks or is accompanied by blood, see a doctor.',
                'cold': 'Common cold symptoms include runny nose, sore throat, and congestion. Rest, drink plenty of fluids, and use over-the-counter medications as needed. Symptoms typically resolve in 7-10 days.',
                'stomach': 'Stomach issues can include pain, nausea, or digestive problems. Eat bland foods, stay hydrated, and avoid trigger foods. Persistent or severe pain requires medical attention.',
                'pain': 'Pain can have many causes. For minor pain, rest and over-the-counter pain relievers may help. For severe, persistent, or unexplained pain, please consult a healthcare provider.',
            },
            'general_health': {
                'exercise': 'Regular exercise is important for overall health. Aim for at least 150 minutes of moderate aerobic activity or 75 minutes of vigorous activity per week.',
                'diet': 'A balanced diet includes fruits, vegetables, whole grains, lean proteins, and healthy fats. Stay hydrated by drinking 8 glasses of water daily.',
                'sleep': 'Adults need 7-9 hours of quality sleep per night. Maintain a consistent sleep schedule and create a relaxing bedtime routine.',
                'stress': 'Manage stress through exercise, meditation, deep breathing, or talking to someone. Chronic stress can impact physical health.',
                'hydration': 'Drink at least 8 glasses (64 ounces) of water daily. Increase intake during exercise or hot weather.',
            },
            'medications': {
                'paracetamol': 'Paracetamol (acetaminophen) is used for pain relief and fever reduction. Adult dose: 500-1000mg every 4-6 hours, maximum 4000mg per day.',
                'ibuprofen': 'Ibuprofen is an anti-inflammatory pain reliever. Adult dose: 200-400mg every 4-6 hours, maximum 1200mg per day without doctor supervision.',
                'antibiotic': 'Antibiotics fight bacterial infections. Always complete the full course as prescribed, even if you feel better. Never share antibiotics or use old prescriptions.',
            }
        }

        data_file = 'data/health_data.csv'
        if os.path.exists(data_file):
            try:
                with open(data_file, 'r', encoding='utf-8') as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        category = row.get('category', '').lower()
                        keyword = row.get('keyword', '').lower()
                        response = row.get('response', '')
                        if category and keyword and response:
                            if category not in knowledge_base:
                                knowledge_base[category] = {}
                            knowledge_base[category][keyword] = response
            except Exception as e:
                print(f"Error loading health data: {e}")

        return knowledge_base

    def get_response(self, user_message):
        user_message_lower = user_message.lower()

        greetings = ['hello', 'hi', 'hey', 'greetings']
        if any(greeting in user_message_lower for greeting in greetings):
            return "Hello! I'm your AI Health Assistant. I can help you with general health information, symptom guidance, and prescription reading. How can I assist you today?"

        if 'thank' in user_message_lower:
            return "You're welcome! Remember, I provide general information only. Always consult healthcare professionals for medical advice. Is there anything else I can help you with?"

        if any(word in user_message_lower for word in ['prescription', 'medicine', 'medication', 'drug']):
            return "I can help you understand your prescription. You can upload an image of your prescription, and I'll extract and explain the information in simple terms. Would you like to upload a prescription now?"

        for category, keywords_dict in self.health_knowledge.items():
            for keyword, response in keywords_dict.items():
                if keyword in user_message_lower:
                    disclaimer = "\n\nNote: This is general information only. For personalized medical advice, please consult a healthcare professional."
                    return response + disclaimer

        if '?' in user_message:
            return "I can provide general health information about symptoms, medications, diet, exercise, and wellness. Could you please be more specific about what health topic you'd like to know about?"

        return "I'm here to help with health-related questions. You can ask me about symptoms, general health advice, medications, or upload a prescription for me to read. What would you like to know?"

    def get_timestamp(self):
        return datetime.now().isoformat()

    def save_conversation(self, user_message, bot_response):
        self.conversation_history.append({
            'timestamp': self.get_timestamp(),
            'user': user_message,
            'bot': bot_response
        })
