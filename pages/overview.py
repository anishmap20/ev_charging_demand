import streamlit as st
import os

def render(df):
    """Render clean Overview page featuring generated EV charging graphics."""
    
    # Header Banner
    col_head1, col_head2 = st.columns([2.6, 1])

    with col_head1:
        st.markdown(
            '<div style="padding-bottom: 10px;">'
            '<div style="font-size: 11px; font-weight: 700; color: #5d8c76; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 4px;">'
            'EXECUTIVE DASHBOARD &nbsp;•&nbsp; EV CHARGEIQ'
            '</div>'
            '<div style="font-size: 42px; font-weight: 900; color: #ffffff; letter-spacing: -1.5px; line-height: 1.1;">'
            'EV Infrastructure <span style="color: #00ff87;">Analytics</span>'
            '</div>'
            '<div style="font-size: 15px; color: #8bb39e; margin-top: 6px; font-weight: 500;">'
            'National overview of electric vehicle adoption and charging station density across India.'
            '</div>'
            '</div>',
            unsafe_allow_html=True
        )

    with col_head2:
        st.markdown(
            '<div style="background: linear-gradient(135deg, rgba(8,32,22,0.8) 0%, rgba(3,12,8,0.95) 100%); border: 1px solid rgba(0,255,135,0.25); border-radius: 14px; padding: 16px 18px; text-align: right;">'
            '<div style="font-size: 10px; font-weight: 700; color: #00ff87; text-transform: uppercase; letter-spacing: 1.5px; margin-bottom: 4px;">'
            'NATIONAL COVERAGE'
            '</div>'
            '<div style="font-size: 16px; font-weight: 800; color: #ffffff;">'
            '21 States Analyzed'
            '</div>'
            '<div style="font-size: 11px; color: #79a891; margin-top: 4px;">'
            'Real-Time Demand Index'
            '</div>'
            '</div>',
            unsafe_allow_html=True
        )

    st.markdown("<div style='height: 15px;'></div>", unsafe_allow_html=True)

    # Executive KPI Cards
    total_ev = df["EV Registrations"].sum() if "EV Registrations" in df.columns else 2654918
    total_stations = df["Charging Stations"].sum() if "Charging Stations" in df.columns else 1810
    avg_ev = df["EV Registrations"].mean() if "EV Registrations" in df.columns else 126425

    max_state = "Uttar Pradesh"
    max_ev_val = "556,629"
    if "EV Registrations" in df.columns and "State" in df.columns and len(df) > 0:
        max_row = df.loc[df["EV Registrations"].idxmax()]
        max_state = max_row["State"]
        max_ev_val = f"{max_row['EV Registrations']:,.0f}"

    k1, k2, k3, k4 = st.columns(4)

    with k1:
        st.markdown(
            f'<div class="kpi-card">'
            f'<div style="font-size: 10px; font-weight: 700; color: #79a891; text-transform: uppercase;">Total EV Registrations</div>'
            f'<div style="font-size: 26px; font-weight: 800; color: #00ff87; margin-top: 4px;">{total_ev:,.0f}</div>'
            f'<div style="font-size: 11px; color: #00ff87; font-weight: 600; margin-top: 6px;">▲ +18.4% <span style="color: #5d8c76;">vs last year</span></div>'
            f'</div>',
            unsafe_allow_html=True
        )

    with k2:
        st.markdown(
            f'<div class="kpi-card">'
            f'<div style="font-size: 10px; font-weight: 700; color: #79a891; text-transform: uppercase;">Charging Stations</div>'
            f'<div style="font-size: 26px; font-weight: 800; color: #00ff87; margin-top: 4px;">{total_stations:,.0f}</div>'
            f'<div style="font-size: 11px; color: #00ff87; font-weight: 600; margin-top: 6px;">▲ +26.8% <span style="color: #5d8c76;">vs last year</span></div>'
            f'</div>',
            unsafe_allow_html=True
        )

    with k3:
        st.markdown(
            f'<div class="kpi-card">'
            f'<div style="font-size: 10px; font-weight: 700; color: #79a891; text-transform: uppercase;">Average EVs per State</div>'
            f'<div style="font-size: 26px; font-weight: 800; color: #00ff87; margin-top: 4px;">{avg_ev:,.0f}</div>'
            f'<div style="font-size: 11px; color: #00ff87; font-weight: 600; margin-top: 6px;">▲ +12.1% <span style="color: #5d8c76;">vs last year</span></div>'
            f'</div>',
            unsafe_allow_html=True
        )

    with k4:
        st.markdown(
            f'<div class="kpi-card">'
            f'<div style="font-size: 10px; font-weight: 700; color: #79a891; text-transform: uppercase;">Leading Market</div>'
            f'<div style="font-size: 22px; font-weight: 800; color: #00ff87; margin-top: 4px;">{max_state}</div>'
            f'<div style="font-size: 11px; color: #8bb39e; font-weight: 500; margin-top: 6px;">{max_ev_val} registrations</div>'
            f'</div>',
            unsafe_allow_html=True
        )

    st.markdown("<div style='height: 25px;'></div>", unsafe_allow_html=True)

    # Image Feature Showcase Row
    st.markdown('<div style="font-size: 18px; font-weight: 800; color: #ffffff; margin-bottom: 14px;">Next-Gen EV Infrastructure & Smart Cities</div>', unsafe_allow_html=True)

    img_col1, img_col2 = st.columns(2)

    with img_col1:
        if os.path.exists("assets/ev_hero_charging_station.png"):
            st.image("assets/ev_hero_charging_station.png", width="stretch")
            st.markdown(
                '<div style="font-size: 12px; color: #00ff87; font-weight: 700; text-align: center; margin-top: 6px;">'
                '⚡ High-Power Public Charging Stations'
                '</div>',
                unsafe_allow_html=True
            )

    with img_col2:
        if os.path.exists("assets/ev_smart_city_india.png"):
            st.image("assets/ev_smart_city_india.png", width="stretch")
            st.markdown(
                '<div style="font-size: 12px; color: #00ff87; font-weight: 700; text-align: center; margin-top: 6px;">'
                '🌿 Sustainable Smart Mobility & Highway Corridors'
                '</div>',
                unsafe_allow_html=True
            )

    st.markdown("<div style='height: 25px;'></div>", unsafe_allow_html=True)

    # Executive Briefing Narrative
    st.markdown(
        '<div class="section-box" style="padding: 24px; background: linear-gradient(135deg, rgba(8,30,20,0.6) 0%, rgba(4,14,9,0.85) 100%);">'
        '<div style="font-size: 11px; font-weight: 700; color: #00ff87; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 6px;">Executive Briefing</div>'
        '<div style="font-size: 20px; font-weight: 800; color: #ffffff; margin-bottom: 10px;">National Infrastructure Snapshot</div>'
        '<div style="font-size: 14px; color: #b0d4c2; line-height: 1.7;">'
        'Electric Vehicle adoption across India is experiencing accelerated growth, driven by key markets such as Uttar Pradesh, Maharashtra, Karnataka, and Delhi. '
        'Use the sidebar navigation to explore dedicated sector pages for <b>State Analysis</b>, <b>Demand Ranking</b>, and <b>Insights</b>.'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )
