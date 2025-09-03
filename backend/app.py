from flask import Flask, jsonify
from flask_cors import CORS
from scrapper import powercut_info
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)

@app.route('/api/schedule', methods=['GET'])
def get_schedule():
    logger.info("API endpoint /api/schedule was called")
    
    try:
        schedule_data = powercut_info()
        
        if schedule_data:
            logger.info("Successfully retrieved power cut schedule")
            return jsonify({
                'success': True,
                'data': schedule_data
            })
        else:
            logger.info("No power cut schedule found")
            return jsonify({
                'success': False,
                'message': 'No power cut schedule found for today or tomorrow.'
            }), 404
            
    except Exception as e:
        logger.error(f"Error retrieving power cut schedule: {str(e)}")
        return jsonify({
            'success': False,
            'message': 'Internal server error'
        }), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)