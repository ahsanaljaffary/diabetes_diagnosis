import pickle
import streamlit as st
import base64

diabetes_model = pickle.load(open('diabetes_model.sav','rb'))

st.set_page_config(
    page_title="Diagnosis Diabetes Ahsan",
    page_icon="👨‍⚕️",
    layout="wide"
)

with st.container():
    st.title("PRAKTEK STREAMLIT DIAGNOSIS PENYAKIT DIABETES")
    st.write("Halaman web ini dibuat untuk memenuhi tugas Mata Kuliah *Paket Aplikasi Data Mining*")
    st.caption("Dosen Pengampu : Muklisin, S.Kom")
    st.write("---")

st.title ('Data Mining Prediksi Diabetes')
st.write("*Harap diisi dengan data yang valid sesuai dengan keadaan yang dialami pasien*")
st.write("---")

col1, col2, = st.columns(2)
with col1:
    Pregnancies = st.text_input('Input Nilai Kehamilan')
with col1:
    BloodPressure = st.text_input('Input Nilai Tekanan Darah')
with col1:
    Insulin = st.text_input('Input Nilai Insulin')
with col1:
    DiabetesPedigreeFunction = st.text_input('Input Nilai Diabetes Pedigree Function')
with col2:
    Glucose = st.text_input('Input Nilai Glukosa')
with col2:
    SkinThickness = st.text_input('Input Nilai Ketebalan Kulit')
with col2:
    BMI = st.text_input('input nilain BMI/Indeks Massa Tubuh')
with col2:
    Age = st.text_input('Input Nilai Umur')

diab_diagnosis =''

if st.button('Test Prediksi Diabetes'):
    diab_prediction = diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])

    if(diab_prediction [0] == 1):
        diab_diagnosis = 'Pasien Terkena Diabetes, Segera Periksa ke Dokter !'
    else:
        diab_diagnosis = 'Pasien Tidak Terkena Diabetes'
    st.success(diab_diagnosis)