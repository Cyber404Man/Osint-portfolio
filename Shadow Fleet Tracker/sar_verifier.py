"""
Agent 2: SAR Verifier
Purpose: Compare AIS data with SAR satellite image to find dark targets
"""

import math

def haversine(lat1, lon1, lat2, lon2):
    """Calculate distance between two points in km"""
    R = 6371  # Earth radius km
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat/2)**2 + math.cos(math.radians(lat1))*math.cos(math.radians(lat2))*math.sin(dlon/2)**2
    return 2 * R * math.asin(math.sqrt(a))

# Mock data: In real project, fetch from Sentinel-1
sar_detections = [
    {"lat": 35.384, "lon": 15.655, "size_meters": 180, "confidence": 0.95},
    {"lat": 35.390, "lon": 15.660, "size_meters": 120, "confidence": 0.92},
]

ais_positions = [
    {"name": "MERIBEL", "lat": 35.384, "lon": 15.655},
    {"name": "GEA", "lat": 35.390, "lon": 15.660},
]

print("=== Agent 2: SAR Verifier ===")
print("Comparing AIS vs SAR...")

for sar in sar_detections:
    matched = False
    for ais in ais_positions:
        dist_km = haversine(sar["lat"], sar["lon"], ais["lat"], ais["lon"])
        if dist_km < 0.5:  # Less than 500m = same vessel
            print(f"MATCH: SAR detected vessel at {sar['lat']},{sar['lon']} matches AIS vessel {ais['name']} - distance {dist_km*1000:.0f}m")
            matched = True
    if not matched:
        print(f"DARK TARGET ALERT! SAR found vessel at {sar['lat']},{sar['lon']} but NO AIS signal there! Hidden vessel!")

print("If DARK TARGET + LOITERING + FOR ORDERS = Strong evidence of illicit STS")
print("This is exactly what Airbus OceanFinder does.")
