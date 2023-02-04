import streamlit as st
import pandas as pd
import numpy as np
import map_page

st.set_page_config(
    page_title="Aloùette",
    page_icon="🐦",
    layout="wide",
    initial_sidebar_state="expanded",
)

map_page.show_page()