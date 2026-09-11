import streamlit as st

def render(df):
    """Render dedicated Data Explorer Sector Page."""
    
    st.markdown(
        '<div style="padding-bottom: 10px;">'
        '<div style="font-size: 11px; font-weight: 700; color: #00ff87; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 4px;">'
        'DATA EXPLORER &nbsp;•&nbsp; INTERACTIVE QUERYING'
        '</div>'
        '<div style="font-size: 36px; font-weight: 900; color: #ffffff; letter-spacing: -1px; line-height: 1.1;">'
        'Dataset <span style="color: #00ff87;">Explorer</span>'
        '</div>'
        '<div style="font-size: 15px; color: #8bb39e; margin-top: 6px; font-weight: 500;">'
        'Filter, inspect, and export state-level EV registration and infrastructure records.'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown("<div style='height: 15px;'></div>", unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1])

    with col1:
        states = ["All States"] + sorted(df["State"].dropna().unique().tolist()) if "State" in df.columns else ["All States"]
        selected_state = st.selectbox("📍 Filter by State", states)

    if selected_state == "All States":
        filtered_df = df.copy()
    else:
        filtered_df = df[df["State"] == selected_state]

    with col2:
        st.markdown(
            f'<div class="kpi-card" style="padding: 12px 18px; margin-top: 25px;">'
            f'<div style="font-size: 10px; font-weight: 700; color: #79a891; text-transform: uppercase;">Showing Records</div>'
            f'<div style="font-size: 20px; font-weight: 800; color: #00ff87;">{len(filtered_df)} / {len(df)} States</div>'
            f'</div>',
            unsafe_allow_html=True
        )

    st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)

    st.dataframe(filtered_df, use_container_width=True)

    st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)

    st.markdown('<div style="font-size: 18px; font-weight: 700; color: #ffffff; margin-bottom: 10px;">Export Filtered Dataset</div>', unsafe_allow_html=True)

    csv = filtered_df.to_csv(index=False)
    st.download_button(
        label="📥 Download CSV Dataset",
        data=csv,
        file_name="ev_chargeiq_filtered_data.csv",
        mime="text/csv"
    )
