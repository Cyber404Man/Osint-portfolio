"""
Agent 1: AIS Hunter
Purpose: Hunt suspicious vessels from AIS data
Calculates risk score 0-100 based on 3 indicators
"""

import json
from pathlib import Path

# Sample data - 3 vessels from SE Malta area - same area as your first report
sample_vessels = [
    {
        "name": "CLEAROCEAN MERIBEL",
        "imo": 9917646,
        "mmsi": 538010279,
        "last_position": {"lat": 35.384, "lon": 15.655, "timestamp": "2026-09-16T08:30:00Z"},
        "speed_knots": 0.8,  # <1 knot = stationary
        "destination": "FOR ORDERS",  # Suspicious
        "draught_history": [5.2, 5.3, 11.8],  # Sudden increase = loaded oil
        "status": "loitering"
    },
    {
        "name": "GEA",
        "imo": 9292591,
        "mmsi": 247389900,
        "last_position": {"lat": 35.390, "lon": 15.660, "timestamp": "2026-09-16T08:32:00Z"},
        "speed_knots": 0.5,
        "destination": "FOR ORDERS",
        "draught_history": [6.0, 6.1, 6.0],
        "status": "loitering"
    },
    {
        "name": "NORMAL TANKER",
        "imo": 1234567,
        "mmsi": 123456789,
        "last_position": {"lat": 36.0, "lon": 14.0, "timestamp": "2026-09-16T08:00:00Z"},
        "speed_knots": 12.5,  # Normal cruising
        "destination": "Rotterdam",  # Clear destination = normal
        "draught_history": [8.0, 8.0, 8.0],
        "status": "underway"
    }
]

def detect_loitering(vessel):
    """Detect LOITERING: speed <1 knot in open sea"""
    if vessel["speed_knots"] < 1.0 and vessel["status"] == "loitering":
        return True, f"Loitering detected: vessel {vessel['name']} stationary at {vessel['speed_knots']} knots - probable STS"
    return False, "Normal movement"

def detect_for_orders(vessel):
    """Detect FOR ORDERS destination - classic shadow fleet tactic"""
    if "FOR ORDERS" in vessel["destination"].upper():
        return True, f"Suspicious destination: {vessel['destination']} - legitimate vessels list port name"
    return False, "Normal destination"

def detect_draught_jump(vessel):
    """Detect sudden draught increase = loaded cargo at sea"""
    history = vessel["draught_history"]
    if len(history) < 2:
        return False, "Insufficient history"
    jump = history[-1] - history[0]
    if jump > 3.0:
        return True, f"Critical draught jump: from {history[0]}m to {history[-1]}m (delta {jump:.1f}m) = loaded oil at sea"
    return False, f"Draught stable: {history}"

def calculate_risk_score(vessel):
    """Calculate risk score 0-100. Each indicator adds points."""
    score = 0
    reasons = []
    
    is_loitering, reason_loit = detect_loitering(vessel)
    if is_loitering:
        score += 40
        reasons.append(reason_loit)
    
    is_for_orders, reason_orders = detect_for_orders(vessel)
    if is_for_orders:
        score += 30
        reasons.append(reason_orders)
    
    is_jump, reason_jump = detect_draught_jump(vessel)
    if is_jump:
        score += 30
        reasons.append(reason_jump)
    
    return score, reasons

# --- Run investigation ---
print("=== Agent 1: AIS Hunter Started ===")
results = []
for vessel in sample_vessels:
    score, reasons = calculate_risk_score(vessel)
    print(f"--- Vessel: {vessel['name']} (IMO {vessel['imo']}) ---")
    print(f"Risk Score: {score}/100")
    if score >= 70:
        print("HIGH RISK - Very suspicious")
    elif score >= 40:
        print("MEDIUM RISK - Needs monitoring")
    else:
        print("LOW RISK - Normal")
    for r in reasons:
        print(f"  - {r}")
    results.append({"name": vessel["name"], "imo": vessel["imo"], "risk_score": score, "reasons": reasons})

# Save results for next agents
output_path = Path(__file__).parent.parent / "data" / "ais_analysis.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2)
print(f"Results saved to {output_path}")
