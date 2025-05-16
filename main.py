from fastapi import FastAPI
from pydantic import BaseModel, Field
import joblib
import pandas as pd

app = FastAPI(title="Decision Tree Prediction API")

# Load model dan preprocessor
model = joblib.load("dt_model.pkl")
preprocessor = joblib.load("preprocessor.pkl")

class InputData(BaseModel):
    JK: int
    RT: int
    RW: int
    Kelurahan: int
    Kecamatan: int
    Kode_Pos: int = Field(..., alias="Kode Pos")
    Jenis_Tinggal: int = Field(..., alias="Jenis Tinggal")
    Alat_Transportasi: int = Field(..., alias="Alat Transportasi")
    Penerima_KPS: int = Field(..., alias="Penerima KPS")
    Ayah_Tahun_Lahir: int = Field(..., alias="Data Ayah - Tahun Lahir")
    Ayah_Pendidikan: int = Field(..., alias="Data Ayah - Jenjang Pendidikan")
    Ayah_Pekerjaan: int = Field(..., alias="Data Ayah - Pekerjaan")
    Ayah_Penghasilan: float = Field(..., alias="Data Ayah - Penghasilan")
    Ibu_Tahun_Lahir: int = Field(..., alias="Data Ibu - Tahun Lahir")
    Ibu_Pendidikan: int = Field(..., alias="Data Ibu - Jenjang Pendidikan")
    Ibu_Pekerjaan: int = Field(..., alias="Data Ibu - Pekerjaan")
    Ibu_Penghasilan: float = Field(..., alias="Data Ibu - Penghasilan")
    Anak_ke: int = Field(..., alias="Anak ke-berapa")
    Berat_Badan: float = Field(..., alias="Berat Badan")
    Tinggi_Badan: float = Field(..., alias="Tinggi Badan")
    Jumlah_Saudara: int = Field(..., alias="Jml. Saudara\r\nKandung")
    Jarak_Rumah_Sekolah: float = Field(..., alias="Jarak Rumah\r\nke Sekolah (KM)")
    Total_Penghasilan: float = Field(..., alias="Total Penghasilan")
    Agama_Islam: int
    Agama_Katholik: int
    Agama_Kristen: int

@app.post("/predict")
def predict(data: InputData):
    try:
        input_dict = data.dict(by_alias=True)
        input_df = pd.DataFrame([input_dict])
        transformed = preprocessor.transform(input_df)
        prediction = model.predict(transformed)
        pred = 1 if prediction[0] == 1 else 0
        status = "Layak" if pred == 1 else "Tidak Layak"
        return {
            "prediction": pred,
            "status": status
        }
    except Exception as e:
        print("Error:", str(e))
        return {"error": str(e)}