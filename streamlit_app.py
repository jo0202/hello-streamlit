import streamlit as st

x= st.slider('Seclect a value')
st.write(x, 'is a squared ', x*x)
st.title("this is the app title")
st.header("this is the markdown")
st.subheader("this is the subheader")
st.caption("this is the caption")
st.code("x=2021")
st.latex(r'''
a + a r ^1+ a r^2 + a r^3 ''')
st.checkbox('yes')
st.button('Click')
st.radio('Pick your gender',['Male','Female'])
st.selectbox('Pick your gender',['Male','Female'])
st.multiselect('choose a planet',['Jupiter','Mars','neptune'])
st.slider('Pick a number',0,50)