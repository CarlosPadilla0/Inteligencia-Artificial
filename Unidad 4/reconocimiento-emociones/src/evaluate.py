import os
import numpy as np
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator

def evaluar_modelo(ruta_modelo, dir_test, dir_valid, tam_img=(150, 150), tam_lote=32):
    modelo = load_model(ruta_modelo)

    test_datagen = ImageDataGenerator(rescale=1./255)
    generador_test = test_datagen.flow_from_directory(
        dir_test,
        target_size=tam_img,
        batch_size=tam_lote,
        class_mode='categorical',
        shuffle=False
    )

    valid_datagen = ImageDataGenerator(rescale=1./255)
    generador_valid = valid_datagen.flow_from_directory(
        dir_valid,
        target_size=tam_img,
        batch_size=tam_lote,
        class_mode='categorical',
        shuffle=False
    )

    perdida_test, exactitud_test = modelo.evaluate(generador_test)
    print(f'Pérdida en Test: {perdida_test}, Exactitud en Test: {exactitud_test}')

    perdida_valid, exactitud_valid = modelo.evaluate(generador_valid)
    print(f'Pérdida en Validación: {perdida_valid}, Exactitud en Validación: {exactitud_valid}')

    predicciones_test = modelo.predict(generador_test)
    predicciones_valid = modelo.predict(generador_valid)

    clases_pred_test = np.argmax(predicciones_test, axis=1)
    clases_pred_valid = np.argmax(predicciones_valid, axis=1)

    clases_reales_test = generador_test.classes
    clases_reales_valid = generador_valid.classes

    print("Reporte de Clasificación - Test :")
    reporte_test = classification_report(
        clases_reales_test, clases_pred_test, target_names=generador_test.class_indices.keys(), output_dict=True
    )
    encabezados = ['precisión', 'sensibilidad', 'puntaje-F1', 'soporte']
    print(f"{'':12}{encabezados[0]:>10}{encabezados[1]:>14}{encabezados[2]:>12}{encabezados[3]:>10}")
    for clase, valores in reporte_test.items():
        if clase in generador_test.class_indices.keys() or clase in ['accuracy', 'macro avg', 'weighted avg']:
            if clase == 'accuracy':
                print(f"{'exactitud total':<12}{'':>10}{'':>14}{valores*100:10.2f}%{reporte_test['macro avg']['support']:>10}")
            else:
                nombre = clase
                if clase == 'macro avg': nombre = 'promedio macro'
                if clase == 'weighted avg': nombre = 'promedio ponderado'
                print(f"{nombre:<12}{valores['precision']:10.2f}{valores['recall']:14.2f}{valores['f1-score']:12.2f}{valores['support']:10}")
    print(f"\nPorcentaje de exactitud en Test: {exactitud_test*100:.2f}%\n")

    print("Reporte de Clasificación - Validación:")
    reporte_valid = classification_report(
        clases_reales_valid, clases_pred_valid, target_names=generador_valid.class_indices.keys(), output_dict=True
    )
    print(f"{'':12}{encabezados[0]:>10}{encabezados[1]:>14}{encabezados[2]:>12}{encabezados[3]:>10}")
    for clase, valores in reporte_valid.items():
        if clase in generador_valid.class_indices.keys() or clase in ['accuracy', 'macro avg', 'weighted avg']:
            if clase == 'accuracy':
                print(f"{'exactitud total':<12}{'':>10}{'':>14}{valores*100:10.2f}%{reporte_valid['macro avg']['support']:>10}")
            else:
                nombre = clase
                if clase == 'macro avg': nombre = 'promedio macro'
                if clase == 'weighted avg': nombre = 'promedio ponderado'
                print(f"{nombre:<12}{valores['precision']:10.2f}{valores['recall']:14.2f}{valores['f1-score']:12.2f}{valores['support']:10}")
    print(f"\nPorcentaje de exactitud en Validación: {exactitud_valid*100:.2f}%\n")

    matriz_conf_test = confusion_matrix(clases_reales_test, clases_pred_test)
    plt.figure(figsize=(10, 7))
    sns.heatmap(matriz_conf_test, annot=True, fmt='d', cmap='Blues', xticklabels=generador_test.class_indices.keys(), yticklabels=generador_test.class_indices.keys())
    plt.title('Matriz de Confusión - Datos de Test')
    plt.xlabel('Predicho')
    plt.ylabel('Real')
    plt.show()

    matriz_conf_valid = confusion_matrix(clases_reales_valid, clases_pred_valid)
    plt.figure(figsize=(10, 7))
    sns.heatmap(matriz_conf_valid, annot=True, fmt='d', cmap='Blues', xticklabels=generador_valid.class_indices.keys(), yticklabels=generador_valid.class_indices.keys())
    plt.title('Matriz de Confusión - Datos de Validación')
    plt.xlabel('Predicho')
    plt.ylabel('Real')
    plt.show()

if __name__ == "__main__":
    ruta_modelo = 'src/model.h5' 
    dir_test = 'data/test' 
    dir_valid = 'data/valid' 
    evaluar_modelo(ruta_modelo, dir_test, dir_valid, tam_img=(150, 150))


# cd "Unidad 4\reconocimiento-emociones"
#.\src\.venv\Scripts\Activate