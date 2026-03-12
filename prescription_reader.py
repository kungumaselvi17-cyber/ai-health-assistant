import re
from PIL import Image
import pytesseract
import os

class PrescriptionReader:
    def __init__(self):
        self.medication_database = {
            'paracetamol': 'Pain reliever and fever reducer (Acetaminophen)',
            'ibuprofen': 'Anti-inflammatory pain reliever',
            'amoxicillin': 'Antibiotic for bacterial infections',
            'metformin': 'Medication for type 2 diabetes',
            'lisinopril': 'Blood pressure medication (ACE inhibitor)',
            'omeprazole': 'Reduces stomach acid production',
            'atorvastatin': 'Cholesterol-lowering medication (statin)',
            'amlodipine': 'Calcium channel blocker for blood pressure',
            'aspirin': 'Pain reliever and blood thinner',
            'cetirizine': 'Antihistamine for allergies',
            'azithromycin': 'Antibiotic for various infections',
            'prednisone': 'Corticosteroid for inflammation',
            'gabapentin': 'Nerve pain medication',
            'sertraline': 'Antidepressant (SSRI)',
            'losartan': 'Blood pressure medication (ARB)',
        }

    def read_prescription(self, image_path):
        try:
            if not os.path.exists(image_path):
                return "Error: Image file not found"

            image = Image.open(image_path)

            text = pytesseract.image_to_string(image)

            cleaned_text = self.clean_text(text)

            if not cleaned_text or len(cleaned_text.strip()) < 10:
                return "Unable to extract text from the image. Please ensure the prescription is clear and well-lit."

            return cleaned_text

        except Exception as e:
            return f"Error processing prescription: {str(e)}"

    def clean_text(self, text):
        text = re.sub(r'\s+', ' ', text)
        text = text.strip()
        return text

    def analyze_prescription(self, prescription_text):
        analysis = {
            'medications_found': [],
            'instructions': [],
            'warnings': [],
            'simplified_text': ''
        }

        text_lower = prescription_text.lower()

        for med_name, med_description in self.medication_database.items():
            if med_name in text_lower:
                analysis['medications_found'].append({
                    'name': med_name.capitalize(),
                    'description': med_description
                })

        dosage_patterns = [
            r'\d+\s*mg',
            r'\d+\s*ml',
            r'\d+\s*tablets?',
            r'\d+\s*times?\s*(?:a|per)\s*day',
            r'once\s*daily',
            r'twice\s*daily',
            r'before\s*meals?',
            r'after\s*meals?',
        ]

        for pattern in dosage_patterns:
            matches = re.findall(pattern, text_lower, re.IGNORECASE)
            if matches:
                analysis['instructions'].extend(matches)

        warning_keywords = ['antibiotic', 'complete course', 'do not', 'avoid', 'contraindication']
        if any(keyword in text_lower for keyword in warning_keywords):
            analysis['warnings'].append('Follow the prescribed course completely')
            analysis['warnings'].append('Do not stop medication without consulting your doctor')

        if 'antibiotic' in text_lower or any(med in text_lower for med in ['amoxicillin', 'azithromycin']):
            analysis['warnings'].append('Complete the full antibiotic course even if you feel better')

        analysis['simplified_text'] = self.simplify_medical_terms(prescription_text)

        return analysis

    def simplify_medical_terms(self, text):
        simplifications = {
            'q.d.': 'once daily',
            'b.i.d.': 'twice daily',
            't.i.d.': 'three times daily',
            'q.i.d.': 'four times daily',
            'p.r.n.': 'as needed',
            'p.o.': 'by mouth',
            'a.c.': 'before meals',
            'p.c.': 'after meals',
            'h.s.': 'at bedtime',
            'stat': 'immediately',
            'mg': 'milligrams',
            'ml': 'milliliters',
            'tabs': 'tablets',
            'caps': 'capsules',
        }

        simplified = text
        for abbr, full_form in simplifications.items():
            simplified = re.sub(r'\b' + re.escape(abbr) + r'\b', full_form, simplified, flags=re.IGNORECASE)

        return simplified

    def extract_prescription_details(self, text):
        details = {
            'patient_name': self.extract_patient_name(text),
            'doctor_name': self.extract_doctor_name(text),
            'date': self.extract_date(text),
            'medications': self.extract_medications(text)
        }
        return details

    def extract_patient_name(self, text):
        patterns = [r'patient:?\s*([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)', r'name:?\s*([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)']
        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                return match.group(1)
        return None

    def extract_doctor_name(self, text):
        patterns = [r'dr\.?\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)', r'doctor:?\s*([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)']
        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                return match.group(1)
        return None

    def extract_date(self, text):
        patterns = [r'\d{1,2}[/-]\d{1,2}[/-]\d{2,4}', r'\d{4}[/-]\d{1,2}[/-]\d{1,2}']
        for pattern in patterns:
            match = re.search(pattern, text)
            if match:
                return match.group(0)
        return None

    def extract_medications(self, text):
        medications = []
        for med_name in self.medication_database.keys():
            if med_name in text.lower():
                medications.append(med_name.capitalize())
        return medications
