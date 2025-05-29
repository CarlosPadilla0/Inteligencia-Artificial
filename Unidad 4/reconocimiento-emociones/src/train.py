import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import load_model, Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint

# Directorios de datos
ruta_entrenamiento = '../data/train'
ruta_validacion = '../data/valid'
ruta_prueba = '../data/test'

ancho_img, alto_img = 150, 150
lote = 64  
epocas = 100 

# Generadores de datos con data augmentation para entrenamiento
entrenamiento_datagen = ImageDataGenerator(
    rescale=1.0/255,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.15,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)
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

# Early stopping y checkpoint para evitar sobreajuste
callbacks = [
    EarlyStopping(monitor='val_loss', patience=8, restore_best_weights=True),
    ModelCheckpoint('src/model.h5', save_best_only=True)
]

# Calcular steps_per_epoch y validation_steps correctamente
steps_per_epoch = int(np.ceil(entrenamiento_generador.samples / lote))
validation_steps = int(np.ceil(validacion_generador.samples / lote))

historial = modelo.fit(
    entrenamiento_generador,
    steps_per_epoch=steps_per_epoch,
    validation_data=validacion_generador,
    validation_steps=validation_steps,
    epochs=epocas,
    callbacks=callbacks
)

# Mostrar el porcentaje de exactitud final de entrenamiento y validación
exactitud_entrenamiento = historial.history['accuracy'][-1]
exactitud_validacion = historial.history['val_accuracy'][-1]
print(f'Porcentaje de exactitud final en entrenamiento: {exactitud_entrenamiento*100:.2f}%')
print(f'Porcentaje de exactitud final en validación: {exactitud_validacion*100:.2f}%')

# Guardar el modelo en formato Keras moderno y también en HDF5 por compatibilidad
modelo.save('src/model.keras')
