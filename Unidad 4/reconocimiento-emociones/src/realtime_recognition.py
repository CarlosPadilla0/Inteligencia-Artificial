import cv2
import numpy as np
from tensorflow.keras.models import load_model

model = load_model('C:\\Users\\Carlo\\Documents\\Repos\\Inteligencia-Artificial\\Unidad 4\\reconocimiento-emociones\\src\\model.h5')

class_names = ['angry', 'disgust', 'fear', 'happy', 'sad', 'surprise']

IMG_SIZE = (150, 150)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

print('Intentando abrir la cámara...')
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
if not cap.isOpened():
    print('No se pudo abrir la cámara. Verifica que esté conectada y no esté siendo usada por otra aplicación.')
    input('Presiona Enter para salir...')
    exit()
print('¡Cámara abierta! Presiona Q para salir.')

while True:
    ret, frame = cap.read()
    print(f'Frame leído: {ret}')
    if not ret:
        print('No se pudo leer el frame de la cámara.')
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    print(f'Rostros detectados: {len(faces)}')
    if len(faces) == 0:
        cv2.putText(frame, 'No se detectaron rostros', (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,255), 2)
    for (x, y, w, h) in faces:
        face_img = frame[y:y+h, x:x+w]
        face_img = cv2.cvtColor(face_img, cv2.COLOR_BGR2RGB)  # Convertir a RGB
        face_img = cv2.resize(face_img, IMG_SIZE)
        face_img = face_img.astype('float32') / 255.0
        face_img = np.expand_dims(face_img, axis=0)
        print('Antes de la predicción')
        try:
            preds = model.predict(face_img)
            print('Predicción realizada:', preds)
            emotion = class_names[np.argmax(preds)]
        except Exception as e:
            print('Error en la predicción:', e)
            emotion = 'error'
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.putText(frame, emotion, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
    cv2.imshow('Reconocimiento de Emociones', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
input('Script finalizado. Presiona Enter para cerrar...')
