import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images\pfp.jpg")

with col2:
    st.title("Konstantinos Zygouris")
    content = """
    Hello, I'm Konstantinos Zygouris and I am from Greece! Below is a selection of some of the apps i have built during the summer of 2023 with the help of a python course I took. I created these apps in preparation for beginning a Bachelor of Computer Science course in the Netherlands at the University of Twente, starting in September 2023.  I enjoy a variety of activities such as extreme sports, driving, programming, watching anime, movies, and gaming. Feel free to contact me!
    """
    st.info(content)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=';')

with col3:
    for index, row in df[:7].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row['image'])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[7:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row['image'])
        st.write(f"[Source Code]({row['url']})")
