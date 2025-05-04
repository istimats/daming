# from flask import Flask, request, render_template, jsonify
# import joblib
# import pandas as pd

# app = Flask(__name__)
# model = joblib.load('fuel_model.pkl')

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/predict', methods=['POST'])
# def predict_form():
#     # Ambil data dari form
#     engine_size = float(request.form['engine_size'])
#     cylinders = int(request.form['cylinders'])
#     fuel_type = request.form['fuel_type']
#     transmission = request.form['transmission']
#     distance_km = float(request.form['distance'])

#     input_df = pd.DataFrame([{
#         'ENGINESIZE': engine_size,
#         'CYLINDERS': cylinders,
#         'FUELTYPE': fuel_type,
#         'TRANSMISSION': transmission
#     }])

#     predicted = model.predict(input_df)[0]
#     total_liters = (predicted / 100.0) * distance_km

#     return f"""
#     <h2>Hasil Prediksi Konsumsi BBM</h2>
#     <p><strong>Konsumsi per 100 km:</strong> {round(predicted, 2)} liter</p>
#     <p><strong>Jarak Tempuh:</strong> {round(distance_km, 2)} km</p>
#     <p><strong>Total Perkiraan BBM:</strong> {round(total_liters, 2)} liter</p>
#     <br><a href='/'>← Kembali</a>
#     """

# if __name__ == '__main__':
#     app.run(debug=True)
