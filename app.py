import streamlit as st
from PIL import Image


st.title("Hola!, mi nombre es majo")
image = Image.open('ardillita.webp')
st.image(image, caption = 'holiwis')

texto = st.text_input('Buenisisimos dias' , 'a todos')
st.write('pendejos' , texto)

st.subheader("Ahora usaremos dos columnas")

col1, col2 = st.columns(2)

with col1:
  st.subheader("Esta es mi primera columna")
  st.write("Las interfaces multimodales mejoran la experiencia de usuario")
  resp = st.checkbox('Estoy deacuerdo')
  if resp:
    st.write('correcto!')

with col2:
  st.subheader("Esta es la segunda colunma")
  modo = st.radio("Que modalidad es la principal en tu interfaz?") ('Visual', 'auditiva', 'Tactil'))
  if modo == 'Visual':
    st.write('La vista es fundamental para tu interfaz')
  if modo == 'auditiva':
    st.write('La audicion es fundamental para tu interfaz')
  if modo == 'Tactil':
    st.write('El texto es fundamental para tu intefaz')






    
  
  
