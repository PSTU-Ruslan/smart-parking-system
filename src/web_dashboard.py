"""
Web dashboard for smart parking system
"""

from flask import Flask, render_template, jsonify
import json
from datetime import datetime

app = Flask(__name__)

# Глобальная переменная для хранения статуса
current_parking_status = []
parking_statistics = {}

@app.route('/')
def index():
    """Main dashboard page"""
    return render_template('index.html')

@app.route('/api/status')
def get_status():
    """API endpoint for parking status"""
    return jsonify({
        'status': current_parking_status,
        'statistics': parking_statistics,
        'timestamp': datetime.now().isoformat()
    })

@app.route('/api/statistics')
def get_statistics():
    """API endpoint for detailed statistics"""
    return jsonify(parking_statistics)

def update_web_data(status, stats):
    """Update data for web interface (вызывается из main loop)"""
    global current_parking_status, parking_statistics
    current_parking_status = status
    parking_statistics = stats

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
