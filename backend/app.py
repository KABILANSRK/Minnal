from flask import Flask, jsonify
from flask_cors import CORS
from scrapper import data_fetch
import logging
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/api/schedule', methods=['GET'])
def get_schedule():
    try:
        schedule_data = data_fetch()
        
        if schedule_data:
            return jsonify({
                'success': True,
                'data': schedule_data
            })
        else:
            return jsonify({
                'success': False,
                'message': 'No power cut schedule found for today.'
            }), 404
            
    except Exception as e:
        return jsonify({
            'success': False,
            'message': 'Internal server error'
        }), 500


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0",debug=False)