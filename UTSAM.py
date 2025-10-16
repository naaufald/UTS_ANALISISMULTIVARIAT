import streamlit as st
from PIL import Image
import requests
from io import BytesIO

st.set_page_config(page_title="UTS Analisis Multivariat", layout="wide")

st.markdown("""
<style>
img {
    max-width: 250px !important;
    height: auto;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

# Buat dua kolom: kiri (gambar), kanan (teks)
col1, col2 = st.columns([1, 2])

with col1:
    st.image("https://raw.githubusercontent.com/naaufald/UTS_ANALISISMULTIVARIAT/main/logo.png")

with col2:
    st.title("UTS Analisis Multivariat")
    st.write("Menampilkan hasil analisis **Correspondence Analysis (CA)** dengan kode R dan outputnya.")
    st.write("Nama : Naufal Fadhlullah (20234920001)")
    st.write("Prodi : Statistika")
    st.write("Mata Kuliah : Analisis Multivariat")

st.markdown("---")

st.header("Teori")
st.write("- Correspondence Analysis")
st.markdown("menurut Greenacre (1984) pada Ekawati et al. (2015), analisis korespondensi merupakan teknik mendemonstrasikan baris serta kolom" \
"dari sebuah tabel kontingensi dua arah yang digunakan sebagai titik ruang vektor dimensi rendah.")
st.markdown(" Menurut Denandra (2025), analisis korespondensi merupakan teknik multivariat yang digunakan dalam pengeksplorasian dam mempelajari hubungan peubah kualitatif dengan mereduksi dimensi dan memetakannya ke dalam dua dimensi.")
st.write("- Tujuan")
st.markdown("Analisis korespondensi bertujuan untuk mendeteksi dan memberikan deskriptif mengenai hubungan antara dua variabel pada data yang berbentuk matriks dengan dimensi besar. analisis ini dapat digunakan dalam mencari pengelompokan yang homogen suatu individu.")
st.write("- 3 langkah kunci melakukan CA di R")
st.markdown("1. melakukan pembuatan tabel kontingensi, atau input data")
st.markdown("2. menjalankan analisis correspondence menggunakan library ca atau FactoMineR")
st.markdown("3. menampilkan hasil dan melakukan interpretasi untuk melihat hubungan")

st.header("Implementasi R")
st.title("table 1")
st.code("""tabel1 <- matrix(c(40,30,20,
                   25,35,30,
                   30,15,10,
                   20,25,25),
                 nrow = 4, byrow = TRUE)

colnames(tabel1) <- c("Muda(18-25)", "Dewasa(26-40)", "Tua(>40)")
rownames(tabel1) <- c("Moisturizer", "Sunscreen", "Serum", "Cleanser")

tabel1""", language='r')
st.image("https://raw.githubusercontent.com/naaufald/UTS_ANALISISMULTIVARIAT/main/tabel 1.png", caption="tabel 1", use_container_width=True)

st.title("Data : dataset yang digunakan merupakan data dari bps yang merupakan jumlah desa yang memiliki fasilitas sekolah menurut provinsi dan tingkat pendidikan.")
st.image("https://raw.githubusercontent.com/naaufald/METNUM/main/datanyaa.png", caption = "Sumber Data: https://www.kaggle.com/datasets/greegtitan/indonesia-climate?select=climate_data.csv")
