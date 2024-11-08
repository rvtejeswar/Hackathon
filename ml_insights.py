import numpy as np

def generate_ml_insights():
    # Mock ML model for generating insights
    data = np.random.randint(10, size=5)
    insights = {"suggested_offline_activities": ["Reading", "Board Games", "Outdoor Play"], "trend": data.tolist()}
    return insights
