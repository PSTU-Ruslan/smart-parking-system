"""
Configuration for Smart Parking System
"""

# Parking lot configuration
PARKING_SPOTS = [
    {"id": 1, "name": "A1", "coords": [100, 100, 200, 200], "type": "standard"},
    {"id": 2, "name": "A2", "coords": [250, 100, 350, 200], "type": "standard"},
    {"id": 3, "name": "A3", "coords": [400, 100, 500, 200], "type": "standard"},
    {"id": 4, "name": "B1", "coords": [100, 300, 200, 400], "type": "disabled"},
    {"id": 5, "name": "B2", "coords": [250, 300, 350, 400], "type": "standard"},
]

# Video source configuration
VIDEO_SOURCE = "data/samples/parking_sample.mp4"  # или 0 для веб-камеры
USE_WEBCAM = False

# Detection settings
DETECTION_CONFIDENCE = 0.6
UPDATE_INTERVAL = 2  # seconds

# Web interface
WEB_HOST = "0.0.0.0"
WEB_PORT = 5000
DEBUG_MODE = True
