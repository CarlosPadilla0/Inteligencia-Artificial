import pandas as pd
import re
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

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

vectorizer = TfidfVectorizer(max_features=5000) 
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

nb_classifier = MultinomialNB()
nb_classifier.fit(X_train_tfidf, y_train)

y_pred = nb_classifier.predict(X_test_tfidf)

accuracy = accuracy_score(y_test, y_pred)
print(f"Precisión: {accuracy:.2f}")
print(classification_report(y_test, y_pred))
