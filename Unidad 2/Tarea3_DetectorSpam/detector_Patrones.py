import re
import csv
from collections import defaultdict

class detector_Patrones:
    def __init__(self):
        self.patterns = [
            r"\b(?:[A-Z]{2,}\s){2,}[A-Z]{2,}\b", 
            r"(.)\1{4,}",  
            r"https?://\S+",  
            r"\b(?:free|offer|win|prize|click here|urgent|congratulations|discount|buy now|subscribe|money|lottery|limited time|work from home|earn \$1000 per day|exclusive deal|make money fast|get rich quick|guaranteed weight loss|verify your account|your account has been suspended|click here to reset your password|urgent action required|viagra|cialis|meet singles)\b",
            r"\b(?:bit\.ly|tinyurl\.com|goo\.gl|shorte\.st|t\.co|ow\.ly|buff\.ly|rebrand\.ly|cli\.gs|tr\.im|is\.gd|tiny\.cc|snipurl\.com|shorturl\.at|shorturl\.co|shorturl\.to|shorturl\.link|shorturl\.pw|shorturl\.gg|shorturl\.us|shorturl\.icu|shorturl\.cf|shorturl\.gq|shorturl\.ml|shorturl\.ga|shorturl\.tk|shorturl\.gq|shorturl\.cm)\b",
            r"\b(?:attachment|file attached|download now|see the attached file|invoice attached|payment proof attached|screenshot attached)\b", 
            r"\b(?:\.zip|\.rar|\.exe|\.pdf|\.docx|\.xlsm|\.apk)\b",  
            r"\b(?:😂|🤣|😍|😜|😎|🔥|💰|💵|🎁|🎉)\b", 
        ]

    def detect_patterns(self, email):
        detected_patterns = []
        for pattern in self.patterns:
            if re.search(pattern, email):
                detected_patterns.append(pattern)
        return detected_patterns

    def detect_patterns_in_csv(self, csv_file_path):
        results = []
        with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                email_text = row['text']
                detected_patterns = self.detect_patterns(email_text)
                results.append({
                    'label': row['label'],
                    'text': email_text,
                    'detected_patterns': detected_patterns
                })
        return results

    def find_common_patterns_in_spam(self, csv_file_path):
        pattern_counts = defaultdict(int)
        spam_emails = []

        with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['label'] == 'spam':
                    email_text = row['text']
                    spam_emails.append(email_text)
                    detected_patterns = self.detect_patterns(email_text)
                    for pattern in detected_patterns:
                        pattern_counts[pattern] += 1

        common_patterns = {pattern: count for pattern, count in pattern_counts.items() if count > 1}
        return common_patterns

if __name__ == "__main__":
    csv_file_path = 'c:\\Users\\Carlo\\Documents\\Repos\\Inteligencia-Artificial\\Unidad 2\\Tarea3_DetectorSpam\\spam_ham_dataset.csv'
    detector = detector_Patrones()
    common_patterns = detector.find_common_patterns_in_spam(csv_file_path)
    print("Patrones comunes en correos spam:")
    for pattern, count in common_patterns.items():
        print(f"Patrón: {pattern}, Frecuencia: {count}")