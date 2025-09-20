import streamlit as st
import pwa

pwa.set_pwa_config()

st.set_page_config(
    page_title="Hello PWA",
    page_icon="static/icon.png"
)

st.title("Home Page")
st.sidebar.error("Select a page above")

st.write("Welcome to my first PWA!")