# Descripción del Data Set

El archivo `Data Set.txt` contiene el enlace al conjunto de datos utilizado para el entrenamiento y evaluación del sistema de reconocimiento de emociones faciales.

## Enlace al Data Set

- URL: https://universe.roboflow.com/firstworkspace-xum67/facial-emotion-detection-u5evn/dataset/1

## Uso del Data Set

Este data set proporciona imágenes de rostros humanos clasificadas según diferentes emociones (por ejemplo: felicidad, tristeza, enojo, sorpresa, etc.).

### ¿Cómo se utiliza?

1. **Descarga:** Accede al enlace y descarga el conjunto de datos. Es posible que necesites crear una cuenta gratuita en Roboflow para obtener acceso.
2. **Estructura:** Organiza las imágenes descargadas en las carpetas `train/`, `test/` y `valid/` dentro de la carpeta `data/` del proyecto, siguiendo la estructura indicada en el README principal.
3. **Entrenamiento y Prueba:** El sistema utiliza estas imágenes para entrenar el modelo de reconocimiento de emociones y para evaluar su desempeño.

### Notas
- Asegúrate de mantener la estructura de carpetas por emoción para que los scripts de entrenamiento y evaluación funcionen correctamente.
- El data set es fundamental para el correcto funcionamiento del sistema, ya que de él depende la capacidad del modelo para aprender a reconocer emociones en imágenes nuevas.
