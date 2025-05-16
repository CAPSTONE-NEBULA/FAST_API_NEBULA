# FAST_API_NEBULA

# 🌟 API Prediksi Kelayakan Bansos Siswa
Sebuah mini-proyek berbasis FastAPI yang dapat memprediksi kelayakan siswa menerima bantuan sosial (bansos) berdasarkan data keluarga dan siswa.

## 📁 Struktur File

├── main.py                # Endpoint API utama
├── dt_model.pkl           # File model Decision Tree yang telah dilatih
├── preprocessor.pkl       # File preprocessor (ColumnTransformer) yang telah dilatih
├── requirements.txt       # Daftar dependensi Python


## 🚀 Fitur API

- Prediksi kelayakan bansos (Layak/Tidak Layak) berdasarkan 26 fitur utama
- Menerima input melalui metode POST
- Hasil prediksi berupa label (0/1) dan status ("Layak"/"Tidak Layak")
- Ringan, cepat, dan siap diintegrasikan ke aplikasi lain

## ⚙ Cara Menjalankan

### 1. Clone Repositori

git clone <https://github.com/CAPSTONE-NEBULA/FAST_API_NEBULA/edit/main/README.md>
cd <FAST_API_NEBULA>


### 2. Buat Virtual Environment
python -m venv venv
venv\Scripts\activate
venv\Scripts\Activate.ps1
source venv/bin/activate


### 3. Install Dependensi

bash
pip install -r requirements.txt


### 4. Jalankan API

bash
fastapi dev main.py


### 5. Akses Swagger UI

Buka browser ke:  
👉 {http://127.0.0.1:8000]
(http://127.0.0.1:8000/docs) 

## 🧪 JSON Input

{
  "JK": 1,
  "RT": 2,
  "RW": 3,
  "Kelurahan": 4,
  "Kecamatan": 5,
  "Kode Pos": 12345,
  "Jenis Tinggal": 1,
  "Alat Transportasi": 2,
  "Penerima KPS": 0,
  "Data Ayah - Tahun Lahir": 1970,
  "Data Ayah - Jenjang Pendidikan": 4,
  "Data Ayah - Pekerjaan": 2,
  "Data Ayah - Penghasilan": 4000000,
  "Data Ibu - Tahun Lahir": 1975,
  "Data Ibu - Jenjang Pendidikan": 4,
  "Data Ibu - Pekerjaan": 2,
  "Data Ibu - Penghasilan": 3000000,
  "Anak ke-berapa": 2,
  "Berat Badan": 45.5,
  "Tinggi Badan": 150.0,
  "Jml. Saudara\r\nKandung": 1,
  "Jarak Rumah\r\nke Sekolah (KM)": 2.5,
  "Total Penghasilan": 7000000,
  "Agama_Islam": 1,
  "Agama_Katholik": 0,
  "Agama_Kristen": 0
}

## ✅ Output

{
  "prediction": 1,
  "status": "Layak"
}
