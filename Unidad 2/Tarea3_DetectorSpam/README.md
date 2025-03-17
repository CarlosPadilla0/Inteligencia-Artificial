# Proyecto: Detector de Spam

## Descripción

Este proyecto implementa un detector de spam utilizando reglas y patrones predefinidos. El objetivo es analizar correos electrónicos y determinar si son spam o no, basándose en diversas características sospechosas.

## Estructura del Proyecto

- `detector_Patrones.py`: Contiene la clase `detector_Patrones` que se encarga de detectar patrones sospechosos en los correos electrónicos.
- `spam.py`: Contiene la clase `SpamDetector` que utiliza reglas específicas para evaluar si un correo electrónico es spam. También incluye una función para analizar un archivo CSV con correos electrónicos.
- `spam_ham_dataset.csv`: Archivo CSV con ejemplos de correos electrónicos etiquetados como spam o ham (no spam).

## Clases y Métodos

### Clase `detector_Patrones`

Esta clase se encarga de detectar patrones sospechosos en los correos electrónicos. Los patrones incluyen:

- Uso de iniciales en mayúsculas (por ejemplo, "U S A")
- Caracteres repetidos (más de 4 veces)
- URLs
- Palabras clave de spam (por ejemplo, "free", "offer", "win", etc.)
- Acortadores de URL (por ejemplo, "bit.ly", "tinyurl.com", etc.)
- Palabras clave de adjuntos (por ejemplo, "attachment", "file attached", etc.)
- Extensiones de archivo sospechosas (por ejemplo, ".zip", ".rar", ".exe", etc.)
- Emojis (por ejemplo, "😂", "🤣", "😍", etc.)

### Clase `SpamDetector`

Esta clase utiliza reglas específicas para evaluar si un correo electrónico es spam. Las reglas incluyen:

- Uso excesivo de mayúsculas (más del 50% del mensaje)
- Palabras clave de spam
- Uso excesivo de caracteres especiales (más del 10% del mensaje)
- Contiene dominios sospechosos
- Contiene acortadores de URL
- Longitud del mensaje (menos de 5 palabras o más de 300 palabras)
- Caracteres repetidos (más de 4 veces)
- Uso excesivo de emojis (más de 5 emojis)
- Contiene múltiples enlaces y pocos textos significativos
- Contiene un solo enlace y pocos textos significativos
- Uso de iniciales en mayúsculas (por ejemplo, "U S A")
- Contiene más de 3 líneas en blanco
- Contiene palabras clave de adjuntos
- Contiene extensiones de archivo sospechosas
- Contiene frases como "screenshot attached" o "see the image below"


## Ejemplo de Uso

Para utilizar el detector de patrones:

```python
from detector_Patrones import detector_Patrones

email = "Congratulations! You have won a prize. Click here to claim your reward: http://bit.ly/12345"
detector = detector_Patrones()
patterns = detector.detect_patterns(email)
print("Patrones detectados:", patterns)
```

## Ejemplo de resultado

- ID.100 Spam=False | Score=3 | Reason: Contiene dominios sospechosos
- ID.101 Spam=True | Score=5 | Reason: Contiene dominios sospechosos, Longitud del mensaje
- ID.102 Spam=False | Score=3 | Reason: Contiene dominios sospechosos
- ID.103 Spam=True | Score=5 | Reason: Palabras clave de spam, Contiene dominios sospechosos
- ID.104 Spam=False | Score=4 | Reason: Uso excesivo de caracteres especiales, Caracteres repetidos
- ID.105 Spam=False | Score=0 | Reason: None
- ID.106 Spam=False | Score=0 | Reason: None
- ID.107 Spam=False | Score=0 | Reason: None
- ID.108 Spam=False | Score=0 | Reason: None
- ID.109 Spam=False | Score=3 | Reason: Contiene dominios sospechosos
- ID.110 Spam=True | Score=5 | Reason: Palabras clave de spam, Contiene dominios sospechosos

Porcentaje de correos detectados como spam: 38.04%


## Fuente de datos 
https://www.kaggle.com/datasets/venky73/spam-mails-dataset/data

