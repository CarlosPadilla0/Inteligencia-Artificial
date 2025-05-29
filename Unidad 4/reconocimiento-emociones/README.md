# Reconocimiento de Emociones

Este proyecto tiene como objetivo desarrollar un modelo de machine learning para reconocer emociones a partir de imágenes. Utiliza un conjunto de datos de imágenes organizadas en diferentes carpetas según la emoción que representan.

## Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

```
reconocimiento-emociones
├── data
│   ├── train
│   │   ├── angry
│   │   ├── disgust
│   │   ├── fear
│   │   ├── happy
│   │   ├── sad
│   │   └── surprise
│   ├── test
│   │   ├── angry
│   │   ├── disgust
│   │   ├── fear
│   │   ├── happy
│   │   ├── sad
│   │   └── surprise
│   └── valid
│       ├── angry
│       ├── disgust
│       ├── fear
│       ├── happy
│       ├── sad
│       └── surprise
├── src
│   ├── model.py
│   ├── train.py
│   └── evaluate.py
├── requirements.txt
└── README.md
```

## Descripción de Archivos

- **data/train/**: Contiene las imágenes de entrenamiento organizadas por emociones: `angry`, `disgust`, `fear`, `happy`, `sad`, y `surprise`.
- **data/test/**: Contiene las imágenes de prueba organizadas por emociones.
- **data/valid/**: Contiene las imágenes de validación organizadas por emociones.
- **notebooks/procesamiento.ipynb**: Cuaderno de Jupyter para análisis exploratorios de datos y visualización.
- **src/data_preprocessing.py**: Funciones para cargar y preprocesar imágenes.
- **src/model.py**: Define la arquitectura del modelo de machine learning.
- **src/train.py**: Código para entrenar el modelo.
- **src/evaluate.py**: Evalúa el rendimiento del modelo.
- **requirements.txt**: Lista de dependencias necesarias para el proyecto.

## Instrucciones

1. Clona este repositorio en tu máquina local.
2. Instala las dependencias listadas en `requirements.txt`.
3. Ejecuta el cuaderno `procesamiento.ipynb` para comenzar con el análisis de datos y el entrenamiento del modelo.

## Cómo ejecutar este proyecto en tu máquina

1. **Crea un entorno virtual de Python:**
   
   En Windows (PowerShell):
   ```powershell
   python -m venv .venv
   .venv\Scripts\Activate
   ```
   En macOS/Linux:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

2. **Instala las dependencias:**
   ```powershell
   pip install -r requirements.txt
   ```

3. **Ejecuta los scripts o notebooks según las instrucciones anteriores.**

> **Nota:** La carpeta `.venv` no se incluye en el repositorio. Cada usuario debe crear su propio entorno virtual y usar `requirements.txt` para instalar las dependencias.

## Ejemplos de Uso

Incluir ejemplos de cómo utilizar el modelo y cómo ejecutar los scripts de entrenamiento y evaluación.

## Contribuciones

Las contribuciones son bienvenidas. Si deseas contribuir, por favor abre un issue o envía un pull request.
