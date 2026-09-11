import streamlit as st

def load_css():
    """Load exact CSS styles matching the dark futuristic EV ChargeIQ mockup."""
    st.markdown(
        '<style>'
        '@import url("https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap");'
        'html, body, [class*="css"] { font-family: "Plus Jakarta Sans", sans-serif; }'
        '.stApp { background-color: #030806 !important; color: #e2f1e9; }'
        'header[data-testid="stHeader"] { background: transparent !important; }'
        '[data-testid="stToolbar"] { display: none !important; }'
        '#MainMenu, footer { visibility: hidden; }'
        '[data-testid="stSidebar"] { background-color: #050d0a !important; border-right: 1px solid #0e3824 !important; }'
        '[data-testid="stSidebarNav"] { display: none !important; }'
        '.kpi-card { background: #081610; border: 1px solid #14402a; border-radius: 16px; padding: 18px 20px; box-shadow: 0 8px 20px rgba(0,0,0,0.4); position: relative; transition: transform 0.2s ease; }'
        '.kpi-card:hover { transform: translateY(-3px); border-color: #00ff87; }'
        '.stButton > button { background: #071911 !important; color: #b5e6ce !important; border: 1px solid #13422b !important; border-radius: 10px !important; padding: 10px 16px !important; font-weight: 600 !important; font-size: 14px !important; text-align: left !important; transition: all 0.2s ease !important; }'
        '.stButton > button:hover { background: #0d2e1f !important; color: #00ff87 !important; border-color: #00ff87 !important; }'
        '[data-testid="stDataFrame"] { border: 1px solid #14402a !important; border-radius: 14px !important; background: #07150f !important; }'
        '.section-box { background: #07150f; border: 1px solid #123824; border-radius: 16px; padding: 20px; box-shadow: 0 4px 15px rgba(0,0,0,0.3); }'
        '</style>',
        unsafe_allow_html=True
    )

def apply_plotly_theme(fig):
    """Apply dark glowing Plotly theme matching mockup."""
    fig.update_layout(
        title=dict(text=""),
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(6,19,13,0.6)",
        font=dict(
            family="Plus Jakarta Sans, sans-serif",
            color="#8bb39e",
            size=11
        ),
        title_font=dict(
            color="#ffffff",
            size=14
        ),
        xaxis=dict(
            gridcolor="#0e2b1c",
            zerolinecolor="#14402a",
            tickfont=dict(color="#6c9983")
        ),
        yaxis=dict(
            gridcolor="#0e2b1c",
            zerolinecolor="#14402a",
            tickfont=dict(color="#6c9983")
        ),
        margin=dict(l=20, r=20, t=20, b=20)
    )
    return fig
