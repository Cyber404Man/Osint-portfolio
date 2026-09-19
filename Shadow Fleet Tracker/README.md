# Shadow Fleet Tracker - Agentic Risk Intelligence Platform
Author: Mohanad Issa | OSINT / Maritime Intelligence
Portfolio Project #3 - Airbus OceanFinder Methodology

## Overview
This project builds a mini version of the Agentic Risk Intelligence Platform requested by the Upwork client.
It combines: Global Data + Governed AI Agents + Insights Investigator to deliver decision-ready intelligence at mission speed.

## Glossary - Every Term Explained

**AIS (Automatic Identification System):** GPS-like device every large vessel must broadcast. Sends every minute: who I am, where I am, where I am going, cargo status. Legally required.

**IMO Number:** Unique 7-digit vessel ID, never changes even if name or flag changes. Like passport number. Example: MERIBEL IMO 9917646

**MMSI:** ID of the AIS device itself.

**Draught / Draft:** How deep vessel sits in water. Empty = 5m, fully loaded with oil = 12m. Sudden jump from 5m to 12m in open sea = loaded oil via illegal STS.

**LOITERING:** Vessel moving <1 knot or stationary in open sea for >6 hours without nearby port. 90% probability it is doing STS (Ship-to-Ship Transfer).

**FOR ORDERS:** Captain writes destination as "FOR ORDERS" meaning "waiting for smuggler instructions". Normal vessels write "Rotterdam". FOR ORDERS is classic shadow fleet indicator.

**SAR (Synthetic Aperture Radar):** Satellite radar imaging. Sees through clouds, at night, in storms. Vessels cannot hide from SAR even if they turn off AIS. White dots on SAR image = ships.

**Dark Target:** Target seen on SAR image but NOT on AIS map = vessel turned off its device intentionally = strong evidence of illicit activity. Core of Airbus OceanFinder.

**STS (Ship-to-Ship Transfer):** Moving cargo from one ship to another in open sea. Can be legal or illegal (to hide oil origin).

**Shadow Fleet / Dark Fleet:** 600+ old tankers bought by Russia/Iran via shell companies to evade sanctions. Age >20 years, no insurance.

**Agentic Workflow:** Not a simple chatbot. An Agent has a goal and plans by itself. Example: Tell agent "find smuggling vessel near Malta" and it will: query MarineTraffic, check if AIS off, fetch Sentinel-1 image, compare, write report.

**Multi-Agent System:** 3 specialized agents working together via LangGraph.

**Governed AI:** Every AI action is logged: who saw what vessel, when, confidence level. Audit log for compliance. Critical for Risk Intelligence platforms.

**Knowledge Graph (Neo4j):** Stores relationships, not just rows. Example: Vessel X owned by Company Y -> Company Y under sanctions -> Company Y sent 5 vessels to Libya -> Vessel X suspicious. AI understands connections.

**Decision-Ready Intelligence:** Instead of 1000 lines of raw data, give client one sentence: "85% probability vessel MERIBEL is smuggling off Malta, evidence is SAR image dated X, recommended action: notify Maltese authorities."

**Mission Speed:** Deliver intelligence in minutes, not days.

## Architecture

[Global Data: AIS + SAR + News + Sanctions] 
   -> Agent 1: AIS Hunter (detects loitering, FOR ORDERS, draught jump)
   -> Agent 2: SAR Verifier (compares AIS vs SAR, finds dark targets)
   -> Agent 3: Insights Investigator (builds graph + writes UNCLASS report)

## Project Structure
- agents/ais_hunter.py : Detect loitering and draught anomalies, calculates risk score 0-100
- agents/sar_verifier.py : Compare AIS positions with SAR detections
- agents/investigator.py : Generate final intelligence report
- data/sample_ais.json : Sample data from real suspicious vessels SE Malta
- data/ais_analysis.json : Output of Agent 1
- reports/ : Final UNCLASS reports

## How to Run
python agents/ais_hunter.py
python agents/sar_verifier.py
python agents/investigator.py

## Next Step: Upgrade to Real Agentic Platform
- Replace mock SAR with Sentinel Hub API
- Replace mock AIS with MarineTraffic API
- Orchestrate with LangGraph
- Store relationships in Neo4j
- Add audit logging

This project is UNCLASS // OSINT only, uses public data.


## STEP 2: Agentic Version (NEW)

We upgraded from simple scripts to a true Agentic Platform using LangGraph pattern.

### What is LangGraph?
- StateGraph: shared memory (InvestigationState)
- Nodes: each agent is a node (ais_hunter_node, sar_verifier_node, investigator_node)
- Edges: agents talk in sequence
- Governed: every action logged in audit_log

### How to run agentic version:
```
pip install -r requirements.txt
python agents/agentic_workflow.py
```

Output:
- data/governed_audit_log.json -> Full audit trail for compliance
- reports/agentic_report_*.txt -> Decision-ready intelligence reports

This is the exact architecture the Upwork client asked for:
"combines global data, governed AI agents, and Insights Investigator"

### Output:
1. Show audit_log.json -> proves governed AI
2. Show final report -> proves decision-ready intelligence
3. Show InvestigationState -> proves global data fusion

Next: You can Add real Sentinel-1 API and MarineTraffic API to replace mock data.
