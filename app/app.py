import streamlit as st
import requests as rs

sepal_length = st.text_input("Sepal Length")
sepal_width = st.text_input("Sepal Width")
petal_length = st.text_input("Petal Length")
petal_width = st.text_input("Petal Width ")


def get_api(params):
    url = f"http://api:8086/predict/"
    response = rs.get(url, params=params)
    return response.content


if st.button("Get response"):
    params = {
        "sepal_length": float(sepal_length),
        "sepal_width": float(sepal_width),
        "petal_length": float(petal_length),
        "petal_width": float(petal_width)
    }

    data = get_api(params)
    st.write(data)

