import streamlit as st

def render_header_banner():
    """Render top search bar & executive title banner."""
    # Top Control Bar
    top_bar_html = (
        '<div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 20px;">'
        '<div style="background: rgba(14, 43, 28, 0.6); border: 1px solid rgba(0, 255, 135, 0.2); border-radius: 20px; padding: 8px 18px; display: flex; align-items: center; gap: 10px; width: 320px;">'
        '<span style="color: #00ff87; font-size: 14px;">🔍</span>'
        '<span style="color: #6c9c84; font-size: 13px; font-weight: 500;">India\'s EV future, powered by data</span>'
        '</div>'
        '<div style="display: flex; align-items: center; gap: 14px;">'
        '<div style="background: rgba(14, 43, 28, 0.6); border: 1px solid rgba(0, 255, 135, 0.2); border-radius: 20px; padding: 6px 14px; font-size: 12px; color: #8bb39e; display: flex; align-items: center; gap: 6px;">'
        '<span>📅</span> <span style="color: #ffffff; font-weight: 600;">Sep 10, 2026</span>'
        '</div>'
        '<div style="font-size: 12px; color: #00ff87; font-weight: 700; display: flex; align-items: center; gap: 6px;">'
        '<span>🌱</span> <span>Drive Change - <span style="color: #ffffff;">Go Electric</span></span>'
        '</div>'
        '<div style="background: linear-gradient(135deg, #00ff87 0%, #00b359 100%); color: #000000; font-weight: 800; font-size: 12px; border-radius: 50%; width: 32px; height: 32px; display: flex; align-items: center; justify-content: center;">'
        'AP'
        '</div>'
        '</div>'
        '</div>'
    )
    st.markdown(top_bar_html, unsafe_allow_html=True)

    # Header Title Banner
    col_head1, col_head2 = st.columns([2.6, 1])

    with col_head1:
        st.markdown(
            '<div style="padding-bottom: 10px;">'
            '<div style="font-size: 11px; font-weight: 700; color: #5d8c76; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 4px;">'
            'DATA &nbsp; INSIGHTS &nbsp; IMPACT'
            '</div>'
            '<div style="font-size: 44px; font-weight: 900; color: #ffffff; letter-spacing: -1.5px; line-height: 1.1;">'
            'EV <span style="color: #00ff87;">ChargeIQ</span>'
            '</div>'
            '<div style="font-size: 15px; color: #8bb39e; margin-top: 6px; font-weight: 500;">'
            'Data-driven analysis of EV charging demand across India'
            '</div>'
            '</div>',
            unsafe_allow_html=True
        )

    with col_head2:
        st.markdown(
            '<div style="background: linear-gradient(135deg, rgba(8,32,22,0.8) 0%, rgba(3,12,8,0.95) 100%); border: 1px solid rgba(0,255,135,0.25); border-radius: 14px; padding: 14px 18px; text-align: right;">'
            '<div style="font-size: 11px; font-weight: 700; color: #ffffff; margin-bottom: 4px;">'
            'More EVs &nbsp;•&nbsp; Stronger Infrastructure &nbsp;•&nbsp; A Cleaner Planet'
            '</div>'
            '<div style="font-size: 10px; color: #00ff87; font-weight: 800; tracking-wider: 1px; margin-top: 8px;">'
            'SUSTAINABLE MOBILITY FOR A BRIGHTER TOMORROW'
            '</div>'
            '</div>',
            unsafe_allow_html=True
        )

    st.markdown("<div style='height: 15px;'></div>", unsafe_allow_html=True)
