import streamlit as st

import pydeck as pdk

def show_page():
    st.markdown("<h1 style='text-align: center; color: #642EFE;'>Al-où-ette", unsafe_allow_html=True)

    lat, lon = 45.50890048124889, -73.58776191515908

    species = st.selectbox("Selectionner l'espèce",("Prob1","Prob2"))

    map_container = st.empty()

    histod = pdk.Layer(
        'GeoJsonLayer',
        #"./Data/test_grid.json",
        "https://raw.githubusercontent.com/pierrotlamontagne/Polyhacks2023/main/Data/test_grid.json",
        #"https://raw.githubusercontent.com/visgl/deck.gl-data/master/examples/geojson/vancouver-blocks.json",
        opacity=0.6,
        stroked=False,
        filled=True,
        extruded=True,
        wireframe=True,
        get_elevation='properties.probPerSector * 500',
        get_fill_color='[200,0,0]',
        get_line_color='[255,255,255]',
        pickable=True,
    )

    histod2 = pdk.Layer(
        'GeoJsonLayer',
        #"./Data/test_grid.json",
        "https://raw.githubusercontent.com/pierrotlamontagne/Polyhacks2023/main/Data/test_grid.json",
        #"https://raw.githubusercontent.com/visgl/deck.gl-data/master/examples/geojson/vancouver-blocks.json",
        opacity=0.6,
        stroked=False,
        filled=True,
        extruded=True,
        wireframe=True,
        get_elevation='properties.probPerSector2 * 500',
        get_fill_color='[0,0,200]',
        get_line_color='[255,255,255]',
        pickable=True,
    )

    layer_dict = {
        "Prob1":histod,
        "Prob2":histod2,
    }

    map_container.pydeck_chart(pdk.Deck(
        map_style='mapbox://styles/mapbox/dark-v9',
        initial_view_state=pdk.ViewState(
            latitude=lat,
            longitude=lon,
            zoom=12,
            pitch=35,
        ),
        layers=[layer_dict[species]]
    ))

    return