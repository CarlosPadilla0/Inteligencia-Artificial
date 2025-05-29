import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import load_model, Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout

# Directorios de datos
ruta_entrenamiento = 'data/train'
ruta_validacion = 'data/valid'
ruta_prueba = 'data/test'

ancho_img, alto_img = 150, 150
lote = 32
epocas = 50

# Generadores de datos
entrenamiento_datagen = ImageDataGenerator(rescale=1.0/255)
validacion_datagen = ImageDataGenerator(rescale=1.0/255)

entrenamiento_generador = entrenamiento_datagen.flow_from_directory(
    ruta_entrenamiento,
    target_size=(ancho_img, alto_img),
    batch_size=lote,
    class_mode='categorical'
)

validacion_generador = validacion_datagen.flow_from_directory(
    ruta_validacion,
    target_size=(ancho_img, alto_img),
    batch_size=lote,
    class_mode='categorical'
)

# Comprobar si existe un modelo guardado, si no, crear uno nuevo
ruta_modelo = 'src/model.h5'
if os.path.exists(ruta_modelo):
    print('Cargando modelo existente...')
    modelo = load_model(ruta_modelo)
else:
    print('Creando un modelo nuevo...')
    modelo = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=(ancho_img, alto_img, 3)),
        MaxPooling2D(2, 2),
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D(2, 2),
        Conv2D(128, (3, 3), activation='relu'),
        MaxPooling2D(2, 2),
        Flatten(),
        Dense(128, activation='relu'),
        Dropout(0.5),
        Dense(entrenamiento_generador.num_classes, activation='softmax')
    ])

modelo.compile(loss='categorical_crossentropy',
               optimizer='adam',
               metrics=['accuracy'])

historial = modelo.fit(
    entrenamiento_generador,
    steps_per_epoch=entrenamiento_generador.samples // lote,
    validation_data=validacion_generador,
    validation_steps=validacion_generador.samples // lote,
    epochs=epocas
)

# Mostrar el porcentaje de exactitud final de entrenamiento y validación
exactitud_entrenamiento = historial.history['accuracy'][-1]
exactitud_validacion = historial.history['val_accuracy'][-1]
print(f'Porcentaje de exactitud final en entrenamiento: {exactitud_entrenamiento*100:.2f}%')
print(f'Porcentaje de exactitud final en validación: {exactitud_validacion*100:.2f}%')

modelo.save('src/model.h5')