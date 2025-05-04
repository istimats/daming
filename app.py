# app.py

from flask import Flask, request, render_template
import pandas as pd
import joblib

app = Flask(__name__)

# Load model yang sudah dilatih dan disimpan
model = joblib.load('fuel_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])


def predict():
    # Ambil input dari form HTML
    engine_size = float(request.form['engine_size'])
    cylinders = int(request.form['cylinders'])
    fuel_type = request.form['fuel_type']
    transmission = request.form['transmission']
    distance = float(request.form['distance'])

    # Buat DataFrame untuk prediksi
    input_df = pd.DataFrame([{
        'ENGINESIZE': engine_size,
        'CYLINDERS': cylinders,
        'FUELTYPE': fuel_type,
        'TRANSMISSION': transmission
    }])

    # Prediksi konsumsi BBM per 100 km
    pred_per_100km = model.predict(input_df)[0]

    # Hitung total BBM untuk jarak tertentu
    total_fuel = (pred_per_100km / 100.0) * distance

    return f"""
    <h2>Hasil Prediksi</h2>
    <p>Konsumsi per 100km: {round(pred_per_100km, 2)} liter</p>
    <p>Jarak: {distance} km</p>
    <p>Total estimasi BBM: {round(total_fuel, 2)} liter</p>
    <br><a href='/'>← Kembali</a>
    """

if __name__ == '__main__':
    app.run(debug=True)
