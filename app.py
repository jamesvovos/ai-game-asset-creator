import streamlit as st
import pandas as pd
import numpy as np
import spacy
from spacy_streamlit import visualize_tokens, visualize_ner

# pip install spacy-streamlit
# pip install spacy
# python -m spacy download en_core_web_sm

# Web App UI
st.title("🎮AI NLP Research Project🎓")
st.header("About the project:")

st.text("Research Project by James Vovos.")

with st.expander("Contact Details:"):
    st.info("Email: james.vovos@gmail.com")
    st.info("Github: https://github.com/jamesvovos")