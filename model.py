import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import joblib

df = pd.read_csv('data.csv')
X = df[['jumlah_menang', 'posisi_klasemen', 'posisi_klasemen', 'tempat_main']]
y = df['result']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = SVC(kernel='linear', probability=True)
model.fit(X_train, y_train)

joblib.dump(model, 'model.pkl')
