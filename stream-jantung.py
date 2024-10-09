import pickle
import numpy as np
import streamlit as st

# Load saved model
model = pickle.load(open('penyakit_jantung.sav', 'rb'))

# Judul web
st.title('Prediksi Penyakit Jantung')

col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input('Umur', min_value=0)  # Menggunakan number_input untuk input numerik
with col2:
    sex = st.selectbox('Jenis Kelamin', options=[0, 1])  # Menggunakan selectbox untuk pilihan biner
with col3:
    cp = st.selectbox('Jenis Nyeri Dada', options=[0, 1, 2, 3])  # Asumsi nilai dari 0-3
with col1:
    trestbps = st.number_input('Tekanan Darah', min_value=0)
with col2:
    chol = st.number_input('Nilai Kolesterol', min_value=0)
with col3:
    fbs = st.selectbox('Gula Darah', options=[0, 1])  # Asumsi biner
with col1:
    restecg = st.selectbox('Hasil Elektrokardiografi', options=[0, 1, 2])  # Asumsi nilai dari 0-2
with col2:
    thalach = st.number_input('Detak Jantung Maksimum', min_value=0)
with col3:
    exang = st.selectbox('Induksi Angina', options=[0, 1])  # Asumsi biner
with col1:
    oldpeak = st.number_input('ST Depression', format="%.1f")  # Input numerik dengan format desimal
with col2:
    slope = st.selectbox('Slope', options=[0, 1, 2])  # Asumsi nilai dari 0-2
with col3:
    ca = st.selectbox('Nilai CA', options=[0, 1, 2, 3])  # Asumsi bahwa nilai dari 0-3
with col1:
    thal = st.selectbox('Nilai Thal', options=[0, 1, 2])  # Asumsi nilai dari 0-2

# Kode untuk prediksi
heart_diagnosis = ''

# Membuat tombol prediksi
if st.button('Prediksi Penyakit Jantung'):
    # Mengonversi input ke dalam format yang tepat
    heart_prediction = model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

    if heart_prediction[0] == 1:
        heart_diagnosis = 'Pasien Terkena Penyakit Jantung'
    else:
        heart_diagnosis = 'Pasien Tidak Terkena Penyakit Jantung'

st.success(heart_diagnosis)
