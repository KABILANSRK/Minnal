from flask import Flask, jsonify
from flask_cors import CORS
from scrapper import data_fetch
import logging
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/')
def index():
    return jsonify({
        'status': 'alive',
        'message': 'Flask backend is running'
    })

@app.route('/api/schedule', methods=['GET'])
def get_schedule():
    logger.info('Received request for /api/schedule')
    try:
        logger.info('Attempting to fetch schedule data...')
        schedule_data = data_fetch()
        
        if schedule_data:
            logger.info(f'Schedule data fetched successfully: {schedule_data}')
            return jsonify({
                'success': True,
                'data': schedule_data
            })
        else:
            logger.warning('No schedule data found')
            return jsonify({
                'success': False,
                'message': 'No power cut schedule found for today.'
            }), 404
            
    except Exception as e:
        logger.error(f'Error occurred: {str(e)}')
        return jsonify({
            'success': False,
            'message': f'Internal server error: {str(e)}'
        }), 500


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0",debug=False)