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
Leer 3 bijzonderheden van je voornaam en geboortedatum

"""

def generate_answer(name, birthdate):
  if name == "": return "## Vul een geldige naam in"
  prompt = f"""Ik ben {name} en geboren op {birthdate.strftime("%d-%m-%Y")}. Kun je 3 interessante bijzonderheden over mijn naam en 3 interessante gebeurtenissen op mijn geboortedatum opnoemen? Formatter het antwoord in markdown en gebruik de headers: Bijzonderheden voornaam: en Bijzonderheden geboortedatum:"""
  return llm(prompt)
  


""

with st.form("form"):
  name = st.text_input("# Voornaam:", placeholder="Voornaam", max_chars=15)
  birthdate = st.date_input("# Geboortedatum", value=datetime.date(2000, 1, 1), min_value=datetime.date(1920, 1, 1))
  ""
  ""
  submitted = st.form_submit_button("Genereer bijzonderheden", use_container_width=True)

if submitted:
  st.markdown(generate_answer(name, birthdate))

