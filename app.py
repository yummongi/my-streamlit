import streamlit as st

x = st.slider('Select a value')
st.write(x, 'sqaured is', x * x)
