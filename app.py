import pandas as pd
import streamlit as st
API_URL = "https://data.paris2024.org/api/explore/v2.1/catalog/exports/csv?delimiter=%3B&lang=fr"
data = pd.read_csv(API_URL, sep=";")
data.columns = [col.replace("default.", "") for col in data.columns]
st.title("My first App")
st.bar_chart(data, x="title", y="records_count")