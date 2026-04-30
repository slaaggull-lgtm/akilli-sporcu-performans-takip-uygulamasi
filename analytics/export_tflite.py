import tensorflow as tf
import numpy as np

# Simple model to predict Performance Score based on metrics
def create_and_export_tflite():
    # Placeholder training data: [speed, cadence, hr_ratio]
    X_train = np.array([
        [10.0, 160, 0.7], [12.0, 170, 0.8], [8.0, 150, 0.65], 
        [15.0, 185, 0.9], [11.0, 165, 0.75]
    ], dtype=np.float32)
    # Target score: 0-100
    y_train = np.array([60, 75, 45, 90, 68], dtype=np.float32)

    model = tf.keras.Sequential([
        tf.keras.layers.Dense(8, activation='relu', input_shape=(3,)),
        tf.keras.layers.Dense(1)
    ])
    
    model.compile(optimizer='adam', loss='mse')
    model.fit(X_train, y_train, epochs=10, verbose=0)

    # Convert to TFLite
    converter = tf.lite.TFLiteConverter.from_keras_model(model)
    tflite_model = converter.convert()

    # Save the model
    with open('analytics/models/running_model.tflite', 'wb') as f:
        f.write(tflite_model)
    print("TensorFlow Lite model exported to analytics/models/running_model.tflite")

if __name__ == "__main__":
    create_and_export_tflite()
