from flask import Flask, render_template, request
import joblib
import numpy as np
import os

app = Flask(__name__)
model = joblib.load('model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Tim A
    a_win = int(request.form['a_jumlah_menang'])
    a_pos = int(request.form['a_posisi_klasemen'])
    a_selisih_gol = int(request.form['a_selisih_gol'])
    a_home = 1 if request.form['a_tempat_main'] == 'home' else 0

    # Tim B
    b_win = int(request.form['b_jumlah_menang'])
    b_pos = int(request.form['b_posisi_klasemen'])
    b_selisih_gol = int(request.form['b_selisih_gol'])
    b_home = 1 if request.form['b_tempat_main'] == 'home' else 0

    # Prediksi
    features_a = np.array([[a_win, a_pos, a_selisih_gol, a_home]])
    features_b = np.array([[b_win, b_pos, b_selisih_gol, b_home]])


    raw_prob_a = model.predict_proba(features_a)[0][1]
    raw_prob_b = model.predict_proba(features_b)[0][1]

    #Hitung probabilitas
    total = raw_prob_a + raw_prob_b
    norm_prob_a = round((raw_prob_a / total) * 100, 2)
    norm_prob_b = round((raw_prob_b / total) * 100, 2)

    return render_template('index.html', prediction_a=norm_prob_a, prediction_b=norm_prob_b)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
