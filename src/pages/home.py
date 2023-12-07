import streamlit as st
from st_pages import Page, Section, show_pages, add_page_title


st.set_page_config(
        page_title="Cawoylel Windanam",
        page_icon="❄️",
        layout="wide"
    )

add_page_title() # By default this also adds indentation

# Specify what pages should be shown in the sidebar, and what their titles and icons
# should be
show_pages(
    [
        Page("src/pages/home.py", "About", "🏠"),
        Page("src/pages/speech_recognition.py", "Speech Recognition", "🗣️"),
        # Page("src/pages/translatation.py", "Translation", "🌐"),
    ]
)


st.write("# 🇺🇸 Welcome to Cawoylel-Demo ! 👋")

st.markdown(
    """
    Cawoylel is a non-profit initiative dedicated to the development of technological and digital tools for the Fula language. 
    Its goal is to address the challenges posed by the modern digital and technological revolution for African languages.

    On this page, you'll find demos of all the technologies that have been developed for the Fula language. We invite you to try them out and provide us your feedback.
    
    This project aims to be participatory. Individuals from diverse backgrounds, regardless of their expertise, are welcomed to actively contribute and shape meaningful solutions. 
    Whether you are a language speaker, an engineer, a linguist, a sociologist, or have any other expertise, you are invited to join Cawoylel and be a part of its journey.

"""
)