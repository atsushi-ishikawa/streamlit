import time
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder

st.title("Machine Learning app")

st.sidebar.markdown("### Upload csv file")
uploaded_file = st.sidebar.file_uploader("Choose a csv file")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    df_columns = df.columns
    
    st.markdown("### input data")
    # st.dataframe(df.style.highlight_max(axis=0))

    st.markdown("### plot")

    x = st.selectbox("x-axis", df_columns)
    y = st.selectbox("y-axis", df_columns)

    fig = plt.figure(figsize=(12, 8))
    plt.scatter(df[x], df[y])
    plt.xlabel(x, fontsize=16)
    plt.ylabel(y, fontsize=16)
    st.pyplot(fig)

    st.markdown("### pairplot")
    item = st.multiselect("columns to see", df_columns)
    hue = st.selectbox("item to color", df_columns)

    execute_pairplot = st.button("Draw pair plot")

    if execute_pairplot:
        df_sns = df[item]
        df_sns["hue"] = df[hue]

        fig = sns.pairplot(df_sns, hue="hue")
        st.pyplot(fig)

    st.markdown("### modeling")
    ex = st.multiselect("Choose descriptors", df_columns)
    ob = st.selectbox("Choose target variable", df_columns)

    st.markdown("#### Do ML")
    execute = st.button("Do")

    lr = linear_model.LinearRegression()

    if execute:
        df_ex = df[ex]
        df_ob = df[ob]
        X_train, X_test, y_train, y_test = train_test_split(df_ex.values, df_ob.values, test_size=0.2)
        lr.fit(X_train, y_train)

        my_bar = st.progress(0)
        for percent_complete in range(100):
            time.sleep(0.02)
            my_bar.progress(percent_complete + 1)

        col1, col2 = st.columns(2)
        col1.metric(label="Training score", value=lr.score(X_train, y_train))
        col2.metric(label="Test score", value=lr.score(X_test, y_test))

    # write
    df.to_csv("new.csv")
