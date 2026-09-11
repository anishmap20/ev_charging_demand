import streamlit as st
import plotly.express as px
from utils.style import apply_plotly_theme

def render(df):
    """Render dedicated Demand Ranking Sector Page without raw dataset tables."""
    
    st.markdown(
        '<div style="padding-bottom: 10px;">'
        '<div style="font-size: 11px; font-weight: 700; color: #ff944d; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 4px;">'
        'SECTOR ANALYTICS &nbsp;•&nbsp; BOTTLENECK EVALUATION'
        '</div>'
        '<div style="font-size: 36px; font-weight: 900; color: #ffffff; letter-spacing: -1px; line-height: 1.1;">'
        'Charging Demand <span style="color: #ff944d;">Ranking</span>'
        '</div>'
        '<div style="font-size: 15px; color: #8bb39e; margin-top: 6px; font-weight: 500;">'
        'Identify high-deficit priority states requiring immediate charging station infrastructure expansion.'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown("<div style='height: 15px;'></div>", unsafe_allow_html=True)

    result = df.copy()
    if "EVs per Station" not in result.columns and "EV Registrations" in result.columns and "Charging Stations" in result.columns:
        result["EVs per Station"] = (
            result["EV Registrations"] / result["Charging Stations"].replace(0, 1)
        )

    if "EVs per Station" in result.columns:
        result = result.sort_values("EVs per Station", ascending=False).reset_index(drop=True)
        result["Rank"] = range(1, len(result) + 1)

        # Top 3 Deficit Spotlight Cards
        c1, c2, c3 = st.columns(3)
        medals = [("🥇 #1 Highest Deficit", "#ff4d4d"), ("🥈 #2 High Deficit", "#ff944d"), ("🥉 #3 Moderate Deficit", "#ffd11a")]
        
        for idx, (col, (badge, col_accent)) in enumerate(zip([c1, c2, c3], medals)):
            if idx < len(result):
                row = result.iloc[idx]
                with col:
                    st.markdown(
                        f'<div class="kpi-card" style="border-top: 3px solid {col_accent};">'
                        f'<div style="font-size: 11px; font-weight: 800; color: {col_accent}; text-transform: uppercase; margin-bottom: 6px;">{badge}</div>'
                        f'<div style="font-size: 22px; font-weight: 800; color: #ffffff;">{row["State"]}</div>'
                        f'<div style="font-size: 15px; font-weight: 800; color: {col_accent}; margin-top: 4px;">⚡ {row["EVs per Station"]:,.0f} EVs / Station</div>'
                        f'<div style="font-size: 11px; color: #79a891; margin-top: 4px;">{row["EV Registrations"]:,.0f} EVs • {row["Charging Stations"]:,.0f} Stations</div>'
                        f'</div>',
                        unsafe_allow_html=True
                    )

        st.markdown("<div style='height: 25px;'></div>", unsafe_allow_html=True)

        # Demand Pressure Bar Chart
        st.markdown('<div style="font-size: 18px; font-weight: 700; color: #ffffff; margin-bottom: 10px;">EV Demand Pressure Index (EVs per Charging Station)</div>', unsafe_allow_html=True)
        fig_demand = px.bar(
            result,
            x="State",
            y="EVs per Station",
            color="EVs per Station",
            color_continuous_scale="Reds",
            text_auto=",.0f"
        )
        fig_demand.update_traces(
            textposition="outside",
            marker_line_color="rgba(255,77,77,0.4)",
            marker_line_width=1
        )
        fig_demand = apply_plotly_theme(fig_demand)
        fig_demand.update_layout(height=420)
        st.plotly_chart(fig_demand, use_container_width=True)

        st.markdown("<div style='height: 25px;'></div>", unsafe_allow_html=True)

        # Ranked List View (Visual list instead of raw dataframe)
        st.markdown('<div style="font-size: 18px; font-weight: 700; color: #ffffff; margin-bottom: 10px;">Full Infrastructure Deficit Ranking</div>', unsafe_allow_html=True)
        
        list_html = '<div class="section-box" style="padding: 16px 20px;">'
        for _, r in result.iterrows():
            col_tag = "#ff4d4d" if r["EVs per Station"] > 10000 else ("#ff944d" if r["EVs per Station"] > 3000 else "#00ff87")
            list_html += (
                f'<div style="display: flex; align-items: center; justify-content: space-between; padding: 10px 0; border-bottom: 1px solid rgba(255,255,255,0.05);">'
                f'<div style="display: flex; align-items: center; gap: 14px;">'
                f'<div style="background: {col_tag}; color: #000; font-weight: 800; font-size: 12px; border-radius: 50%; width: 26px; height: 26px; display: flex; align-items: center; justify-content: center;">{r["Rank"]}</div>'
                f'<div>'
                f'<div style="font-size: 15px; font-weight: 700; color: #ffffff;">{r["State"]}</div>'
                f'<div style="font-size: 11px; color: #79a891;">{r["EV Registrations"]:,.0f} EVs • {r["Charging Stations"]:,.0f} Stations</div>'
                f'</div>'
                f'</div>'
                f'<div style="font-size: 15px; font-weight: 800; color: {col_tag};">{r["EVs per Station"]:,.0f} <span style="font-size: 11px; font-weight: 500; color: #79a891;">EVs/Station</span></div>'
                f'</div>'
            )
        list_html += '</div>'
        st.markdown(list_html, unsafe_allow_html=True)
