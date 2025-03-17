import re

class detector_Patrones:
    def __init__(self):
        self.patterns = [
            r"\b(?:[A-Z]{2,}\s){2,}[A-Z]{2,}\b",  # Uso de iniciales en mayúsculas (por ejemplo, "U S A")
            r"(.)\1{4,}",  # Caracteres repetidos (más de 4 veces)
            r"https?://\S+",  # URLs
            r"\b(?:free|offer|win|prize|click here|urgent|congratulations|discount|buy now|subscribe|money|lottery|limited time|work from home|earn \$1000 per day|exclusive deal|make money fast|get rich quick|guaranteed weight loss|verify your account|your account has been suspended|click here to reset your password|urgent action required|viagra|cialis|meet singles)\b",  # Palabras clave de spam
            r"\b(?:bit\.ly|tinyurl\.com|goo\.gl|shorte\.st|t\.co|ow\.ly|buff\.ly|rebrand\.ly|cli\.gs|tr\.im|is\.gd|tiny\.cc|snipurl\.com|shorturl\.at|shorturl\.co|shorturl\.to|shorturl\.link|shorturl\.pw|shorturl\.gg|shorturl\.us|shorturl\.icu|shorturl\.cf|shorturl\.gq|shorturl\.ml|shorturl\.ga|shorturl\.tk|shorturl\.gq|shorturl\.cm)\b",  # Acortadores de URL
            r"\b(?:attachment|file attached|download now|see the attached file|invoice attached|payment proof attached|screenshot attached)\b",  # Palabras clave de adjuntos
            r"\b(?:\.zip|\.rar|\.exe|\.pdf|\.docx|\.xlsm|\.apk)\b",  # Extensiones de archivo sospechosas
            r"\b(?:😂|🤣|😍|😜|😎|🔥|💰|💵|🎁|🎉)\b",  # Emojis
        ]

    def detect_patterns(self, email):
        detected_patterns = []
        for pattern in self.patterns:
            if re.search(pattern, email):
                detected_patterns.append(pattern)
        return detected_patterns

# Ejemplo de uso
if __name__ == "__main__":
    email = "Congratulations! You have won a prize. Click here to claim your reward: http://bit.ly/12345"
    detector = detector_Patrones()
    patterns = detector.detect_patterns(email)
    print("Patrones detectados:", patterns)