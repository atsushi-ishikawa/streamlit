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
# get material name
material_name = st.sidebar.text_input("Material name", placeholder="Material name")

# get activity value
activity = st.sidebar.number_input("Activity", value=0.0)

# register button
register = st.sidebar.button("Register")

# show title message
st.title("Spectrum Viewer")

# show current time
st.write("Current time: ", pd.Timestamp.now())

# show uploaded file
if uploaded_file:
    st.write("Uploaded file: ", uploaded_file.name)

# show current directory
st.write("Current directory: ", os.getcwd())

if register:
    df = pd.read_csv(uploaded_file, header=header)
    new_df = pd.DataFrame({"material": material_name, "filename": uploaded_file.name,
                           "y": [df[df.columns[1]].to_numpy()],
                           "activity": activity
                           })
    df_all = pd.concat([df_all, new_df])

    st.dataframe(df_all,
            column_config={
            "y": st.column_config.LineChartColumn("spectrum", width="large", y_min=0, y_max=100),
            "activity": st.column_config.NumberColumn("activity"),
            }
    )
