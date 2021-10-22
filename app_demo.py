import streamlit as st
import streamlit_pages.streamlit_pages import MultiPage

def home():
    st.write("Welcome to home page")
    if st.button("Click Home"):
        st.write("Welcome to home page")


def about():
:wq    st.write("Welcome to about page")
    if st.button("Click about"):
        st.write("Welcome to About page")


def contact():
    st.write("Welcome to contact page")
    if st.button("Click Contact"):
        st.write("Welcome to contact page")


# call app class object
app = MultiPage()
# Add pages
app.add_page("Home",home)
app.add_page("About",about)
app.add_page("Contact",contact)
app.run()
