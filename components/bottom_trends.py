import streamlit as st
import plotly.graph_objects as go
from utils.style import apply_plotly_theme

def render_bottom_trends():
    """Render bottom grid: EV trend line graph, station trend line graph, distribution graphic card."""
    b1, b2, b3 = st.columns([1.5, 1.5, 1.4])

    years = [2020, 2021, 2022, 2023, 2024, 2025]
    ev_trend = [200000, 450000, 800000, 1250000, 1700000, 2260000]
    station_trend = [150, 350, 700, 1100, 1450, 1792]

    with b1:
        st.markdown('<div style="font-size: 14px; font-weight: 700; color: #ffffff; margin-bottom: 8px;">EV Registrations Trend (2020–2025)</div>', unsafe_allow_html=True)
        fig_trend1 = go.Figure()
        fig_trend1.add_trace(go.Scatter(
            x=years,
            y=ev_trend,
            mode='lines+markers',
            line=dict(color='#00ff87', width=3),
            marker=dict(size=8, color='#00ff87'),
            name='EV Registrations'
        ))
        fig_trend1.add_annotation(
            x=2025, y=2260000,
            text="2.26M in 2025",
            showarrow=True,
            arrowhead=2,
            arrowcolor="#00ff87",
            ax=-40, ay=-30,
            bgcolor="#00ff87",
            font=dict(color="#000000", size=10, family="Plus Jakarta Sans")
        )
        fig_trend1 = apply_plotly_theme(fig_trend1)
        fig_trend1.update_layout(height=260)
        st.plotly_chart(fig_trend1, use_container_width=True)

    with b2:
        st.markdown('<div style="font-size: 14px; font-weight: 700; color: #ffffff; margin-bottom: 8px;">Charging Stations Trend (2020–2025)</div>', unsafe_allow_html=True)
        fig_trend2 = go.Figure()
        fig_trend2.add_trace(go.Scatter(
            x=years,
            y=station_trend,
            mode='lines+markers',
            line=dict(color='#00ff87', width=3),
            marker=dict(size=8, color='#00ff87'),
            name='Charging Stations'
        ))
        fig_trend2.add_annotation(
            x=2025, y=1792,
            text="1,792 in 2025",
            showarrow=True,
            arrowhead=2,
            arrowcolor="#00ff87",
            ax=-40, ay=-30,
            bgcolor="#00ff87",
            font=dict(color="#000000", size=10, family="Plus Jakarta Sans")
        )
        fig_trend2 = apply_plotly_theme(fig_trend2)
        fig_trend2.update_layout(height=260)
        st.plotly_chart(fig_trend2, use_container_width=True)

    with b3:
        st.markdown('<div style="font-size: 14px; font-weight: 700; color: #ffffff; margin-bottom: 8px;">EV Registrations by State</div>', unsafe_allow_html=True)
        
        map_card_html = (
            '<div class="section-box" style="height: 260px; display: flex; flex-direction: column; justify-content: space-between;">'
            '<div style="display: flex; align-items: center; gap: 10px;">'
            '<div style="font-size: 32px;">🗺️</div>'
            '<div>'
            '<div style="font-size: 13px; font-weight: 700; color: #ffffff;">National Coverage</div>'
            '<div style="font-size: 11px; color: #79a891;">EV Density Classification</div>'
            '</div>'
            '</div>'
            '<div style="display: flex; flex-direction: column; gap: 6px; font-size: 11px;">'
            '<div style="display: flex; align-items: center; justify-content: space-between;"><span><span style="color: #00ff87;">■</span> &gt; 500K Registrations</span><span style="font-weight: 700; color: #00ff87;">High Density</span></div>'
            '<div style="display: flex; align-items: center; justify-content: space-between;"><span><span style="color: #24d879;">■</span> 200K - 500K Registrations</span><span style="font-weight: 700; color: #24d879;">Medium-High</span></div>'
            '<div style="display: flex; align-items: center; justify-content: space-between;"><span><span style="color: #11864d;">■</span> 100K - 200K Registrations</span><span style="font-weight: 700; color: #11864d;">Moderate</span></div>'
            '<div style="display: flex; align-items: center; justify-content: space-between;"><span><span style="color: #0b5933;">■</span> 50K - 100K Registrations</span><span style="font-weight: 700; color: #0b5933;">Emerging</span></div>'
            '<div style="display: flex; align-items: center; justify-content: space-between;"><span><span style="color: #063820;">■</span> &lt; 50K Registrations</span><span style="font-weight: 700; color: #063820;">Early Stage</span></div>'
            '</div>'
            '<div style="background: rgba(0,255,135,0.12); border: 1px solid rgba(0,255,135,0.3); border-radius: 10px; padding: 8px 12px; display: flex; align-items: center; justify-content: space-between;">'
            '<span style="font-size: 11px; font-weight: 700; color: #00ff87;">🌱 Greener India, Stronger Tomorrow</span>'
            '<span style="font-size: 10px; color: #79a891;">2026 Vision</span>'
            '</div>'
            '</div>'
        )
        st.markdown(map_card_html, unsafe_allow_html=True)
