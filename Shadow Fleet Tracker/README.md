# Shadow Fleet Tracker - Agentic Risk Intelligence Platform
### OSINT Portfolio Project 3 | By Mohanad Issa

> **Live Demo:** `streamlit run app.py`
> **Status:** v2.0 Agentic Platform Complete - Governed AI Enabled

[Architecture](architecture.png)

## What is this?

A multi-agent platform that detects shadow fleet STS operations (ship-to-ship oil transfers) SE Malta, combining:

- **Global Data:** AIS (MarineTraffic) + SAR Satellite (Sentinel-1 Copernicus) + Sanctions Lists
- **Governed AI Agents:** 3 agents with full audit log (timestamp, confidence, details)
- **Insights Investigator:** Fuses evidence and generates decision-ready UNCLASS reports

This matches the exact spec from Upwork client: "combines global data, governed AI agents, and Insights Investigator to deliver decision-ready intelligence at mission speed"

And aligns with Airbus Defence and Space OceanFinder methodology.

## Quick Start (3 minutes)

```bash
# 1. Clone
git clone https://github.com/Cyber404Man/Osint-portfolio
cd Osint-portfolio/Shadow\ Fleet\ Tracker

# 2. Install
pip install -r requirements.txt

# 3. Run Agentic Workflow (Mock mode works without credentials)
python agents/agentic_workflow_detailed.py

# 4. Run Real SAR API (optional - needs free Copernicus account)
cp .env.example .env
# Edit .env with your Copernicus email/password
python agents/sar_real_api.py

# 5. Launch Dashboard
streamlit run app.py
```

## Architecture - LangGraph Pattern

```
Global Data (AIS + SAR + News)
        |
        v
[AIS Hunter Node] -> Risk Score 0-100, detects loitering, FOR ORDERS, draught jump
        |               logs to audit_log
        v
[SAR Verifier Node] -> Confirms with Sentinel-1 radar, detects dark targets
        |               logs to audit_log
        v
[Investigator Node] -> Fuses AIS+SAR, calculates confidence, generates UNCLASS report
        |               includes audit trail
        v
Decision-Ready Intelligence + Governed Audit Log
```

**State:** InvestigationState (shared memory)
**Nodes:** 3 agents
**Edges:** AIS -> SAR -> Investigator
**Governed:** log_audit() every action

## Project Structure

```
Shadow Fleet Tracker/
├── app.py                              # Streamlit live dashboard
├── agents/
│   ├── ais_hunter.py                   # Agent 1 - Simple version
│   ├── sar_verifier.py                 # Agent 2 - Simple version
│   ├── investigator.py                 # Agent 3 - Simple version
│   ├── agentic_workflow.py             # Agentic v2 - Short version
│   ├── agentic_workflow_detailed.py    # Agentic v2 - Detailed with comments
│   └── sar_real_api.py                 # Real Sentinel-1 Copernicus integration
├── data/
│   ├── sample_ais.json                 # Input vessels (MERIBEL, GEA)
│   ├── ais_analysis.json               # Agent 1 output
│   ├── sar_real_analysis.json          # Agent 2 output (real + mock)
│   └── governed_audit_log.json         # Governed AI audit trail
├── reports/
│   ├── report_9917646.txt              # Simple report
│   └── agentic_report_9917646.txt      # Decision-ready report with audit
├── .env.example                        # Template for credentials
├── .gitignore                          # Blocks .env
├── requirements.txt
└── README.md
```

## Agents Explained

### Agent 1: AIS Hunter
- **Detects:** Loitering (<1 knot), FOR ORDERS destination, Draught jump >3m
- **Physics:** Draught 5m empty, 12m full, jump at sea = loaded illegally
- **Output:** Risk score 0-100
- **Audit:** Logs every vessel analyzed

### Agent 2: SAR Verifier
- **What is SAR?** Synthetic Aperture Radar - sees at night, through clouds, ships are bright
- **Real API:** Copernicus Dataspace OData API, Sentinel-1 GRD product, polygon search
- **Detects:** SAR confirms AIS, or Dark Target (SAR sees ship, AIS doesn't = hiding)
- **Resilient:** Works in REAL mode with credentials, auto fallback to MOCK for CI/CD
- **Audit:** Logs every SAR detection with image ID

### Agent 3: Insights Investigator
- **Fuses:** AIS + SAR + Audit log
- **Generates:** UNCLASS intelligence report with Executive Summary, Indicators, SAR Correlation, Audit Trail, Recommendation
- **Decision-ready:** Client can act immediately

## Governed AI - Why it matters

Without audit log: "AI says ship is smuggling" -> not trustworthy
With audit log:
```
[2026-09-16T08:30:00] AIS_Hunter: Analyzed MERIBEL - Risk 100 - LOITERING
[2026-09-16T08:31:00] SAR_Verifier: SAR confirmed at 35.384,15.655 brightness 245
[2026-09-16T08:32:00] Investigator: Generated report - Confidence 85%
```
-> Full traceability for compliance, court, sanctions.

## Results

- Detected: CLEAROCEAN MERIBEL IMO 9917646 + GEA IMO 9292591
- Location: SE Malta 35.38N 15.65E
- Pattern: Libyan STS corridor, loitering, FOR ORDERS
- Confidence: 85% (AIS + SAR confirmed)
- Reports: reports/agentic_report_*.txt
- Audit: data/governed_audit_log.json

## For Airbus Interview

Q: What is Agentic?
A: Multi-agent system using LangGraph pattern with 3 nodes sharing InvestigationState, each logs to audit log for governance. Methodology aligns with OceanFinder STS detection but adds governed AI.

Q: Have you worked with satellite imagery?
A: Yes, integrated Copernicus Dataspace API to fetch Sentinel-1 GRD for SE Malta AOI, using OData polygon search and OpenID token auth, detects ships by radar brightness.

## For Upwork Client

This repo is a working demo of your spec:
- Global data: MarineTraffic + Sentinel-1 + News (mock + real)
- Governed AI agents: 3 agents + audit_log.json
- Insights Investigator: investigator_node()
- Decision-ready: UNCLASS reports with recommendation

Deploy dashboard free: streamlit cloud, share link with client.

## Deployment

Streamlit Cloud (free):
1. Push to GitHub
2. Go to share.streamlit.io, connect repo, select app.py
3. Live demo link ready to send to client

## License

UNCLASS // OSINT - Public data only (AIS + Open SAR)
All analysis uses open sources, no classified data.

Author: Mohanad Issa - Aspiring Intelligence Analyst
GitHub: Cyber404Man
Location: Gaza, EMEA GMT+3
