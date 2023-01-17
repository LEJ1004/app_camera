import streamlit as st

st.subheader('학생 사진 촬영')

col1, col2 = st.columns(2)

hakbun = col1.text_input('학번')
name = col2.text_input('성명')



