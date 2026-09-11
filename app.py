import streamlit as st

from utils.style import load_css
from utils.data_loader import load_data
from utils.sidebar import render_sidebar
from components.footer_bar import render_footer_bar

from pages import (
    overview,
    state_analysis,
    demand_ranking,
    insights,
    data_explorer
)

# Page configuration
st.set_page_config(
    page_title="EV ChargeIQ - Powering a Cleaner Tomorrow",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load CSS styles & cached data
load_css()
df = load_data()

# Initialize default session state page
if "page" not in st.session_state:
    st.session_state.page = "Overview"

# Render left sidebar navigation
render_sidebar()

# Page routing logic
if st.session_state.page == "Overview":
    overview.render(df)
elif st.session_state.page == "State Analysis":
    state_analysis.render(df)
elif st.session_state.page == "Demand Ranking":
    demand_ranking.render(df)
elif st.session_state.page == "Insights":
    insights.render(df)
elif st.session_state.page == "Data Explorer":
    data_explorer.render(df)

# Render footer bar from component
render_footer_bar()