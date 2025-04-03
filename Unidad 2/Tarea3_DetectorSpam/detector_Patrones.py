import re
import csv
from collections import defaultdict, Counter

class detector_Patrones:
    def __init__(self):
        self.patterns = [
            r"\b(?:[A-Z]{2,}\s){2,}[A-Z]{2,}\b",  # Palabras en mayúsculas consecutivas
            r"(.)\1{4,}",  # Caracteres repetidos
            r"https?://\S+",  # URLs
            r"\b(?:free|offer|win|prize|click here|urgent|congratulations|discount|buy now|subscribe|money|lottery|limited time|work from home|earn \$1000 per day|exclusive deal|make money fast|get rich quick|guaranteed weight loss|verify your account|your account has been suspended|click here to reset your password|urgent action required|viagra|cialis|meet singles)\b",  # Palabras clave
            r"\b(?:bit\.ly|tinyurl\.com|goo\.gl|shorte\.st|t\.co|ow\.ly|buff\.ly|rebrand\.ly|cli\.gs|tr\.im|is\.gd|tiny\.cc|snipurl\.com|shorturl\.at|shorturl\.co|shorturl\.to|shorturl\.link|shorturl\.pw|shorturl\.gg|shorturl\.us|shorturl\.icu|shorturl\.cf|shorturl\.gq|shorturl\.ml|shorturl\.ga|shorturl\.tk|shorturl\.gq|shorturl\.cm)\b",  # Acortadores de URL
            r"\b(?:attachment|file attached|download now|see the attached file|invoice attached|payment proof attached|screenshot attached)\b",  # Adjuntos
            r"\b(?:\.zip|\.rar|\.exe|\.pdf|\.docx|\.xlsm|\.apk)\b",  # Extensiones sospechosas
            r"\b(?:😂|🤣|😍|😜|😎|🔥|💰|💵|🎁|🎉)\b",  # Emojis
        ]

    def detect_patterns(self, email):
        """checa qué patrones coinciden en un email."""
        detected_patterns = []
        for pattern in self.patterns:
            if re.search(pattern, email, re.IGNORECASE):
                detected_patterns.append(pattern)
        return detected_patterns

    def tokenize_and_count(self, text):
        """agarra tokens que coincidan con los patrones."""
        tokens = []
        for pattern in self.patterns:
            matches = re.findall(pattern, text, flags=re.IGNORECASE)
            if matches:
                if isinstance(matches[0], tuple):
                    matches = [m[0] for m in matches if m]
                tokens.extend(matches)
        return Counter(tokens)

    def count_tokens_in_csv(self, csv_file_path, label_filter=None):
        """Cuenta los tokens en CSV"""
        token_counts = Counter()
        with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if label_filter is None or row['label'] == label_filter:
                    tokens = self.tokenize_and_count(row['text'])
                    token_counts.update(tokens)
        return token_counts
    
    def find_common_patterns(self, csv_file_path):
        """Cuenta cuántos emails lo tienen."""
        pattern_counts = defaultdict(int)
        with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['label'] == 'spam':
                    detected_patterns = self.detect_patterns(row['text'])
                    for pattern in detected_patterns:
                        pattern_counts[pattern] += 1
        return pattern_counts
    
    def tokenize_all_words(self, text, min_length=2):
        """Tokeniza las palabras."""
        words = re.findall(r'\b\w+\b', text.lower())
        return Counter([word for word in words if len(word) >= min_length])
    
    def count_all_words_in_csv(self, csv_file_path, label_filter=None, min_length=2):
        """Cuenta palabras en el CSV"""
        word_counts = Counter()
        with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if label_filter is None or row['label'] == label_filter:
                    words = self.tokenize_all_words(row['text'], min_length)
                    word_counts.update(words)
        return word_counts

if __name__ == "__main__":
    #ruta del spam.csv
    csv_file_path = r"C:\Users\Carlo\Documents\Repos\Inteligencia-Artificial\Unidad 2\Tarea3_DetectorSpam\spam_ham_dataset.csv"  

    detector = detector_Patrones()

    # Contar palabras en spam
    spam_word_counts = detector.count_all_words_in_csv(csv_file_path, label_filter='spam', min_length=2)
    print("\n 100 palabras más comunes en spam:")
    for word, count in spam_word_counts.most_common(200):
        print(f"{word}: {count}")

    # Comparar spam vs ham
    ham_word_counts = detector.count_all_words_in_csv(csv_file_path, label_filter='ham', min_length=2)
    print("\n 100 palabras únicas en spam (no en ham):")
    spam_unique_words = set(spam_word_counts) - set(ham_word_counts)
    for word in list(spam_unique_words)[:100]:
        print(f"{word}: {spam_word_counts[word]}")
