import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

st.title("Peta Pariwisata Indonesia")

# Baca data
file_path = "wisata_indonesia_clean.xlsx"
df = pd.read_excel(file_path)

# Ambil kategori unik
kategori_unik = df["kategori"].unique()

# Daftar warna Folium
daftar_warna = [
    "red", "blue", "green", "purple", "orange",
    "darkred", "cadetblue", "darkgreen",
    "darkblue", "pink", "lightred"
]

# Mapping kategori ke warna
warna_kategori = {
    kategori: daftar_warna[i % len(daftar_warna)]
    for i, kategori in enumerate(kategori_unik)
}

# Buat peta
peta = folium.Map(location=[-2.5, 118], zoom_start=5)

# Tambahkan marker
for i, row in df.iterrows():
    kategori = row["kategori"]
    warna = warna_kategori[kategori]

    folium.Marker(
        location=[row["latitude"], row["longitude"]],
        popup=row["nama_wisata"] + " | " + kategori,
        icon=folium.Icon(color=warna)
    ).add_to(peta)

# Simpan peta
peta.save("gis_kategori.html")
st_folium(peta, width=900, height=500)