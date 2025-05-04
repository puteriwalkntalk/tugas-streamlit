import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import requests
import PyPDF2 as pdf
from PyPDF2 import PdfReader
from PIL import Image
# menambahkan judul
st.title("Aplikasi Dasar dengan Streamlit")
st.title("Welcome to my streamlit app uci")
st.text('''Perkenalkan nama saya Putri Amelia ''')
st.header("pendahuluan tentang aplikasi ini")
st.subheader("bagian pertama : pengunaan element text")
st.caption("saya mahasiswi universitas negeri makassar")
st.code('import numpy as np, pandas as pd, ploty.express as px, streamlit as st, requests')
st.latex(r'F = G (m₁.m₂)/r²')
st.markdown('contoh pengaturan tesk: **teks tebal** dan _teks miring_ serta [link](https://youtu.be/hErTL9lLeq8?si=6onK0dDDtaq1Rfx)')
uploaded_file = st.file_uploader("silahkan pilih file", type="csv" )

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.dataframe(data)

# Menambahkan penjelasan 
st.write("ini adalah aplikasi pertama yang menggunakan streamlit")

data = {
    'Nama': ['Uto', 'uci', 'elma', 'akram', 'yaya'],
    'Usia': [16, 17, 18, 19, 20],
    'Kota': ['Maluku', 'Toraja', 'Maros', 'Sudiang', 'Bau bau'],

}
df = pd.DataFrame(data)
st.write(df)
np.random.randn(50, 3),
df = pd.DataFrame(
    np.random.randn(50, 3),
    columns=['a', 'b', 'c']
    )  

df = pd.DataFrame(data)
st.write('Tabel data aku')
st.dataframe(df)

df = pd.DataFrame(
    np.random.randn(50, 3),
    columns=['a', 'b', 'c']
    )  

st.write(df)

#matric

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Harga beli", value="Rp 7.000", delta="+3%")
with col2:
    st.metric(label="Volume Transaksi", value="1,6 Juta", delta="+20%")
with col3:
    st.metric(label="Perobahan Harga", value="-50", delta="-5%")

col1, col2 = st.columns(2)


df = pd.DataFrame(
    np.random.randn(40, 5),
    columns=['x', 'y', 'z', 'a', 'b']
    )  
st.line_chart(df)

df = pd.DataFrame(
    np.random.randn(40, 5),
    columns=['a', 'b', 'c', 'd', 'e']
    )  
st.area_chart(df)

df = pd.DataFrame(
    np.random.randn(40, 5),
    columns=['a', 'b', 'c', 'd', 'e']
    )  
st.bar_chart(df)


data = pd.DataFrame({
    'lat': [-5.1357, -5.1375, -5.1472, -5.1411, -5.1398],
    'lon': [119.4124, 119.4189, 119.4281, 119.4240, 119.4195]
})
st.map(data)





# Judul dashboard
st.title("📊 Dashboard Penjualan 5 Tahun")
st.caption("Dibuat oleh: **Putri Amelia**")

# Data penjualan dan laba
data = pd.DataFrame({
    'Tahun': [2018, 2019, 2020, 2021, 2022],
    'Penjualan': [100, 120, 90, 140, 180],
    'Laba': [20, 30, 15, 35, 50]
})

# Grafik garis - Tren Penjualan
fig_penjualan = px.line(
    data,
    x='Tahun',
    y='Penjualan',
    markers=True,
    text='Penjualan',
    title="📈 Tren Penjualan Tiap Tahun",
    labels={'Penjualan': 'Jumlah Penjualan', 'Tahun': 'Tahun'},
    template='plotly_white'
)
fig_penjualan.update_traces(textposition="top center")
fig_penjualan.update_layout(title_x=0.5)

# Grafik batang - Laba Tahunan
fig_laba = px.bar(
    data,
    x='Tahun',
    y='Laba',
    color='Tahun',
    title="💰 Laba Tahunan",
    labels={'Laba': 'Jumlah Laba'},
    template='plotly_dark'
)
fig_laba.update_layout(title_x=0.5)

# Tampilkan dalam 2 kolom
col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(fig_penjualan, use_container_width=True)
with col2:
    st.plotly_chart(fig_laba, use_container_width=True)

# Divider dan Footer
st.divider()
st.caption("Dibuat dengan ❤️ oleh **Putri Amelia** menggunakan Streamlit dan Plotly.")



import streamlit as st

with st.form("form_input"):
    nama = st.text_input("Nama Lengkap")
    alamat = st.text_area("Alamat Lengkap")
    usia = st.number_input("Usia (tahun)", min_value=0)
    tanggal_lahir = st.date_input("Tanggal Lahir")
    waktu_janjian = st.time_input("Waktu Janjian")
    jenis_kelamin = st.radio("Jenis Kelamin", ("Pria", "Wanita", "Lainnya"))
    hobi = st.multiselect("Hobi", ["Membaca", "Bersepeda", "Musik", "Memasak"])
    warna_favorit = st.color_picker("Pilih Warna Favorit")
    foto_potret = st.file_uploader("Upload Foto Profil")
    rating = st.slider("Rating Kepuasan", 1, 10)
    submitted = st.form_submit_button("Kirim Data")

if submitted:
    st.success(f"Data {nama} berhasil dikirim!")


image = Image.open("putri.jpg")
st.image(image, caption='foto saya')

st.image("https://blog.tripcetera.com/id/wp-content/uploads/2019/07/bunga-edelweis.jpg", caption='gambar bungan edelwies', use_column_width=True)

##dari dari file lokal
st.video("vidioputerik.mp4")
#menampilkan vidio dari url
st.video("https://youtu.be/txOWhzgrZpM?si=Pf6Xj-_I-q-6QrdM")

##menampilkan sound dari file lokal
st.audio("artic monkeys - 505.mp3")
#menampilak vidio dari url
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")

uploaded_file = st.file_uploader("silahkan pilih file PDF or Excel", type=["pdf", "xlsx"])

if uploaded_file is not None:
    st.write("file berhasil di upload")
    st.write(uploaded_file.name)
    st.download_button("download", uploaded_file)   
    

# Menampilkan PDF
uploaded_pdf = st.file_uploader("Pilih file PDF", type=["pdf"])

if uploaded_pdf is not None:
    reader = PdfReader(uploaded_pdf)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    st.write(text)


# Menampilkan HTML langsung
html_code = """
<h3> saya adalah seorang mahasiswa</h3>
<p>saya sedang belajar streamlit</p>
"""
st.markdown(html_code, unsafe_allow_html=True)

# Membuat dua kolom
kol1, kol2 = st.columns(2)

# Menampilkan konten di kolom pertama
with kol1:
    st.header("Kolom Pertama")
    st.write("Ini adalah isi di kolom pertama.")
    st.button("Tombol di Kolom Pertama")

# Menampilkan konten di kolom kedua
with kol2:
    st.header("Kolom Kedua")
    st.write("Ini adalah isi di kolom kedua.")
    st.button("Tombol di Kolom Kedua")

with st.expander("Klik untuk melihat lebih banyak"):
    st.write("Ini adalah konten tersembunyi yang bisa dilihat saat pengguna klik expander.")
    st.image("https://th.bing.com/th/id/OIP.d-QOwW_6YgNwuvgZPHBceAHaE8?cb=iwc1&rs=1&pid=ImgDetMain", caption="Gambar bunga desy")


container = st.container()

# Menambahkan elemen ke dalam container
with container:
    st.header("Konten di dalam Container")
    st.write("Ini adalah elemen-elemen yang ada dalam container.")
    st.button("Tombol dalam Container")




# Menambahkan elemen navigasi di Sidebar
st.sidebar.header("Navigasi")
selection = st.sidebar.radio("Pilih Halaman", ["Beranda", "Tentang", "Kontak"])

# Konten berdasarkan pilihan
if selection == "Beranda":
    st.title("Beranda")
    st.write("Ini adalah halaman beranda.")
elif selection == "Tentang":
    st.title("Tentang")
    st.write("Ini adalah halaman tentang.")
else:
    st.title("Kontak")
    st.write("Ini adalah halaman kontak.")

# Menambahkan elemen navigasi dengan dropdown di Sidebar
st.sidebar.header("Navigasi")
selection = st.sidebar.selectbox("Pilih Halaman", ["Beranda", "Tentang", "Galeri", "Kontak"])

# Konten berdasarkan pilihan
if selection == "Beranda":
    st.title("Beranda")
    st.write("Ini adalah halaman beranda.")
elif selection == "Tentang":
    st.title("Tentang")
    st.write("Ini adalah halaman tentang.")
elif selection == "Galeri":
    st.title("Galeri")
    st.write("Ini adalah halaman galeri.")
else:
    st.title("Kontak")
    st.write("Ini adalah halaman kontak.")

# Menambahkan tombol untuk navigasi di Sidebar
st.sidebar.header("Navigasi")
if st.sidebar.button("Beranda"):
    st.title("Beranda")
    st.write("Ini adalah halaman beranda.")
elif st.sidebar.button("Tentang"):
    st.title("Tentang")
    st.write("Ini adalah halaman tentang.")
elif st.sidebar.button("Kontak"):
    st.title("Kontak")
    st.write("Ini adalah halaman kontak.")

# Menambahkan tautan navigasi di Sidebar
st.sidebar.header("Navigasi")
st.sidebar.markdown("[Beranda](#beranda)")
st.sidebar.markdown("[Tentang](#tentang)")
st.sidebar.markdown("[Kontak](#kontak)")

# Konten halaman berdasarkan tautan
st.title("Beranda")
st.write("Ini adalah halaman beranda.")

st.title("Tentang")
st.write("Ini adalah halaman tentang.")

st.title("Kontak")
st.write("Ini adalah halaman kontak.")