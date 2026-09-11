import streamlit as st

def render_footer_bar():
    """Render footer bar matching exact mockup."""
    st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)
    footer_html = (
        '<div style="border-top: 1px solid #0e3824; padding-top: 16px; margin-top: 20px; display: flex; justify-content: space-between; align-items: center; font-size: 12px; color: #5d8c76;">'
        '<div style="display: flex; gap: 20px; font-size: 11px; font-weight: 600; color: #8bb39e;">'
        '<span>🌱 Lower Emissions</span>'
        '<span>🌱 Cleaner Cities</span>'
        '<span>👥 Higher Adoption</span>'
        '<span>📊 Economic Growth</span>'
        '</div>'
        '<div style="font-size: 11px; color: #5d8c76;">'
        'EV ChargeIQ &nbsp;|&nbsp; Data for a Sustainable Tomorrow &nbsp;|&nbsp; Made with <span style="color: #00ff87;">💚</span>'
        '</div>'
        '</div>'
    )
    st.markdown(footer_html, unsafe_allow_html=True)
