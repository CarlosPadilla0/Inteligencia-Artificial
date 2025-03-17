import pandas as pd
import re

class SpamDetector:
    def __init__(self):
        # Palabras claves
        self.spam_keywords = [
            "free", "offer", "win", "prize", "click here", "urgent", "congratulations",
            "discount", "buy now", "subscribe", "money", "lottery", "limited time",
            "work from home", "earn $1000 per day", "exclusive deal", "make money fast",
            "get rich quick", "guaranteed weight loss", "verify your account", 
            "your account has been suspended", "click here to reset your password",
            "urgent action required", "viagra", "cialis","meet singles"
        ] 
        
        # dominios sospechosos
        self.suspicious_domains = ["spam.com", "freeoffers.com", "easy-money.net", "cheapmeds.com", "click-me-now.net", "discounts.org",
        "lottery.net", "you-are-a-winner.com", "earn-money.org", "work-from-home.biz", "urgent-message.com", "verify-account.net", "reset-password-now.com", 
        "suspended-account.com", "weightlossguaranteed.com", "get-rich-quick.net", "meet-singles.net", "viagra-pills.net", "cialis-pills.net",".co",".xyz",".info",".club",".top",".site",
        ".bid",".win",".vip",".work",".space",".website",".tech",".online",".store",".shop",".site",".fun",".press",".news",".social",".buzz",".cool",".pro",".click",".link",".live",".video",
        ".guru",".ninja",".expert",".money",".cash",".today",".world",".zone",".network",".email",".digital",".media",".marketing",".agency",".software",".systems",".solutions",".services",
        ".consulting",".business",".enterprises",".company",".management",".gg",".to",".cf",".gq",".cm",".tk","tm","ly","ga",".us"
        ]

        # Acortadores de URL
        self.url_shorteners = ["bit.ly", "tinyurl.com", "goo.gl", "shorte.st","t.co", "ow.ly", "buff.ly", "rebrand.ly", "cli.gs", "tr.im", "is.gd", 
        "tiny.cc", "snipurl.com", "shorturl.at", "shorturl.co", "shorturl.to", "shorturl.link", "shorturl.pw", "shorturl.gg", "shorturl.us", "shorturl.icu", "shorturl.cf", 
        "shorturl.gq", "shorturl.ml", "shorturl.ga", "shorturl.tk", "shorturl.gq", "shorturl.cm"]
        
        # Palabras clave de adjuntos
        self.attachment_keywords = [
        "attachment", "file attached", "download now", "see the attached file",
        "invoice attached", "payment proof attached", "screenshot attached"
        ]
        # Extensiones de archivo sospechosas
        self.suspicious_extensions = [".zip", ".rar", ".exe", ".pdf", ".docx", ".xlsm", ".apk"]

        
    def is_spam(self, email):
        score = 0
        reasons = []
        
        # Regla 2: Uso excesivo de mayúsculas (más del 50% del mensaje)
        uppercase_ratio = sum(1 for c in email if c.isupper()) / max(len(email), 1)
        if uppercase_ratio > 0.5:
            score += 2
            reasons.append("Uso excesivo de mayúsculas")

        email = email.lower()  

        # Regla 1: Palabras clave de spam
        if any(word in email for word in self.spam_keywords):
            score += 2
            reasons.append("Palabras clave de spam")

        # Regla 3: Uso excesivo de caracteres especiales (más del 10% del mensaje)
        special_chars_ratio = sum(1 for c in email if c in "!?!") / max(len(email), 1)
        if special_chars_ratio > 0.1:
            score += 2
            reasons.append("Uso excesivo de caracteres especiales")

        # Regla 4: Contiene dominios sospechosos
        if any(domain in email for domain in self.suspicious_domains):
            score += 3
            reasons.append("Contiene dominios sospechosos")

        # Regla 5: Contiene acortadores de URL
        if any(shortener in email for shortener in self.url_shorteners):
            score += 3
            reasons.append("Contiene acortadores de URL")

        # Regla 6: Longitud del mensaje (menos de 5 palabras o más de 300 palabras)
        words = email.split()
        if len(words) < 5 or len(words) > 300:
            score += 2
            reasons.append("Longitud del mensaje")

        # Regla 7: Caracteres repetidos (más de 4 veces)
        if re.search(r"(.)\1{4,}", email):  # More than 4 repeated characters
            score += 2
            reasons.append("Caracteres repetidos")

        # Regla 8: Emojis (más de 5 emojis)
        if sum(1 for c in email if c in "😂🤣😍😜😎🔥💰💵🎁🎉") > 5:
            score += 2
            reasons.append("Uso excesivo de emojis")

        # Regla 9: Contiene múltiples enlaces y pocos textos significativos
        urls = re.findall(r"https?://\S+", email)
        if len(urls) > 0 and len(urls) / max(len(words), 1) > 0.5:
            score += 3
            reasons.append("Contiene múltiples enlaces y pocos textos significativos")

        # Regla 10: Contiene un solo enlace y pocos textos significativos
        if len(urls) == 1 and len(words) < 10:
            score += 3
            reasons.append("Contiene un solo enlace y pocos textos significativos")

        # Regla 11: Uso de iniciales en mayúsculas (por ejemplo, "U S A")
        if re.search(r"\b([A-Z])\s([A-Z])\s([A-Z])\b", email):
            score += 2
            reasons.append("Uso de iniciales en mayúsculas")

        # Regla 12: Contiene más de 3 líneas en blanco
        blank_lines = email.count("\n\n")
        if blank_lines > 3:
            score += 2
            reasons.append("Contiene más de 3 líneas en blanco")
        
        # Regla 13: Contiene palabras clave de adjuntos
        if any(word in email for word in self.attachment_keywords):
            score += 3
            reasons.append("Contiene palabras clave de adjuntos")

        # Regla 14: Contiene extensiones de archivo sospechosas
        if any(ext in email for ext in self.suspicious_extensions):
            score += 4
            reasons.append("Contiene extensiones de archivo sospechosas")

        # Regla 15: Contiene frases como "screenshot attached" o "see the image below"
        if "screenshot attached" in email or "see the image below" in email:
            score += 2
            reasons.append("Contiene frases como 'screenshot attached' o 'see the image below'")

        is_spam = score >= 5
        return is_spam, score, reasons

def analyze_csv(file_path):
    df = pd.read_csv(file_path)
    detector = SpamDetector()

    results = []
    spam_count = 0
    for index, row in df.iterrows():
        is_spam, score, reasons = detector.is_spam(row['text'])
        reason_str = ", ".join(reasons) if reasons else "None"
        results.append(f"ID.{index} Spam={is_spam} | Score={score} | Reason: {reason_str}")
        if is_spam:
            spam_count += 1

    for result in results[100:120]:
        print(result)
    
    spam_percentage = (spam_count / len(df)) * 100
    print(f"\nPorcentaje de correos detectados como spam: {spam_percentage:.2f}%")

csv_file = r"C:\Users\Carlo\Documents\Repos\Inteligencia-Artificial\Unidad 2\Tarea3_DetectorSpam\spam_ham_dataset.csv"  
analyze_csv(csv_file)

