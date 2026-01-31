import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

st.title("Peta Pariwisata Indonesia")

# Baca data
file_path = "wisata_indonesia_clean.xlsx"
df = pd.read_excel(file_path)

# Sidebar untuk filter
st.sidebar.header("Filter Kategori")

# Ambil kategori unik
kategori_unik = df["kategori"].unique()

# Checkbox untuk semua kategori
select_all = st.sidebar.checkbox("Pilih Semua Kategori", value=True)

# Buat checkbox untuk setiap kategori
selected_categories = []

if select_all:
    selected_categories = list(kategori_unik)
else:
    for kategori in kategori_unik:
        if st.sidebar.checkbox(kategori, value=True):
            selected_categories.append(kategori)

# Filter data berdasarkan kategori yang dipilih
filtered_df = df[df["kategori"].isin(selected_categories)]

# Informasi jumlah data
st.sidebar.info(f"Menampilkan {len(filtered_df)} dari {len(df)} lokasi wisata")

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

# Buat peta dengan lokasi rata-rata berdasarkan data yang difilter
if len(filtered_df) > 0:
    avg_lat = filtered_df["latitude"].mean()
    avg_lon = filtered_df["longitude"].mean()
    peta = folium.Map(location=[avg_lat, avg_lon], zoom_start=5)
    
    # Tambahkan marker hanya untuk data yang difilter
    for i, row in filtered_df.iterrows():
        kategori = row["kategori"]
        warna = warna_kategori[kategori]
        
        popup_content = f"""
        <b>{row['nama_wisata']}</b><br>
        Kategori: {kategori}<br>
        Lokasi: {row['latitude']:.4f}, {row['longitude']:.4f}
        """
        
        folium.Marker(
            location=[row["latitude"], row["longitude"]],
            popup=folium.Popup(popup_content, max_width=300),
            tooltip=row["nama_wisata"],
            icon=folium.Icon(color=warna)
        ).add_to(peta)
    
    # Tampilkan peta
    st_folium(peta, width=900, height=500)
    
    # Tampilkan tabel data
    st.subheader("Data Wisata yang Ditampilkan")
    st.dataframe(filtered_df[['nama_wisata', 'kategori', 'latitude', 'longitude']])
else:
    st.warning("Tidak ada data yang ditampilkan. Silakan pilih setidaknya satu kategori.")

# Informasi tentang filter
st.sidebar.subheader("Legenda Warna")
for kategori, warna in warna_kategori.items():
    if kategori in selected_categories:
        st.sidebar.markdown(f"<span style='color:{warna}'>■</span> {kategori}", unsafe_allow_html=True)
