import streamlit as st

x= st.slider('Seclect a value')
st.write(x, 'is a squared ', x*x)