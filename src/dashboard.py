"""
BI-style dashboard for content automation studio.
Phase 1: read-only scaffolding.
"""

import streamlit as st

st.set_page_config(page_title="Content Automation Studio", layout="wide")

st.title("Content Automation Studio – BI View")

st.markdown("### Studio Overview")
col1, col2, col3 = st.columns(3)
col1.metric("Jobs Today", 0)
col2.metric("Avg Cycle Time (min)", "-")
col3.metric("Render Failure Rate", "0%")

st.markdown("---")
st.markdown("### Pipeline Board (Placeholder)")
st.info("Pipeline visualization will appear here.")

st.markdown("---")
st.markdown("### Script Analytics (Placeholder)")
st.info("Script timelines, sentiment arcs, and pacing charts will appear here.")
