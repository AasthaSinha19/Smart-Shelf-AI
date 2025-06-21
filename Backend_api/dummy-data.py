# ---- dummy_data.py ----

import random
from datetime import datetime, timedelta

def get_dummy_alerts():
    data = [
        {"title": "Port Strike Affects Food Imports", "risk_level": "High", "risk_percent": 85, "source": "Reuters", "disruption_days": 7},
        {"title": "Heavy Rainfall Delays Transportation in Assam", "risk_level": "Medium", "risk_percent": 55, "source": "NDTV", "disruption_days": 4},
        {"title": "Milk Supply Shortage Due to Heatwave", "risk_level": "High", "risk_percent": 90, "source": "BBC", "disruption_days": 6},
        {"title": "Labor Protest Halts Logistics at Warehouse X", "risk_level": "High", "risk_percent": 75, "source": "India Today", "disruption_days": 5},
        {"title": "Packaging Raw Material Unavailable in Gujarat", "risk_level": "Low", "risk_percent": 20, "source": "Times of India", "disruption_days": 2},
        {"title": "Container Congestion at Nhava Sheva Port", "risk_level": "Medium", "risk_percent": 60, "source": "Economic Times", "disruption_days": 5},
        {"title": "Rice Export Ban Causes Shelf Shortages", "risk_level": "High", "risk_percent": 80, "source": "Mint", "disruption_days": 10},
        {"title": "Truckers Strike in Maharashtra Impacts FMCG", "risk_level": "Medium", "risk_percent": 50, "source": "The Hindu", "disruption_days": 3},
        {"title": "Power Outages Slow Down Cold Storage", "risk_level": "Medium", "risk_percent": 45, "source": "Scroll.in", "disruption_days": 2},
        {"title": "Shortage of Skilled Labor in Packaging Units", "risk_level": "Low", "risk_percent": 25, "source": "Hindustan Times", "disruption_days": 1}
    ]
    return random.sample(data, 5)

def get_dummy_trending():
    products = [
        {"topic": "Organic Milk", "trend_score": 82, "intensity": "High", "source": "Google Trends"},
        {"topic": "Coconut Water", "trend_score": 76, "intensity": "High", "source": "Twitter"},
        {"topic": "Gluten-Free Bread", "trend_score": 67, "intensity": "High", "source": "Google Trends"},
        {"topic": "Energy Drinks", "trend_score": 58, "intensity": "Medium", "source": "Reddit"},
        {"topic": "Plant-Based Meat", "trend_score": 71, "intensity": "High", "source": "YouTube"},
        {"topic": "Cold Coffee Bottles", "trend_score": 48, "intensity": "Medium", "source": "Google Trends"},
        {"topic": "Protein Shakes", "trend_score": 64, "intensity": "Medium", "source": "Instagram"},
        {"topic": "Chocolate Cookies", "trend_score": 37, "intensity": "Low", "source": "Facebook"},
        {"topic": "Almond Butter", "trend_score": 53, "intensity": "Medium", "source": "Twitter"},
        {"topic": "Oatmeal Packets", "trend_score": 30, "intensity": "Low", "source": "Pinterest"}
    ]
    return random.sample(products, 5)
