import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images\pfp.jpg")

with col2:
    st.title("Konstantinos Zygouris")
    content = """
    Hello, I'm Konstantinos Zygouris and I am from Greece! I am currently learning how to code in python
    so i will be ready to start attending a computer science course in the Netherlands at the University of Twente
    by September 2023.I enjoy many different things such as extreme sports, driving, programming, and gaming.
    """
    st.info(content)

content2 = """
Below you can find some of the apps I have built in Python.Feel free to contact me!
"""
st.write(content2)

col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=';')

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
