import os
import logging
from flask import Flask, request, jsonify
from nutrition_tracker.service.nutrition_tracker_service import NutritionalValue


nutrition_tracker_service = NutritionalValue()

app = Flask(__name__)

# Set up logging
log_dir = '/Users/afzhalahmed/Documents/GitHub/nutrition-tracker/nutrition_tracker/logs'  # Replace with the path where you want to store logs
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

log_file_path = os.path.join(log_dir, 'app.log')
logging.basicConfig(filename=log_file_path, level=logging.DEBUG)

UPLOAD_FOLDER = '/Users/afzhalahmed/Documents/GitHub/nutrition-tracker/nutrition_tracker/assets/'  # Adjust this to the actual path where you want to save uploaded files
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# Enable CORS for all routes
@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS, POST, GET, PUT, DELETE'
    return response

@app.route('/serve_nutrition_data/<consolidated_data>/<raw_meal_wise_data>/<print_meal_wise_data_for_the_day>', methods=['POST'])
def process_nutrition_data(consolidated_data, raw_meal_wise_data, print_meal_wise_data_for_the_day):
    try:
        # Get the uploaded file from the request
        uploaded_file = request.files['file']
        # uploaded_file= request.data.decode('utf-8')

        # Ensure the directory specified in UPLOAD_FOLDER exists
        if not os.path.exists(app.config['UPLOAD_FOLDER']):
            os.makedirs(app.config['UPLOAD_FOLDER'])

        # Save the uploaded file to the specified folder
        file_path =  uploaded_file.filename
        uploaded_file.save(file_path)

        # Log file path for debugging
        app.logger.debug('Uploaded file saved to: %s', file_path)

        # Your logic to process the parameters, raw_data, and the uploaded file
        text_file = nutrition_tracker_service.take_file_name_of_text_file_and_give_text_file(file_path)
        request_booleans = nutrition_tracker_service.convert_request_to_boolean(consolidated_data, raw_meal_wise_data, print_meal_wise_data_for_the_day)

        ans = nutrition_tracker_service.take_in_raw_user_text_data_serve_nutritional_data_split_into_meals_with_units_and_days_nutritional_data_with_units(
            text_file, request_booleans[0], request_booleans[1], request_booleans[2])

        # Log the result for debugging
        app.logger.debug('Result: %s', ans)

        # Return the result as JSON
        response_data = {
            'code': 200,
            'message': 'Success',
            'result': ans
        }
        return jsonify(response_data), 200
    except Exception as e:
        # Log the error with traceback for more details
        app.logger.exception('Error processing nutrition data')
        response_data = {
            'code': 500,
            'message': 'Error',
            'error': str(e)
        }
        return jsonify(response_data), 500

# Dummy endpoint for testing
@app.route('/test', methods=['GET'])
def test_endpoint():
    app.logger.info('Testing the /test endpoint')
    return jsonify({'message': 'Dummy endpoint is working!'}), 200

if __name__ == '__main__':
    app.run(debug=True)

