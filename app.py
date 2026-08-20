import streamlit as st
from PIL import Image


st.title("Hola!, mi nombre es majo")
image = Image.open('ardillita.webp')
st.image(image, caption = 'holiwis')


