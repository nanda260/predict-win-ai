## Prediksi Kemenangan Laga Tim Sepakbola
Program ini bisa menghitung presentase kemenangan dari tim sepakbola yang akan berlaga, 
program ini menggunakan algoritma Support Vector Machine (SVM) untuk menghitung prediksinya. 
Yang dimana SVM dilatih dengan dataset dengan nama file data.csv dan akan mengenali data baru yang dimasukkan oleh pengguna dengan melakukan klasifikasi, setelah diketahui antara 0-1, nantinya dikoncersi ke presentase untuk tampilan prediksi yang lebih jelas.


![image](https://github.com/user-attachments/assets/f018c3df-f76f-4078-9416-025d70e30d74)



Adapun masukkan yang harus diisi pengguna antara lain:

1. Jumlah kemenangan di 5 laga terakhir,
2. Posisi di klasemen liga,
3. Selisih gol pada liga, dan
4. Bermain di kandang atau tandang.
   
Tools yang digunakan adalah pemrograman html, css, bahasa python sebagai backend dan pemrosesan teknik AI Learning (SVM).


### Link Demo Website
[Menuju Website](https://predict-match.up.railway.app/)

## Cara Instalasi

### 1. Clone Repository

```bash
git clone https://github.com/nanda260/predict-win-ai.git
cd predict-win-ai
```

### 2. Buat dan Aktifkan Virtual Environment (Opsional tapi disarankan)

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Jalankan Aplikasi

```bash
python app.py
```

### 5. Akses di Browser

Buka browser dan akses:
```
http://127.0.0.1:5000/
```



Dibuat oleh:

Romadhoni Kusuma Nanda Prihadi
23050974063 - PTI 2023B
