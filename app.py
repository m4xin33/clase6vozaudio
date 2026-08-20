import streamlit as st
from PIL import Image


st.title("Hola!, mi nombre es majo")
image = Image.open('ardillita.webp')
st.image(image, caption = 'holiwis')

texto = st.text_input('Buenisisimos dias' , 'a todos')
st.write('El texto escrito es' , texto)


