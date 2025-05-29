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
    win_count = int(request.form['jumlah_menang'])
    position = int(request.form['posisi_klasemen'])
    goals_conceded = int(request.form['kebobolan'])
    is_home = 1 if request.form['tempat_main'] == 'home' else 0

    features = np.array([[win_count, position, goals_conceded, is_home]])
    prob = model.predict_proba(features)[0][1]
    prob_percent = round(prob * 100, 2)

    return render_template('index.html', prediction=prob_percent)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)