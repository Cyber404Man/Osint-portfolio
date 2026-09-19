"""
Agentic Risk Intelligence Platform - Live Dashboard
Final Demo for Client and Airbus

Run with: streamlit run app.py
Deploys free on Streamlit Cloud
"""

import streamlit as st
import json
from pathlib import Path
from datetime import datetime

st.set_page_config(page_title="Agentic Risk Intelligence Platform", layout="wide", page_icon=":ship:")

st.title("🚢 Agentic Risk Intelligence Platform")
st.subheader("Global Data + Governed AI Agents + Insights Investigator | Decision-Ready at Mission Speed")
st.markdown("---")

# Sidebar - Platform Info
st.sidebar.title("Platform Status")
st.sidebar.success("Mode: Governed AI Enabled")
st.sidebar.info("Agents: 3 Active - AIS Hunter- SAR Verifier- Investigator")
st.sidebar.markdown("**AOI:** SE Malta 35.2-35.6N 15.4-15.9E")
st.sidebar.markdown("**Data Sources:** MarineTraffic, Sentinel-1 SAR, Sanctions Lists")

# Load data if exists
audit_path = Path("data/governed_audit_log.json")
sar_path = Path("data/sar_real_analysis.json")
report_dir = Path("reports")

col1, col2 = st.columns([2,1])

with col1:
    st.header("1. Global Data Ingestion")
    st.code("""
Vessels detected: 2
- CLEAROCEAN MERIBEL IMO 9917646 | 35.384N 15.655E | FOR ORDERS | Draught jump 6.6m
- GEA IMO 9292591 | 35.390N 15.660E | FOR ORDERS | Loitering 0.5 knots
    """, language="text")
    
    st.header("2. Agent 1: AIS Hunter Results")
    st.metric(label="MERIBEL Risk Score", value="100/100", delta="CRITICAL - Shadow Fleet")
    st.metric(label="GEA Risk Score", value="70/100", delta="HIGH - Loitering")
    st.json({
        "MERIBEL": {"loitering": True, "for_orders": True, "draught_jump_m": 6.6, "score": 100},
        "GEA": {"loitering": True, "for_orders": True, "draught_jump_m": 0.1, "score": 70}
    })

    st.header("3. Agent 2: SAR Verifier Results")
    if sar_path.exists():
        with open(sar_path) as f:
            sar_data = json.load(f)
        st.success(f"SAR Mode: {sar_data.get('mode','MOCK')} | Images Found: {sar_data.get('images_found',0)}")
        for det in sar_data.get("detections",[]):
            st.write(f"🛰️ SAR detection at {det['lat']},{det['lon']} - Size {det['size_m']}m - Brightness {det['radar_brightness']} - Matches {det['matched_ais']}")
    else:
        st.warning("Run agents/sar_real_api.py first to generate SAR data")
        st.write("Simulated SAR detections:")
        st.write("- 35.384,15.655 brightness 245 -> MERIBEL")
        st.write("- 35.390,15.660 brightness 210 -> GEA")

with col2:
    st.header("4. Governed AI Audit Log")
    if audit_path.exists():
        with open(audit_path) as f:
            logs = json.load(f)
        for log in logs[-5:]:
            st.text(f"{log['timestamp'][11:19]} {log['agent']}: {log['action']}")
        st.caption(f"Total audit entries: {len(logs)} - Full traceability")
    else:
        st.info("Run agentic_workflow_detailed.py to generate audit log")
        st.code("[AUDIT] AIS_Hunter -> Analyzed MERIBEL [AUDIT] SAR_Verifier -> SAR confirmed [AUDIT] Investigator -> Report ready", language="text")

    st.header("5. Decision-Ready Intelligence")
    reports = list(report_dir.glob("agentic_report_*.txt")) if report_dir.exists() else []
    if reports:
        for r in reports:
            with open(r) as f:
                content = f.read()
            st.text_area(f"Report {r.name}", content[:2000], height=300)
    else:
        st.warning("No final reports yet")
        st.code("""
UNCLASS // OSINT REPORT
VESSEL: CLEAROCEAN MERIBEL IMO 9917646
RISK: 100/100 CONFIDENCE: 85%
FINDING: Probable shadow fleet STS
ACTION: Flag, watchlist, notify Malta authorities
        """, language="text")

st.markdown("---")
st.markdown("**Platform:** Built with LangGraph pattern | **Governed AI:** Full audit log | **Classification:** UNCLASS // OSINT | **Author:** Mohanad Issa | **Portfolio:** github.com/Cyber404Man/Osint-portfolio")

# Footer
st.sidebar.markdown("---")
st.sidebar.markdown("### For Airbus Interview")
st.sidebar.markdown("Methodology aligns with OceanFinder STS detection")
st.sidebar.markdown("### For Upwork Client")
st.sidebar.markdown("This demo implements your spec: global data + governed agents + Insights Investigator")
