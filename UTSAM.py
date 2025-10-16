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
kode_r = """
```r
tabel1 <- matrix(c(40,30,20,
                   25,35,30,
                   30,15,10,
                   20,25,25),
                 nrow = 4, byrow = TRUE)

colnames(tabel1) <- c("Muda(18-25)", "Dewasa(26-40)", "Tua(>40)")
rownames(tabel1) <- c("Moisturizer", "Sunscreen", "Serum", "Cleanser")

tabel1"""
st.markdown(kode_r)
st.image("https://raw.githubusercontent.com/naaufald/UTS_ANALISISMULTIVARIAT/main/tabel 1.png", caption="tabel 1", width = 1200)

st.title("table 2")
st.subheader("Data : dataset yang digunakan merupakan data dari bps yang merupakan jumlah desa yang memiliki fasilitas sekolah menurut provinsi dan tingkat pendidikan.")
st.image("https://raw.githubusercontent.com/naaufald/UTS_ANALISISMULTIVARIAT/main/datauts.png")
st.write("Sumber data: [Data BPS](https://www.bps.go.id/id/statistics-table/2/MjA1IzI=/jumlah-desa-yang-memiliki-fasilitas-sekolah-menurut-provinsi-dan-tingkat-pendidikan.html)")
kode_r = """
```r
data_utss <- read.csv("D:/Matana/Semester 5/ANALISIS MULTIVARIAT/UTS/jumlah desa.csv", sep = ";")
data_utss"""
st.markdown(kode_r)
st.image("https://raw.githubusercontent.com/naaufald/UTS_ANALISISMULTIVARIAT/main/tabel2.png")

st.title("Melakukan CA")
kode_r = """
```r
library(ca)
ca_tabel1 <- ca(table1)
summary(ca_tabel1)
"""
st.markdown(kode_r)
st.subheader("ringkasan :")
st.image("https://raw.githubusercontent.com/naaufald/UTS_ANALISISMULTIVARIAT/main/CAtab1.png")
st.write("pada dimensi 1, menjelaskan bahwa hampir seluruh variasi atau 97,8% antar kategori dalam kontingensi dapat dijelaskan pada satu dimensi utama. eigenvalue pada dimensi 1 menunjukkan adanya asosiasi yang dominan dengan total inersia mendekati 0 yang menandakan bahwa hubungan antar kategori ada tapi tidak kuat.")

st.subheader("plot dan interpretasi")
kode_r = """
```r
plot(ca_tabel1, main = "CA: Tipe Produk Skincare vs Kelompok Usia", 
     xlab = "Dimensi 1", ylab = "Dimensi 2")
abline(h=0, v=0, lty=2, col="gray")
"""
st.markdown(kode_r)
st.image("https://raw.githubusercontent.com/naaufald/UTS_ANALISISMULTIVARIAT/main/plot.png")
st.write("berdasarkan plot, diketahui bahwa kelompok muda (18-25) cenderung menggunakan serum dibandingkan dengan skincare lainnya, dewasa (26-40) cenderung memakai sunscreen, dan Tua (>40) cenderung memakai cleanser.")
st.markdown("produk serum dan moisturizer berada pada titik negatif yang lebih dekat atau terkait dengan usia muda (18-25). dan produk cleanser serta sunscreen berada di sisi kanan yang dikaitkan dengan usia kelompok dewasa dan tua.")
st.markdown("produk moisturizer tidak spesifik pada kelompok usia, bisa dibilang moisturizer berada pada posisi netral.")

st.title("CA Table 2")
kode_r = """
```r
rownames(data_utss) <- data_utss$Provinsi
data_ca <- data_utss[, -1]
library(ca)
ca_result <- ca(data_ca, graph = FALSE)
summary(ca_result)"""
st.markdown(kode_r)
st.image("https://raw.githubusercontent.com/naaufald/UTS_ANALISISMULTIVARIAT/main/CATable2.png")
st.write("nilai total inertia menunjukkan angka 0.0366 yang memberikan bukti bahwa asosiasi antar kategori dari provinsi dan jenjang pendidikan memiliki distribusi yang tidak terlalu besar.")
st.markdown("pada dimensi 1 menjelaskan 77,4% yang berarti sebagian besar variasi data menggambarkan perbedaan utama antar provinsi dan jenjang pendidikan. dimana, pada dimensi 2 hanya menambah sedikit informasi sebesar 13,1%. kedua dimensi menunjukkan 90.5% total variasi")

st.subheader("plot dan interpretasi")
kode_r = """
```r
fviz_ca_biplot(ca_result, repel = TRUE, 
               title = "Hasil Correspondence Analysis Tabel 2")
"""
st.markdown(kode_r)
st.image("https://raw.githubusercontent.com/naaufald/UTS_ANALISISMULTIVARIAT/main/plottab2.png")
st.write("- titik merah menunjukkan jenjang pendidikan, dan titik biru menunjukkan provinsi. sehingga titik biru yang berdekatan dengan titik merah menunjukkan asosiasi kuat.")
st.markdown("berdasarkan plot, diketahui bahwa jenjang perguruan tinggi berada di sisi kanan dengan provinsi terkait yang berada di sisi kanan, seperti DIY, DKI Jakarta, dan Jawa Barat. sehingga menunjukkan jumlah perguruan tinggi yang relatif lebih banyak.")
st.markdown("Pada jenjang SMK, provinsi yang berasosiasi kuat yaitu DIY dan Jawa Barat, menandakan bahwa kedua provinsi memiliki sekolah kejuruan yang relatif lebih banyak dibandingkan dengan provinsi lain.")
st.markdown("jenjang SD dan SMP, berada di sisi kiri, begitupun provinsi yang berasosiasi yaitu Sulawesi tengah, Kalimantan Utara, Papua, Papua Barat Daya, NTT, dll cenderung memiliki proporsi fasilitas pendidikan dasar (SD_SMP) yang lebih tinggi. namun masih terbatas pada jenjang SMU")
st.markdown("jenjang SMU berada pada posisi mendekati tengah bawah, menunjukkan adanya dominasi kuat pada provinsi tertentu")

st.title("Kesimpulan Bisnis")
st.write("berdasarkan hasil CA tabel 1, diketahui bahwa :")
st.write("- usia muda cenderung memakai produk skincare berupa moisturizer dan serum,")
st.write("- usia dewasa cenderung memakai produk skincare berupa sunscreen,")
st.write("- usia tua cenderung memakai produk skincare berupa cleanser")

st.write("berdasarkan hasil CA tabel 2, diketahui bahwa :")
st.write("- provinsi dengan kecenderungan jenjang perguruan tinggi DIY, DKI Jakarta, Jawa Barat,")
st.write("- provinsi dengan kecenderungan jenjang SMK yaitu DIY dan Jawa Barat,")
st.write("- provinsi dengan kecenderungan jenjang SD dan SMP yaitu Sulawesi tengah, Kalimantan Utara, Papua, Papua Barat Daya, NTT")

st.title("strategi Pemasaran")
st.write("- berdasarkan segmentasi usia muda, fokus promosi pada hydration care dengan sasaran target remaja dan dewasa muda,")
st.write("- berdasarkan segmentasi usia dewasa, dewasa, menekankan pentingnya anti-aging dan UV protection, promosikan sunscreen & serum dengan antioksidan,")
st.write("- berdasarkan segmen usia tua, Tonjolkan manfaat gentle cleanser & moisturizer untuk kulit sensitif dan anti-aging ringan.")
st.subheader("mengadakan bundling produk, seperti :")
st.write("- paket “Daily Starter” untuk usia muda (serum + moisturizer),")
st.write("- paket “Protection Set” untuk dewasa (sunscreen + moisturizer)")