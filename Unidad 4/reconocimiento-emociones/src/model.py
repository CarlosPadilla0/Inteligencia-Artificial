from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout

def crear_modelo(forma_entrada, num_clases):
    modelo = Sequential()
    
    modelo.add(Conv2D(32, (3, 3), activation='relu', input_shape=forma_entrada))
    modelo.add(MaxPooling2D(pool_size=(2, 2)))
    
    modelo.add(Conv2D(64, (3, 3), activation='relu'))
    modelo.add(MaxPooling2D(pool_size=(2, 2)))
    
    modelo.add(Conv2D(128, (3, 3), activation='relu'))
    modelo.add(MaxPooling2D(pool_size=(2, 2)))
    
    modelo.add(Flatten())
    
    modelo.add(Dense(128, activation='relu'))
    modelo.add(Dropout(0.5))
    
    modelo.add(Dense(num_clases, activation='softmax'))
    
    return modelo