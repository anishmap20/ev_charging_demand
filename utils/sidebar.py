import streamlit as st

def safe_rerun():
    """Fallback rerun method compatible with Streamlit 1.23.1+ and older versions."""
    if hasattr(st, "rerun"):
        st.rerun()
    elif hasattr(st, "experimental_rerun"):
        st.experimental_rerun()

def render_sidebar():
    """Render clean, decent navigation sidebar."""
    with st.sidebar:
        st.markdown(
            '<div style="padding: 10px 0 20px 0;">'
            '<div style="font-size: 24px; font-weight: 800; color: #00ff87; letter-spacing: -0.5px; display: flex; align-items: center; gap: 8px;">'
            '<span style="font-size: 26px;">⚡</span> <span>EV Charge<span style="color: #ffffff;">IQ</span></span>'
            '</div>'
            '<div style="font-size: 11px; color: #79a891; font-weight: 600; margin-top: 2px;">'
            'Infrastructure Analytics'
            '</div>'
            '</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div style="font-size: 11px; font-weight: 700; color: #5d8c76; text-transform: uppercase; letter-spacing: 1.5px; margin: 15px 0 10px 4px;">Navigation</div>',
            unsafe_allow_html=True
        )

        pages = [
            ("🏠", "Overview"),
            ("📊", "State Analysis"),
            ("🏆", "Demand Ranking"),
            ("💡", "Insights"),
            ("🗄️", "Data Explorer")
        ]

        for icon, page_name in pages:
            if st.session_state.get("page") == page_name:
                st.markdown(
                    f'<div style="background: linear-gradient(90deg, #0e3d26 0%, #062316 100%); border-left: 4px solid #00ff87; color: #00ff87; font-weight: 700; padding: 12px 16px; border-radius: 0 10px 10px 0; margin-bottom: 8px; font-size: 14px; display: flex; align-items: center; gap: 10px; box-shadow: 0 4px 15px rgba(0, 255, 135, 0.15);">'
                    f'<span>{icon}</span> <span>{page_name}</span>'
                    f'</div>',
                    unsafe_allow_html=True
                )
            else:
                if st.button(
                    f"{icon}   {page_name}",
                    key=f"nav_{page_name}",
                    use_container_width=True
                ):
                    st.session_state.page = page_name
                    safe_rerun()

        st.markdown(
            '<div style="margin-top: 50px; background: rgba(8, 32, 22, 0.6); border: 1px solid rgba(0, 255, 135, 0.15); border-radius: 14px; padding: 16px; text-align: left;">'
            '<div style="font-size: 11px; font-weight: 700; color: #00ff87; text-transform: uppercase; letter-spacing: 1px;">System Status</div>'
            '<div style="font-size: 13px; color: #ffffff; margin-top: 4px; font-weight: 600;">21 State Dataset Active</div>'
            '<div style="font-size: 10px; color: #5d8c76; margin-top: 2px;">Real-time analytics engine</div>'
            '</div>',
            unsafe_allow_html=True
        )
