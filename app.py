import streamlit as st

x = st.slider('Select a value')
st.write(x, 'sqaured is', x * x)

st.title("this is the app title")
st.header("this is the header")
st.markdown("this is the markdown")
st.subheader("this is the subheader")
st.caption("this is the caption")
st.code("x=2021")
st.latex(r''' a + a r ^1+ a r^2 + a r^3 ''')

st.sidebar.title("This is written inside the sidbar")
st.sidebar.button("Click")
