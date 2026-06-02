"""
TensorFlow Lite Model Olusturma ve Disa Aktarimi
Kosu verilerinden performans skoru tahmin eden modeli egitir
ve mobil uygulamaya gomulmek uzere .tflite formatinda kaydeder.

Model Girdileri:
  - Hiz (km/saat)
  - Kadans (adim/dakika)
  - Nabiz Orani (ortalama nabiz / maksimum nabiz)

Model Ciktisi:
  - Performans Skoru (0-100 arasi)
"""

import numpy as np

try:
    import tensorflow as tf
    TF_AVAILABLE = True
except ImportError:
    TF_AVAILABLE = False
    print("TensorFlow yuklu degil. Sadece veri hazirlama gosterilecek.")


def prepare_training_data():
    """
    Ornek egitim verisi hazirlar.
    Gercek projede giyilebilir sensorlerden toplanan veriler kullanilir.

    Donus degeri:
        tuple: (X_train, y_train) — ozellikler ve etiketler
    """
    # [Hiz (km/h), Kadans (SPM), Nabiz Orani]
    X_train = np.array([
        [8.0,  150, 0.65],   # Yavash kos, dusuk yogunluk -> dusuk skor
        [10.0, 160, 0.70],   # Orta tempo
        [12.0, 170, 0.80],   # Iyi tempo
        [14.0, 178, 0.85],   # Hizli kos
        [15.0, 185, 0.90],   # Yuksek performans
        [9.5,  155, 0.68],
        [11.0, 165, 0.75],
        [13.0, 172, 0.82],
    ], dtype=np.float32)

    # Performans skorlari (0-100)
    y_train = np.array([42, 58, 68, 80, 90, 50, 63, 75], dtype=np.float32)

    return X_train, y_train


def create_and_export_tflite(output_path="analytics/models/running_model.tflite"):
    """
    Modeli egitir ve TFLite formatinda kaydeder.

    Parametreler:
        output_path (str): Cikti dosya yolu

    Donus degeri:
        bool: Basarili ise True
    """
    if not TF_AVAILABLE:
        print("TensorFlow bulunamadi. Kurulum: pip install tensorflow")
        return False

    X_train, y_train = prepare_training_data()

    # Model mimarisi: 3 giris -> 8 noron -> 4 noron -> 1 cikis
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(8, activation='relu', input_shape=(3,),
                              name="giris_katmani"),
        tf.keras.layers.Dense(4, activation='relu', name="gizli_katman"),
        tf.keras.layers.Dense(1, name="cikis_katmani")
    ])

    model.compile(optimizer='adam', loss='mse', metrics=['mae'])
    model.summary()

    print("\nModel egitiliyor...")
    model.fit(X_train, y_train, epochs=50, verbose=0)
    print("Egitim tamamlandi.")

    # TFLite donusumu — mobil cihazlar icin optimize edilmis format
    converter = tf.lite.TFLiteConverter.from_keras_model(model)
    tflite_model = converter.convert()

    import os
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "wb") as f:
        f.write(tflite_model)

    size_kb = os.path.getsize(output_path) / 1024
    print(f"\nModel kaydedildi: {output_path}")
    print(f"Model boyutu: {size_kb:.2f} KB")

    # Ornek tahmin testi
    interpreter = tf.lite.Interpreter(model_path=output_path)
    interpreter.allocate_tensors()
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    test_input = np.array([[12.0, 170, 0.80]], dtype=np.float32)
    interpreter.set_tensor(input_details[0]['index'], test_input)
    interpreter.invoke()
    output = interpreter.get_tensor(output_details[0]['index'])
    print(f"Ornek tahmin (hiz=12, kadans=170, nabiz_orani=0.80): {output[0][0]:.1f}/100")

    return True


if __name__ == "__main__":
    create_and_export_tflite()
