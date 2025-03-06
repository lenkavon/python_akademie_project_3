import streamlit as st
import pandas as pd
import numpy as np
from scraper.election_result import scrape_election_results, validate_source_url
import os.path

if 'button' not in st.session_state:
    st.session_state.button = False
    st.session_state.city_name = "např. Litoměřice"


url = st.text_input("zadejte odkaz na vysledky voleb roku 2017")


def handle_scrape(valid_url):
    st.session_state.button = True
    st.session_state.city_name = scrape_election_results(valid_url, "vysledky.csv")

is_valid_url = validate_source_url(url)
if is_valid_url== False:
  st.write("Neplatný odkaz")
else:
  st.write(is_valid_url)
  st.button("Stáhnout data", on_click=handle_scrape, args=[is_valid_url])


df = pd.read_csv('example_vysledky.csv')
if os.path.isfile("vysledky.csv"):
  df = pd.read_csv('vysledky.csv')


st.write("vysledky voleb roku 2017 pro:")
st.write(st.session_state.city_name )
st.dataframe(data=df)

parties = df.iloc[:, 5:].sum()
total_votes = df.iloc[1:, 4].sum()

percentage_results = (parties.divide(total_votes) * 100).round(0)

tab1, tab2 = st.tabs(["graf", "vysledky"])
tab1.bar_chart(percentage_results.sort_values(ascending=False), height=250)
tab2.dataframe({"hlasy": parties, "procenta": percentage_results}, height=250, use_container_width=True)
