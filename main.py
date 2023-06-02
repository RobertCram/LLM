import os
import datetime
import streamlit as st

from dotenv import load_dotenv
load_dotenv()

from langchain.llms import OpenAI

@st.cache_resource
def load_model():
  return OpenAI(temperature=0.5)

llm = load_model()

"""
# LLM example
Leer de bijzonderheden van je voornaam en geboortedatum

"""

""
name = "Robert"
birthdate = datetime.date(1962, 7, 24)
name = st.text_input("# Voornaam:", value=name, placeholder="Voornaam", max_chars=15)
birthdate = st.date_input("# Geboortedatum", value=birthdate)
""
""

prompt = f"""Ik ben {name} en geboren op {birthdate.strftime("%d-%m-%Y")}. Kun je 3 opvallende bijzonderheden over mijn naam en 3 opvallende bijzonderheden over mijn geboortedatum opnoemen? Formatter het antwoord in markdown en gebruik de headers: Bijzonderheden voornaam: en Bijzonderheden geboortedatum:"""

st.markdown(llm(prompt))



