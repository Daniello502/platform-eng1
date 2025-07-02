from flask import Flask, jsonify
import datetime
import socket

app = Flask(__name__)

@app.route('/api/v1/details')

def get_details():
    details = {
        'hostname': socket.gethostname(),
        'current_time': datetime.datetime.now().isoformat()
    }
    return jsonify(details)

@app.route('/api/v1/health')

def health_check():
    return jsonify({'status': 'healthy'}), 200  

if __name__ == '__main__':
    app.run(host="0.0.0.0") 