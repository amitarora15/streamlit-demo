import streamlit as st

st.sidebar.header("Navigation")

pages=['A','B','C']
page=st.sidebar.radio('Navigation',pages)

if page=='A':
   st.write('A selcted')
elif page=='B':
   st.write('B selected')
else:
   st.write('C')

st.sidebar.header("Contributor")
st.sidebar.write('Amit')

