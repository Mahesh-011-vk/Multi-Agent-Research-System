import json
from datetime import datetime
from pathlib import Path

import streamlit as st

from pipeline import run_research_pipeline


# ---------------------------- Page configuration ----------------------------
st.set_page_config(
    page_title="Burgundy Research Studio",
    page_icon="◆",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------------------------- Premium burgundy theme ------------------------
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@500;600;700&display=swap');

    :root {
        --wine: #35101f;
        --wine-deep: #230914;
        --wine-light: #572238;
        --cream: #f7efe5;
        --muted: #d1bfc5;
        --gold: #d7b477;
        --panel: rgba(255, 248, 241, 0.07);
        --line: rgba(247, 239, 229, 0.15);
    }

    html, body, [data-testid="stAppViewContainer"] {
        background:
            radial-gradient(ellipse at 12% 0%, rgba(130, 48, 76, .38), transparent 42%),
            radial-gradient(ellipse at 92% 18%, rgba(111, 66, 48, .18), transparent 35%),
            linear-gradient(135deg, var(--wine-deep) 0%, var(--wine) 52%, #421629 100%);
        color: var(--cream);
        font-family: 'DM Sans', sans-serif;
    }

    [data-testid="stHeader"] { background: rgba(0,0,0,0); }
    [data-testid="stSidebar"] {
        background: rgba(25, 6, 14, .82);
        border-right: 1px solid var(--line);
    }
    [data-testid="stSidebar"] * { color: var(--cream); }

    .block-container { padding-top: 2.3rem; padding-bottom: 3rem; max-width: 1400px; }
    h1, h2, h3 { color: var(--cream) !important; }
    h1, .serif { font-family: 'Playfair Display', Georgia, serif !important; }
    p, li, label, .stCaption { color: var(--muted); }

    .eyebrow {
        color: var(--gold);
        text-transform: uppercase;
        letter-spacing: .23em;
        font-size: .72rem;
        font-weight: 700;
        margin-bottom: .8rem;
    }
    .hero-title {
        font-family: 'Playfair Display', Georgia, serif;
        font-size: clamp(2.5rem, 5vw, 4.6rem);
        line-height: 1.03;
        letter-spacing: -.035em;
        color: var(--cream);
        margin: 0 0 1rem 0;
    }
    .hero-title span { color: var(--gold); font-style: italic; }
    .hero-subtitle {
        color: var(--muted);
        font-size: 1.03rem;
        max-width: 720px;
        line-height: 1.8;
    }
    .top-line {
        height: 1px;
        background: linear-gradient(90deg, var(--gold), rgba(215,180,119,0));
        margin: 1.5rem 0 1.8rem;
    }
    .glass-card {
        background: var(--panel);
        border: 1px solid var(--line);
        border-radius: 18px;
        padding: 1.2rem 1.3rem;
        min-height: 118px;
        backdrop-filter: blur(12px);
    }
    .metric-label {
        color: var(--muted);
        text-transform: uppercase;
        letter-spacing: .12em;
        font-size: .7rem;
        margin-bottom: .7rem;
    }
    .metric-value {
        color: var(--cream);
        font-family: 'Playfair Display', Georgia, serif;
        font-size: 1.55rem;
        line-height: 1.2;
    }
    .section-kicker {
        color: var(--gold);
        text-transform: uppercase;
        letter-spacing: .16em;
        font-size: .72rem;
        font-weight: 700;
        margin: .4rem 0 .55rem;
    }
    .stTextArea textarea, .stTextInput input {
        background: rgba(255, 248, 241, .06) !important;
        color: var(--cream) !important;
        border: 1px solid rgba(215,180,119,.35) !important;
        border-radius: 12px !important;
    }
    .stTextArea textarea:focus, .stTextInput input:focus {
        border-color: var(--gold) !important;
        box-shadow: 0 0 0 1px var(--gold) !important;
    }
    .stButton > button, .stDownloadButton > button, button[kind="primary"] {
        background: linear-gradient(135deg, #dfc18a, #bd9256) !important;
        color: #2c0c18 !important;
        border: none !important;
        border-radius: 999px !important;
        font-weight: 700 !important;
        padding: .68rem 1.25rem !important;
        min-height: 2.8rem;
        transition: transform .2s ease, filter .2s ease;
    }
    .stButton > button:hover, .stDownloadButton > button:hover {
        filter: brightness(1.08);
        transform: translateY(-1px);
    }
    div[data-testid="stTabs"] button {
        color: var(--muted);
        border-radius: 10px 10px 0 0;
    }
    div[data-testid="stTabs"] button[aria-selected="true"] {
        color: var(--gold);
    }
    [data-testid="stExpander"] {
        border: 1px solid var(--line);
        border-radius: 12px;
        background: rgba(255,255,255,.025);
    }
    [data-testid="stAlert"] { border-radius: 12px; }
    .footer {
        color: #bba5ad;
        font-size: .78rem;
        text-align: center;
        padding-top: 2rem;
        margin-top: 3rem;
        border-top: 1px solid var(--line);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------- Sidebar ---------------------------------------
with st.sidebar:
    st.markdown(
        """
        <div style="padding: .5rem 0 1.4rem">
          <div style="color:#d7b477;font-size:.7rem;letter-spacing:.22em;font-weight:700">
            RESEARCH INTELLIGENCE
          </div>
          <div style="font-family:'Playfair Display',Georgia,serif;font-size:1.65rem;
                      color:#f7efe5;margin-top:.35rem">Maison Research</div>
          <div style="color:#d1bfc5;font-size:.83rem;margin-top:.4rem">
            Multi-agent research workspace
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("---")
    st.markdown("**Your research workflow**")
    st.markdown("01  ·  Web research agent")
    st.markdown("02  ·  Webpage reader agent")
    st.markdown("03  ·  LCEL report writer")
    st.markdown("04  ·  Critic review")
    st.markdown("---")
    st.caption("Powered by your existing pipeline, Gemini model configuration, Tavily search, and webpage extraction.")
    st.caption("Keep API keys in your local `.env` file. Never paste them into the UI.")

# ---------------------------- Hero ------------------------------------------
st.markdown('<div class="eyebrow">A considered approach to discovery</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="hero-title">Research, with <span>clarity.</span></div>',
    unsafe_allow_html=True,
)
st.markdown(
    '<div class="hero-subtitle">A multi-agent research studio that searches the web, reads relevant sources, '
    'builds an evidence-led report, and asks a critic agent to review the result.</div>',
    unsafe_allow_html=True,
)
st.markdown('<div class="top-line"></div>', unsafe_allow_html=True)

# Keep results during Streamlit reruns.
if "research_results" not in st.session_state:
    st.session_state.research_results = None
if "research_topic" not in st.session_state:
    st.session_state.research_topic = ""

left, right = st.columns([1.55, 1], gap="large")

with left:
    st.markdown('<div class="section-kicker">01 / Define your inquiry</div>', unsafe_allow_html=True)
    with st.form("research_form", clear_on_submit=False):
        topic = st.text_area(
            "Research topic",
            value=st.session_state.research_topic,
            placeholder="e.g. How is generative AI changing healthcare operations in 2026?",
            height=125,
            help="Use a focused question for more relevant search results.",
            label_visibility="visible",
        )
        submitted = st.form_submit_button("◆  Run research", type="primary", use_container_width=True)

with right:
    st.markdown('<div class="section-kicker">02 / Your research pipeline</div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="glass-card">
          <div class="metric-label">Research stages</div>
          <div class="metric-value">04 agents &amp; pipelines</div>
          <p style="margin:.65rem 0 0;line-height:1.65">
            Search → Read → Write → Critique<br>
            <span style="color:#d7b477">Evidence first. Clear conclusions.</span>
          </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

if submitted:
    clean_topic = topic.strip()
    if not clean_topic:
        st.warning("Enter a research topic before starting.")
    else:
        st.session_state.research_topic = clean_topic
        try:
            with st.status("Your research studio is working…", expanded=True) as status:
                st.write("Running the web research, webpage reader, report writer, and critic pipeline.")
                results = run_research_pipeline(clean_topic)
                st.session_state.research_results = results
                status.update(label="Research pipeline completed", state="complete", expanded=False)
        except Exception as exc:
            st.error(
                "The research pipeline failed. Check your terminal for the full traceback, "
                "confirm your `.env` keys and API quota, and verify your dependencies."
            )
            with st.expander("Technical error details"):
                st.code(f"{type(exc).__name__}: {exc}")
            st.stop()

results = st.session_state.research_results

if results:
    st.markdown('<div class="top-line"></div>', unsafe_allow_html=True)
    st.markdown('<div class="eyebrow">Your completed research</div>', unsafe_allow_html=True)
    st.markdown(
        f'<h2 style="font-family:Playfair Display,Georgia,serif;font-weight:500">'
        f'{st.session_state.research_topic}</h2>',
        unsafe_allow_html=True,
    )

    report = str(results.get("report", "No report was returned."))
    feedback = str(results.get("feedback", "No critic feedback was returned."))
    search_result = str(results.get("search_result", "No search results were returned."))
    scraped_content = str(results.get("scraped_content", "No scraped content was returned."))

    m1, m2, m3 = st.columns(3, gap="medium")
    with m1:
        st.markdown(
            '<div class="glass-card"><div class="metric-label">Research</div>'
            '<div class="metric-value">Web discovery</div>'
            '<p>Search results and source leads</p></div>',
            unsafe_allow_html=True,
        )
    with m2:
        st.markdown(
            '<div class="glass-card"><div class="metric-label">Synthesis</div>'
            '<div class="metric-value">Evidence report</div>'
            '<p>Structured findings and limitations</p></div>',
            unsafe_allow_html=True,
        )
    with m3:
        st.markdown(
            '<div class="glass-card"><div class="metric-label">Quality check</div>'
            '<div class="metric-value">Critic review</div>'
            '<p>Strengths and improvement areas</p></div>',
            unsafe_allow_html=True,
        )

    tab_report, tab_critic, tab_sources, tab_raw = st.tabs(
        ["✦ Research report", "◎ Critic review", "↗ Research evidence", "⌘ Raw output"]
    )

    with tab_report:
        st.markdown(report)
        st.download_button(
            "Download report (.md)",
            data=report,
            file_name="research_report.md",
            mime="text/markdown",
        )

    with tab_critic:
        st.markdown(feedback)

    with tab_sources:
        st.markdown("#### Web research results")
        st.markdown(search_result)
        st.markdown("#### Extracted webpage evidence")
        st.markdown(scraped_content)

    with tab_raw:
        st.json(results)
        st.download_button(
            "Download all results (.json)",
            data=json.dumps(results, indent=2, ensure_ascii=False),
            file_name="research_report.json",
            mime="application/json",
        )

    # Save a local copy, preserving the existing JSON output behavior.
    try:
        output_path = Path("research_report.json")
        output_path.write_text(
            json.dumps(results, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )
        st.caption(f"Latest results saved locally to `{output_path.resolve()}`.")
    except OSError:
        st.info("Results are available above, but could not be saved to the local JSON file.")

st.markdown(
    '<div class="footer">MAISON RESEARCH STUDIO · MULTI-AGENT INTELLIGENCE · BUILT FOR EVIDENCE-LED WORK</div>',
    unsafe_allow_html=True,
)
