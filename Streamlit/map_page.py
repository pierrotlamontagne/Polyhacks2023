import streamlit as st

import pydeck as pdk

def show_page():
    st.markdown("<h1 style='text-align: center; color: #642EFE;'>Al-où-ette", unsafe_allow_html=True)

    lat, lon = 45.50890048124889, -73.58776191515908

    query = st.text_input("Entrez une espèce d'oiseau")

    map_container = st.empty()

    map_container.pydeck_chart(pdk.Deck(
        map_style='mapbox://styles/mapbox/dark-v9',
        initial_view_state=pdk.ViewState(
            latitude=lat,
            longitude=lon,
            zoom=12,
            pitch=0,
        ),
        layers=None
    ))

    return