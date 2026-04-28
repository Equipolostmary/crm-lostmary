import streamlit as st
from services.google_sheets import get_all_sheets
from services.data_processor import unify_data

SPREADSHEET_URL = "https://docs.google.com/spreadsheets/d/1EkUx27lMVtO7S88uuyYtzmjxBBiKyVNc1dXY-nUwpVM"

st.set_page_config(page_title="CRM Lost Mary", layout="wide")

st.title("🚀 CRM Lost Mary")

if st.button("🔄 Cargar datos"):
    all_sheets = get_all_sheets(SPREADSHEET_URL)
    unified = unify_data(all_sheets)

    st.success("Datos cargados correctamente")

    for sheet, df in all_sheets.items():
        st.subheader(f"📄 {sheet}")
        st.dataframe(df)
