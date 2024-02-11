import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.sidebar.markdown("### Upload csv file")

header = 1

if os.path.exists("all.pkl"):
    df_all = pd.read_pickle("all.pkl")
else:
    df_all = pd.DataFrame()

uploaded_file = st.sidebar.file_uploader("Choose a csv file")
material_name = st.sidebar.text_input("Material name", placeholder="Material name")
register = st.sidebar.button("Register")

if register:
    df = pd.read_csv(uploaded_file, header=header)
    new_df = pd.DataFrame({"material": material_name, "filename": uploaded_file.name, "y": [df[df.columns[1]].to_numpy()]})
    df_all = pd.concat([df_all, new_df])

    st.dataframe(df_all, column_config={"y": st.column_config.LineChartColumn("spectrum", width="large", y_min=0, y_max=100)})

    df_all.to_pickle("all.pkl")

