import streamlit as st
import plotly.express as px
import pandas as pd
from utils.style import apply_plotly_theme

def render_middle_charts(df):
    """Render middle grid: Scatter chart, Top 5 horizontal bars, Demand index list."""
    m1, m2, m3 = st.columns([1.8, 1.4, 1.1])

    with m1:
        st.markdown(
            '<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">'
            '<div style="font-size: 14px; font-weight: 700; color: #ffffff;">EV Registrations vs Charging Stations</div>'
            '<div style="font-size: 11px; color: #00ff87; background: rgba(0,255,135,0.1); padding: 2px 10px; border-radius: 12px; border: 1px solid rgba(0,255,135,0.2);">All States ˅</div>'
            '</div>',
            unsafe_allow_html=True
        )
        fig_scatter = px.scatter(
            df,
            x="EV Registrations",
            y="Charging Stations",
            size="EV Registrations" if "EV Registrations" in df.columns else None,
            hover_name="State",
            hover_data={
                "EV Registrations": ":,.0f",
                "Charging Stations": ":,.0f"
            }
        )
        fig_scatter.update_traces(
            mode="markers",
            marker=dict(color="#00ff87", opacity=0.85, line=dict(width=1, color="#ffffff"))
        )
        fig_scatter = apply_plotly_theme(fig_scatter)
        fig_scatter.update_layout(height=310)
        st.plotly_chart(fig_scatter, use_container_width=True)

    with m2:
        st.markdown('<div style="font-size: 14px; font-weight: 700; color: #ffffff; margin-bottom: 8px;">Top 5 States by EV Registrations</div>', unsafe_allow_html=True)
        top5_df = df.sort_values("EV Registrations", ascending=False).head(5) if "EV Registrations" in df.columns else pd.DataFrame()
        
        fig_top5 = px.bar(
            top5_df,
            y="State",
            x="EV Registrations",
            orientation="h",
            text_auto=",.0f"
        )
        fig_top5.update_traces(
            marker_color="#00ff87",
            textposition="outside"
        )
        fig_top5 = apply_plotly_theme(fig_top5)
        fig_top5.update_layout(height=310, yaxis=dict(autorange="reversed"))
        st.plotly_chart(fig_top5, use_container_width=True)

    with m3:
        st.markdown('<div style="font-size: 14px; font-weight: 700; color: #ffffff; margin-bottom: 8px;">Charging Demand Index <span style="font-size: 11px; font-weight: 400; color: #8bb39e;">(EVs per Station)</span></div>', unsafe_allow_html=True)
        
        demand_list = [
            ("🔴", "1", "Bihar", "155,457", "#ff4d4d"),
            ("🟠", "2", "Assam", "58,302", "#ff944d"),
            ("🟡", "3", "Jharkhand", "17,665", "#ffd11a"),
            ("🟢", "4", "Andhra Pradesh", "11,083", "#00ff87"),
            ("🟢", "5", "West Bengal", "9,587", "#00ff87")
        ]

        if "EVs per Station" in df.columns:
            top_demand = df.sort_values("EVs per Station", ascending=False).head(5)
            colors = ["#ff4d4d", "#ff944d", "#ffd11a", "#00ff87", "#00ff87"]
            demand_list = []
            for i, (_, r) in enumerate(top_demand.iterrows()):
                c = colors[i] if i < len(colors) else "#00ff87"
                demand_list.append(("🟢" if i >= 3 else "🔴", str(i+1), r["State"], f"{r['EVs per Station']:,.0f}", c))

        html_list = '<div class="section-box" style="padding: 14px 16px; height: 310px; overflow-y: auto;">'
        for icon, rank, state_name, ratio, col in demand_list:
            html_list += (
                f'<div style="display: flex; align-items: center; justify-content: space-between; padding: 8px 0; border-bottom: 1px solid rgba(255,255,255,0.05);">'
                f'<div style="display: flex; align-items: center; gap: 10px;">'
                f'<div style="background: {col}; color: #000; font-weight: 800; font-size: 11px; border-radius: 50%; width: 22px; height: 22px; display: flex; align-items: center; justify-content: center;">{rank}</div>'
                f'<div style="font-size: 13px; font-weight: 600; color: #ffffff;">{state_name}</div>'
                f'</div>'
                f'<div style="font-size: 13px; font-weight: 700; color: #00ff87;">{ratio}</div>'
                f'</div>'
            )
        html_list += '</div>'
        st.markdown(html_list, unsafe_allow_html=True)

    st.markdown("<div style='height: 15px;'></div>", unsafe_allow_html=True)
