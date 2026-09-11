import streamlit as st

def render_kpi_cards(df):
    """Render 4 KPI metric cards section."""
    total_ev = df["EV Registrations"].sum() if "EV Registrations" in df.columns else 2260000
    total_stations = df["Charging Stations"].sum() if "Charging Stations" in df.columns else 1792
    avg_ev = df["EV Registrations"].mean() if "EV Registrations" in df.columns else 226000

    max_state = "Karnataka"
    max_ev_val = "590,000"
    if "EV Registrations" in df.columns and "State" in df.columns and len(df) > 0:
        max_row = df.loc[df["EV Registrations"].idxmax()]
        max_state = max_row["State"]
        max_ev_val = f"{max_row['EV Registrations']:,.0f}"

    k1, k2, k3, k4 = st.columns(4)

    with k1:
        st.markdown(
            f'<div class="kpi-card">'
            f'<div style="display: flex; justify-content: space-between; align-items: flex-start;">'
            f'<div style="background: rgba(0,255,135,0.15); border: 1px solid rgba(0,255,135,0.3); border-radius: 50%; width: 38px; height: 38px; display: flex; align-items: center; justify-content: center; font-size: 18px;">🚗</div>'
            f'<div>'
            f'<div style="font-size: 10px; font-weight: 700; color: #79a891; text-transform: uppercase;">Total EV Registrations</div>'
            f'<div style="font-size: 24px; font-weight: 800; color: #00ff87; margin-top: 2px;">{total_ev:,.0f}</div>'
            f'<div style="font-size: 11px; color: #00ff87; font-weight: 700; margin-top: 4px;">▲ 18.4% <span style="color: #5d8c76; font-weight: 400;">vs last year</span></div>'
            f'</div>'
            f'</div>'
            f'</div>',
            unsafe_allow_html=True
        )

    with k2:
        st.markdown(
            f'<div class="kpi-card">'
            f'<div style="display: flex; justify-content: space-between; align-items: flex-start;">'
            f'<div style="background: rgba(0,255,135,0.15); border: 1px solid rgba(0,255,135,0.3); border-radius: 50%; width: 38px; height: 38px; display: flex; align-items: center; justify-content: center; font-size: 18px;">⛽</div>'
            f'<div>'
            f'<div style="font-size: 10px; font-weight: 700; color: #79a891; text-transform: uppercase;">Charging Stations</div>'
            f'<div style="font-size: 24px; font-weight: 800; color: #00ff87; margin-top: 2px;">{total_stations:,.0f}</div>'
            f'<div style="font-size: 11px; color: #00ff87; font-weight: 700; margin-top: 4px;">▲ 26.8% <span style="color: #5d8c76; font-weight: 400;">vs last year</span></div>'
            f'</div>'
            f'</div>'
            f'</div>',
            unsafe_allow_html=True
        )

    with k3:
        st.markdown(
            f'<div class="kpi-card">'
            f'<div style="display: flex; justify-content: space-between; align-items: flex-start;">'
            f'<div style="background: rgba(0,255,135,0.15); border: 1px solid rgba(0,255,135,0.3); border-radius: 50%; width: 38px; height: 38px; display: flex; align-items: center; justify-content: center; font-size: 18px;">👥</div>'
            f'<div>'
            f'<div style="font-size: 10px; font-weight: 700; color: #79a891; text-transform: uppercase;">Average EVs per State</div>'
            f'<div style="font-size: 24px; font-weight: 800; color: #00ff87; margin-top: 2px;">{avg_ev:,.0f}</div>'
            f'<div style="font-size: 11px; color: #00ff87; font-weight: 700; margin-top: 4px;">▲ 12.1% <span style="color: #5d8c76; font-weight: 400;">vs last year</span></div>'
            f'</div>'
            f'</div>'
            f'</div>',
            unsafe_allow_html=True
        )

    with k4:
        st.markdown(
            f'<div class="kpi-card">'
            f'<div style="display: flex; justify-content: space-between; align-items: flex-start;">'
            f'<div style="background: rgba(0,255,135,0.15); border: 1px solid rgba(0,255,135,0.3); border-radius: 50%; width: 38px; height: 38px; display: flex; align-items: center; justify-content: center; font-size: 18px;">🏆</div>'
            f'<div>'
            f'<div style="font-size: 10px; font-weight: 700; color: #79a891; text-transform: uppercase;">Leading State</div>'
            f'<div style="font-size: 22px; font-weight: 800; color: #00ff87; margin-top: 2px;">{max_state}</div>'
            f'<div style="font-size: 11px; color: #8bb39e; font-weight: 500; margin-top: 4px;">{max_ev_val} EV registrations</div>'
            f'</div>'
            f'</div>'
            f'</div>',
            unsafe_allow_html=True
        )

    st.markdown("<div style='height: 15px;'></div>", unsafe_allow_html=True)
