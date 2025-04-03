import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
from spam import SpamDetector  

def preprocess_text(text):
    text = text.lower()  
    text = re.sub(r'\W', ' ', text)  
    text = re.sub(r'\s+', ' ', text) 
    return text.strip()

csv_file = r"C:\Users\Carlo\Documents\Repos\Inteligencia-Artificial\Unidad 2\Tarea3_DetectorSpam\spam_ham_dataset.csv"
df = pd.read_csv(csv_file)

df['text'] = df['text'].apply(preprocess_text)
df['label'] = df['label'].map({'spam': 1, 'ham': 0})

X_train, X_test, y_train, y_test = train_test_split(df['text'], df['label'], test_size=0.2, random_state=42)

# Vectorización del texto
vectorizer = TfidfVectorizer(max_features=5000) 
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# Entrenar el modelo Naive Bayes
nb_classifier = MultinomialNB()
nb_classifier.fit(X_train_tfidf, y_train)

# Predicciones 
y_pred = nb_classifier.predict(X_test_tfidf)

# Evaluación 
accuracy = accuracy_score(y_test, y_pred)
print(f"Precisión del modelo Naive Bayes: {accuracy:.2f}")
print(classification_report(y_test, y_pred))


detector = SpamDetector()

print("\n--- Análisis combinado (Naive Bayes + Reglas) ---")
for index, email in enumerate(X_test[:10]):  # Analizamos los primeros 10 correos de prueba
    is_spam_model = y_pred[index] == 1
    is_spam_rules, score, reasons = detector.is_spam(email)

    print(f"Correo {index + 1}:")
    print(f"Texto: {email}")
    print(f"Predicción del modelo: {'Spam' if is_spam_model else 'Ham'}")
    print(f"Análisis basado en reglas: {'Spam' if is_spam_rules else 'Ham'}")
    print(f"Razones (reglas): {', '.join(reasons) if reasons else 'Ninguna'}")
    print("-" * 50)
