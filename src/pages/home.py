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
        Page("pages/home.py", "Home", "🏠")
    ]
)

st.write("# Bienvenue sur ClauseBenef! 👋")

st.markdown(
    """
    ClauseBenef est une IA vous permettant d'automatiser l'analyse et le processus de validation de vos clauses bénéficiaires.
    En seulement quelques clicks, faites analyser des milliers de clauses bénéficiaires.

    ### Fonctionnalités
    - Définissez vos règles de validation et soumettez les
    - Ajoutez l'ensemble des vos clauses au format de votre choix
    - Choisisez d'anonymiser ou non vos données (remplacer les PII avec des données fausses)
    - Laissez l'IA faire le travail d'analyse
"""
)