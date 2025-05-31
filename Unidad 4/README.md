# Proyecto: Reconocimiento de Rostros y Emociones con Inteligencia Artificial

## Descripción

Este proyecto implementa un sistema de inteligencia artificial capaz de reconocer emociones humanas a partir de imágenes de rostros. Utiliza técnicas de visión por computadora y aprendizaje automático para identificar expresiones faciales y clasificarlas en diferentes emociones (felicidad, tristeza, enojo, sorpresa, etc.).

## Características

- Detección automática de rostros en imágenes.
- Extracción de características faciales relevantes.
- Entrenamiento y evaluación de un modelo de reconocimiento de emociones.
- Identificación y verificación de personas a partir de nuevas imágenes.
- Soporte para agregar nuevos rostros al sistema.

## Estructura del Proyecto

- `reconocimiento-emociones/`: Carpeta principal del sistema de reconocimiento de emociones.
  - `data/`: Contiene las imágenes organizadas en carpetas `train/`, `test/` y `valid/`, cada una con subcarpetas por emoción (`angry`, `disgust`, `fear`, `happy`, `sad`, `surprise`).
  - `src/`: Código fuente del sistema.
    - `model.py`: Define la arquitectura del modelo de machine learning.
    - `train.py`: Entrenamiento del modelo.
    - `evaluate.py`: Evaluación del modelo.
    - `model.h5`: Modelo entrenado guardado.
  - `requirements.txt`: Lista de dependencias necesarias.
  - `README.md`: Documentación específica del módulo.

## Requisitos

- Python 3.x
- Las siguientes librerías (instalables con `pip`):
  - tensorflow
  - keras
  - numpy
  - matplotlib
  - pandas
  - scikit-learn
  - opencv-python
  - seaborn

## Instalación

1. Clona este repositorio en tu máquina local.
2. Crea un entorno virtual (opcional pero recomendado):
   ```powershell
   python -m venv .venv
   .venv\Scripts\Activate
   ```
3. Instala las dependencias:
   ```powershell
   pip install -r reconocimiento-emociones/requirements.txt
   ```

## Uso

1. Prepara el dataset siguiendo la estructura de carpetas indicada en `reconocimiento-emociones/data/`.
2. Para entrenar el modelo ejecuta:
   ```powershell
   python reconocimiento-emociones/src/train.py
   ```
3. Para evaluar el modelo ejecuta:
   ```powershell
   python reconocimiento-emociones/src/evaluate.py
   ```

## Ejemplo de ejecución

```powershell
python reconocimiento-emociones/src/train.py
python reconocimiento-emociones/src/evaluate.py
```

## Créditos y Autores

- Padilla Pimentel Carlos Eduardo
- Diana Leticia Alvarez Moreno

## Notas adicionales

- El dataset utilizado puede descargarse desde el enlace especificado en `Data Set.txt`.
- Si deseas contribuir, abre un issue o pull request.
