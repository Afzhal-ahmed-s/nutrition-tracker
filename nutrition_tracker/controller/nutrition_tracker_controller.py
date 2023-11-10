import os

from flask import Flask, request, jsonify
import nutrition_tracker
from nutrition_tracker.service.nutrition_tracker_service import NutritionalValue

nutrition_tracker_service = NutritionalValue()

app = Flask(__name__)

# @app.route('/serve_nutrition_data/<consolidated_data>/<raw_meal_wise_data>/<print_meal_wise_data_for_the_day>', methods=['POST'])
# def process_nutrition_data(consolidated_data, raw_meal_wise_data, print_meal_wise_data_for_the_day):
#     try:
#         # Get the uploaded file from the request
#         uploaded_file = request.files['file']
#
#         # Save the uploaded file to a temporary location
#         path = "/Users/afzhalahmed/Documents/GitHub/nutrition-tracker/nutrition_tracker/assets/"
#         uploaded_file.save(path)
#
#         # Your logic to process the parameters, raw_data, and the uploaded file
#         text_file = nutrition_tracker_service.take_file_name_of_text_file_and_give_text_file(path)
#         request_booleans = nutrition_tracker_service.convert_request_to_boolean(consolidated_data, raw_meal_wise_data, print_meal_wise_data_for_the_day)
#         ans = nutrition_tracker_service.take_in_raw_user_text_data_serve_nutritional_data_split_into_meals_with_units_and_days_nutritional_data_with_units(
#             text_file, request_booleans[0], request_booleans[1], request_booleans[2])
#
#         # Return the result as JSON
#         return jsonify({'result': ans}), 200
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500


UPLOAD_FOLDER = '/Users/afzhalahmed/Documents/GitHub/nutrition-tracker/nutrition_tracker/assets/'  # Adjust this to the actual path where you want to save uploaded files
# UPLOAD_FOLDER = ""  # Adjust this to the actual path where you want to save uploaded files
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/serve_nutrition_data/<consolidated_data>/<raw_meal_wise_data>/<print_meal_wise_data_for_the_day>', methods=['POST'])
def process_nutrition_data(consolidated_data, raw_meal_wise_data, print_meal_wise_data_for_the_day):
    try:

        # Get the uploaded file from the request
        uploaded_file = request.files['file']

        # Ensure the directory specified in UPLOAD_FOLDER exists
        if not os.path.exists(app.config['UPLOAD_FOLDER']):
            os.makedirs(app.config['UPLOAD_FOLDER'])

        # Save the uploaded file to the specified folder
        file_path2 = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
        file_path = uploaded_file.filename
        uploaded_file.save(file_path)

        # Your logic to process the parameters, raw_data, and the uploaded file
        text_file = nutrition_tracker_service.take_file_name_of_text_file_and_give_text_file(file_path)
        request_booleans = nutrition_tracker_service.convert_request_to_boolean(consolidated_data, raw_meal_wise_data, print_meal_wise_data_for_the_day)
        print(request_booleans)
        ans = nutrition_tracker_service.take_in_raw_user_text_data_serve_nutritional_data_split_into_meals_with_units_and_days_nutritional_data_with_units(
            text_file, request_booleans[0], request_booleans[1], request_booleans[2])
        # Return the result as JSON
        return jsonify({'result': ans}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Dummy endpoint for testing
@app.route('/test', methods=['GET'])
def test_endpoint():
    return jsonify({'message': 'Dummy endpoint is working!'}), 200


if __name__ == '__main__':
    app.run(debug=True)
