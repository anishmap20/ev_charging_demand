import streamlit as st
import pandas as pd
import plotly.express as px
from utils.style import apply_plotly_theme

def render(df):
    """Render dedicated State Analysis Sector Page with Interactive State Search Inspector."""
    
    st.markdown(
        '<div style="padding-bottom: 10px;">'
        '<div style="font-size: 11px; font-weight: 700; color: #00ff87; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 4px;">'
        'SECTOR ANALYTICS &nbsp;•&nbsp; REGIONAL SEARCH & BREAKDOWN'
        '</div>'
        '<div style="font-size: 36px; font-weight: 900; color: #ffffff; letter-spacing: -1px; line-height: 1.1;">'
        'State-by-State <span style="color: #00ff87;">EV Adoption & Details</span>'
        '</div>'
        '<div style="font-size: 15px; color: #8bb39e; margin-top: 6px; font-weight: 500;">'
        'Search any state to inspect detailed vehicle registrations, charger capacity, demand pressure, and policy recommendations.'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown("<div style='height: 15px;'></div>", unsafe_allow_html=True)

    if "State" in df.columns:
        state_list = sorted(df["State"].dropna().unique().tolist())
        
        # State Search Inspector Controls
        st.markdown('<div style="font-size: 18px; font-weight: 800; color: #ffffff; margin-bottom: 10px;">🔍 Search & Inspect State Details</div>', unsafe_allow_html=True)
        selected_state = st.selectbox(
            "Select or type a State name to view detailed information:",
            state_list
        )

        state_data = df[df["State"] == selected_state].iloc[0]

        # Calculate rank
        sorted_temp = df.sort_values("EV Registrations", ascending=False).reset_index(drop=True)
        rank_idx = sorted_temp[sorted_temp["State"] == selected_state].index
        rank_val = rank_idx[0] + 1 if len(rank_idx) > 0 else "-"

        # Determine demand level & status colors
        evs_per_st = state_data["EVs per Station"] if "EVs per Station" in state_data else (state_data["EV Registrations"] / max(state_data["Charging Stations"], 1))
        
        if evs_per_st > 10000:
            badge_col = "#ff4d4d"
            demand_status = "CRITICAL HIGH DEFICIT"
        elif evs_per_st > 3000:
            badge_col = "#ff944d"
            demand_status = "MODERATE PRESSURE"
        else:
            badge_col = "#00ff87"
            demand_status = "SUFFICIENT DENSITY"

        recommendation = state_data["Recommendation"] if "Recommendation" in state_data and pd.notna(state_data["Recommendation"]) else "Monitor infrastructure expansion and highway fast-charging deployment."

        # Detailed State Profile Card
        st.markdown(
            f'<div class="section-box" style="padding: 24px; border-left: 5px solid {badge_col}; background: linear-gradient(135deg, rgba(8,32,22,0.85) 0%, rgba(4,14,9,0.95) 100%);">'
            f'<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px;">'
            f'<div>'
            f'<div style="font-size: 12px; font-weight: 800; color: #79a891; text-transform: uppercase;">National Rank: #{rank_val}</div>'
            f'<div style="font-size: 32px; font-weight: 900; color: #ffffff;">{selected_state}</div>'
            f'</div>'
            f'<div style="background: rgba(0,0,0,0.4); border: 1px solid {badge_col}; color: {badge_col}; font-weight: 800; font-size: 12px; padding: 6px 14px; border-radius: 20px;">'
            f'● {demand_status}'
            f'</div>'
            f'</div>'
            f'<div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 15px; margin-bottom: 20px; background: rgba(0,0,0,0.3); padding: 16px; border-radius: 12px; border: 1px solid rgba(0,255,135,0.15);">'
            f'<div>'
            f'<div style="font-size: 10px; font-weight: 700; color: #79a891; text-transform: uppercase;">EV Registrations</div>'
            f'<div style="font-size: 22px; font-weight: 800; color: #00ff87; margin-top: 4px;">{state_data["EV Registrations"]:,.0f}</div>'
            f'</div>'
            f'<div>'
            f'<div style="font-size: 10px; font-weight: 700; color: #79a891; text-transform: uppercase;">Charging Stations</div>'
            f'<div style="font-size: 22px; font-weight: 800; color: #00ff87; margin-top: 4px;">{state_data["Charging Stations"]:,.0f}</div>'
            f'</div>'
            f'<div>'
            f'<div style="font-size: 10px; font-weight: 700; color: #79a891; text-transform: uppercase;">EVs per Station Ratio</div>'
            f'<div style="font-size: 22px; font-weight: 800; color: {badge_col}; margin-top: 4px;">{evs_per_st:,.0f}</div>'
            f'</div>'
            f'<div>'
            f'<div style="font-size: 10px; font-weight: 700; color: #79a891; text-transform: uppercase;">Total Vehicles</div>'
            f'<div style="font-size: 22px; font-weight: 800; color: #ffffff; margin-top: 4px;">{state_data.get("Total_Vehicles", 0):,.0f}</div>'
            f'</div>'
            f'</div>'
            f'<div style="font-size: 13px; color: #c5e1d4; line-height: 1.6;">'
            f'<b>📌 State Strategic Recommendation:</b> {recommendation}'
            f'</div>'
            f'</div>',
            unsafe_allow_html=True
        )

        st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)

        # Full-width bar chart
        sorted_df = df.sort_values("EV Registrations", ascending=False)
        st.markdown('<div style="font-size: 18px; font-weight: 700; color: #ffffff; margin-bottom: 10px;">EV Registrations Comparison Across States</div>', unsafe_allow_html=True)
        fig_bar = px.bar(
            sorted_df,
            x="State",
            y="EV Registrations",
            color="EV Registrations",
            color_continuous_scale=["#072618", "#125434", "#00ff87"],
            text_auto=",.0f"
        )
        fig_bar.update_traces(
            textposition="outside",
            marker_line_color="rgba(0,255,135,0.4)",
            marker_line_width=1
        )
        fig_bar = apply_plotly_theme(fig_bar)
        fig_bar.update_layout(height=420)
        st.plotly_chart(fig_bar, use_container_width=True)

        st.markdown("<div style='height: 25px;'></div>", unsafe_allow_html=True)

        # Scatter chart - Dots only, hover for details
        st.markdown('<div style="font-size: 18px; font-weight: 700; color: #ffffff; margin-bottom: 10px;">EV Adoption vs Charging Infrastructure Scatter Plot</div>', unsafe_allow_html=True)
        
        scatter_hover_cols = {
            "EV Registrations": ":,.0f",
            "Charging Stations": ":,.0f"
        }
        if "EVs per Station" in sorted_df.columns:
            scatter_hover_cols["EVs per Station"] = ":,.0f"

        fig_scatter = px.scatter(
            sorted_df,
            x="EV Registrations",
            y="Charging Stations",
            size="EV Registrations",
            hover_name="State",
            hover_data=scatter_hover_cols
        )
        fig_scatter.update_traces(
            mode="markers",
            marker=dict(color="#00ff87", opacity=0.85, line=dict(width=1, color="#ffffff"))
        )
        fig_scatter = apply_plotly_theme(fig_scatter)
        fig_scatter.update_layout(height=380)
        st.plotly_chart(fig_scatter, use_container_width=True)
