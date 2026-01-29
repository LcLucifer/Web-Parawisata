import streamlit as st
import pandas as pd

st.title("Hasil Scrapping Data Tempat Wisata di Indonesia")

#Membaca file excel
df = pd.read_excel("wisata_indonesia_clean.xlsx")
st.dataframe(df)
