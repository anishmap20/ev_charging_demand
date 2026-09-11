import streamlit as st

def render(df):
    """Render dedicated Insights & Strategic Takeaways Sector Page."""
    
    st.markdown(
        '<div style="padding-bottom: 10px;">'
        '<div style="font-size: 11px; font-weight: 700; color: #00ff87; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 4px;">'
        'STRATEGIC INTELLIGENCE &nbsp;•&nbsp; POLICY RECOMMENDATIONS'
        '</div>'
        '<div style="font-size: 36px; font-weight: 900; color: #ffffff; letter-spacing: -1px; line-height: 1.1;">'
        'Infrastructure <span style="color: #00ff87;">Insights</span>'
        '</div>'
        '<div style="font-size: 15px; color: #8bb39e; margin-top: 6px; font-weight: 500;">'
        'Key strategic findings and actionable deployment recommendations distilled from state dataset.'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown("<div style='height: 15px;'></div>", unsafe_allow_html=True)

    if len(df) > 0 and "EV Registrations" in df.columns:
        highest_ev = df.loc[df["EV Registrations"].idxmax()]
        highest_stations = df.loc[df["Charging Stations"].idxmax()]

        pressure = df.copy()
        if "EVs per Station" not in pressure.columns and "Charging Stations" in pressure.columns:
            pressure["EVs per Station"] = (
                pressure["EV Registrations"] / pressure["Charging Stations"].replace(0, 1)
            )

        highest_pressure = pressure.loc[pressure["EVs per Station"].idxmax()]

        c1, c2, c3 = st.columns(3)

        with c1:
            st.markdown(
                f'<div class="kpi-card" style="min-height: 220px; border-top: 3px solid #00ff87;">'
                f'<div style="font-size: 11px; font-weight: 700; color: #00ff87; text-transform: uppercase; margin-bottom: 8px;">🟢 Leader in EV Adoption</div>'
                f'<div style="font-size: 24px; font-weight: 800; color: #ffffff;">{highest_ev["State"]}</div>'
                f'<div style="font-size: 18px; font-weight: 800; color: #00ff87; margin-top: 4px;">{highest_ev["EV Registrations"]:,.0f} EVs</div>'
                f'<div style="font-size: 12px; color: #79a891; margin-top: 8px; line-height: 1.5;">Pioneering state in overall EV volume. High demand for fast chargers on major commuting hubs.</div>'
                f'</div>',
                unsafe_allow_html=True
            )

        with c2:
            st.markdown(
                f'<div class="kpi-card" style="min-height: 220px; border-top: 3px solid #00e5ff;">'
                f'<div style="font-size: 11px; font-weight: 700; color: #00e5ff; text-transform: uppercase; margin-bottom: 8px;">⚡ Charger Density Leader</div>'
                f'<div style="font-size: 24px; font-weight: 800; color: #ffffff;">{highest_stations["State"]}</div>'
                f'<div style="font-size: 18px; font-weight: 800; color: #00e5ff; margin-top: 4px;">{highest_stations["Charging Stations"]:,.0f} Stations</div>'
                f'<div style="font-size: 12px; color: #79a891; margin-top: 8px; line-height: 1.5;">Highest concentration of active public charging points installed. Serves as urban benchmark.</div>'
                f'</div>',
                unsafe_allow_html=True
            )

        with c3:
            st.markdown(
                f'<div class="kpi-card" style="min-height: 220px; border-top: 3px solid #ff4d4d;">'
                f'<div style="font-size: 11px; font-weight: 700; color: #ff4d4d; text-transform: uppercase; margin-bottom: 8px;">⚠️ Critical Infrastructure Gap</div>'
                f'<div style="font-size: 24px; font-weight: 800; color: #ffffff;">{highest_pressure["State"]}</div>'
                f'<div style="font-size: 18px; font-weight: 800; color: #ff4d4d; margin-top: 4px;">{highest_pressure["EVs per Station"]:,.0f} EVs / Station</div>'
                f'<div style="font-size: 12px; color: #79a891; margin-top: 8px; line-height: 1.5;">Urgent priority zone where vehicle onboarding severely outpaces public charger installation.</div>'
                f'</div>',
                unsafe_allow_html=True
            )

        st.markdown("<div style='height: 25px;'></div>", unsafe_allow_html=True)

        st.markdown(
            '<div class="section-box" style="padding: 24px; background: linear-gradient(135deg, rgba(8,30,20,0.6) 0%, rgba(4,14,9,0.85) 100%);">'
            '<div style="font-size: 18px; font-weight: 800; color: #00ff87; margin-bottom: 12px;">📌 Strategic Action Plan</div>'
            '<div style="font-size: 14px; color: #c5e1d4; line-height: 1.8;">'
            '• <b>Targeted Capital Grants:</b> Direct immediate state-level subsidy allocations toward high-deficit regions.<br>'
            '• <b>Highway Corridor Deployment:</b> Inter-city expressways connecting high-density hubs require continuous DC fast charging.<br>'
            '• <b>Grid Transformer Upgrades:</b> Heavy cluster urban zones require utility-side transformer capacity expansion for multi-port fast charging peaks.'
            '</div>'
            '</div>',
            unsafe_allow_html=True
        )
