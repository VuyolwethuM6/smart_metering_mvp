from flask import Flask, request, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Initialize the database
def init_db():
    conn = sqlite3.connect('usage_data.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS usage_data (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        meter_id TEXT NOT NULL,
                        usage REAL NOT NULL,
                        timestamp TEXT NOT NULL)''')
    conn.commit()
    conn.close()

@app.route('/data', methods=['POST'])
def receive_data():
    data = request.json
    meter_id = data['meter_id']
    usage = data['usage']
    timestamp = data['timestamp']
    
    conn = sqlite3.connect('usage_data.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usage_data (meter_id, usage, timestamp) VALUES (?, ?, ?)",
                   (meter_id, usage, timestamp))
    conn.commit()
    conn.close()
    
    return jsonify({"status": "success"}), 200

@app.route('/usage', methods=['GET'])
def get_usage():
    conn = sqlite3.connect('usage_data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usage_data")
    rows = cursor.fetchall()
    conn.close()
    
    usage_data = [{"meter_id": row[1], "usage": row[2], "timestamp": row[3]} for row in rows]
    return jsonify(usage_data)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
