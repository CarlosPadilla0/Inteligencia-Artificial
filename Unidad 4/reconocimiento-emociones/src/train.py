import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import load_model, Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, BatchNormalization, GlobalAveragePooling2D
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint, ReduceLROnPlateau, TensorBoard
from tensorflow.keras.applications import MobileNetV2
import random
import datetime
import matplotlib.pyplot as plt
import argparse

# Reproducibilidad
SEED = 42
np.random.seed(SEED)
tf.random.set_seed(SEED)
random.seed(SEED)

# Argumentos por línea de comandos
parser = argparse.ArgumentParser(description='Entrenamiento de red neuronal para reconocimiento de emociones')
parser.add_argument('--epochs', type=int, default=50, help='Número de épocas')
parser.add_argument('--batch', type=int, default=32, help='Tamaño de batch')
parser.add_argument('--lr', type=float, default=0.001, help='Learning rate')
parser.add_argument('--patience', type=int, default=20, help='Patience para EarlyStopping (más alto = más aprendizaje)')
parser.add_argument('--monitor', type=str, default='val_loss', help='Métrica a monitorear para EarlyStopping')
parser.add_argument('--logdir', type=str, default='logs', help='Directorio para logs de TensorBoard')
args = parser.parse_args()

# Directorios de datos (usar rutas absolutas basadas en la ubicación del script)
script_dir = os.path.dirname(os.path.abspath(__file__))
ruta_entrenamiento = os.path.join(script_dir, '../data/train')
ruta_validacion = os.path.join(script_dir, '../data/valid')
ruta_prueba = os.path.join(script_dir, '../data/test')

# Cambiar tamaño de imagen a 224x224 para MobileNetV2
ancho_img, alto_img = 224, 224
lote = args.batch
epocas = args.epochs

# Generadores de datos con data augmentation para entrenamiento
entrenamiento_datagen = ImageDataGenerator(
    rescale=1.0/255,
    rotation_range=25,
    width_shift_range=0.25,
    height_shift_range=0.25,
    shear_range=0.2,
    zoom_range=0.25,
    horizontal_flip=True,
    brightness_range=[0.8,1.2],
    fill_mode='nearest'
)
validacion_datagen = ImageDataGenerator(rescale=1.0/255)

test_datagen = ImageDataGenerator(rescale=1.0/255)
test_generador = test_datagen.flow_from_directory(
    ruta_prueba,
    target_size=(ancho_img, alto_img),
    batch_size=lote,
    class_mode='categorical',
    shuffle=False
)

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
    print('Creando un modelo nuevo con MobileNetV2 (transfer learning y fine-tuning)...')
    base_model = MobileNetV2(weights='imagenet', include_top=False, input_shape=(ancho_img, alto_img, 3))
    # Congelar todas las capas excepto las últimas 30
    for layer in base_model.layers[:-30]:
        layer.trainable = False
    for layer in base_model.layers[-30:]:
        layer.trainable = True
    modelo = Sequential([
        base_model,
        GlobalAveragePooling2D(),
        Dense(128, activation='relu'),
        Dropout(0.5),
        Dense(entrenamiento_generador.num_classes, activation='softmax')
    ])

# Usar un learning rate más bajo para fine-tuning
optimizer = tf.keras.optimizers.Adam(learning_rate=args.lr * 0.1)
modelo.compile(loss='categorical_crossentropy',
               optimizer=optimizer,
               metrics=['accuracy'])

# Early stopping y checkpoint para evitar sobreajuste
fecha = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
tensorboard_callback = TensorBoard(log_dir=os.path.join(args.logdir, fecha))
callbacks = [
    EarlyStopping(monitor=args.monitor, patience=args.patience, restore_best_weights=True, verbose=1),
    ModelCheckpoint('src/model.h5', save_best_only=True, monitor='val_accuracy', verbose=1),
    ReduceLROnPlateau(monitor='val_loss', factor=0.5, patience=5, min_lr=1e-6, verbose=1),
    tensorboard_callback
]
steps_per_epoch = int(np.ceil(entrenamiento_generador.samples / lote))
validation_steps = int(np.ceil(validacion_generador.samples / lote))

if __name__ == "__main__":
    try:
        t0 = datetime.datetime.now()
        historial = modelo.fit(
            entrenamiento_generador,
            steps_per_epoch=steps_per_epoch,
            validation_data=validacion_generador,
            validation_steps=validation_steps,
            epochs=epocas,
            callbacks=callbacks
        )
        t1 = datetime.datetime.now()
        print(f"Tiempo total de entrenamiento: {t1-t0}")

        # Guardar el modelo en formato SavedModel y Keras
        modelo.save('src/model.keras')
        # Evaluación automática en test
        loss_test, acc_test = modelo.evaluate(test_generador, verbose=1)
        print(f"Exactitud en test: {acc_test*100:.2f}% | Pérdida: {loss_test:.4f}")

        # Graficar accuracy y loss
        plt.figure(figsize=(12,5))
        plt.subplot(1,2,1)
        plt.plot(historial.history['accuracy'], label='Entrenamiento')
        plt.plot(historial.history['val_accuracy'], label='Validación')
        plt.title('Exactitud')
        plt.xlabel('Época')
        plt.ylabel('Exactitud')
        plt.legend()
        plt.subplot(1,2,2)
        plt.plot(historial.history['loss'], label='Entrenamiento')
        plt.plot(historial.history['val_loss'], label='Validación')
        plt.title('Pérdida')
        plt.xlabel('Época')
        plt.ylabel('Pérdida')
        plt.legend()
        plt.tight_layout()
        plt.savefig('src/entrenamiento_metricas.png')
        plt.show()

        print('Entrenamiento finalizado. Usa TensorBoard para visualizar logs:')
        print(f'tensorboard --logdir {args.logdir}')
    except Exception as e:
        print('\n\n¡Ocurrió un error durante el entrenamiento!\n')
        import traceback
        traceback.print_exc()
    input('Presiona Enter para cerrar el script...')
