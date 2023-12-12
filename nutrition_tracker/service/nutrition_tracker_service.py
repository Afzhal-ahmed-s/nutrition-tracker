from nutrition_tracker.repository import food_nutrition_repository
from nutrition_tracker.repository.food_nutrition_repository import output_format_with_units, output_format_without_units
from nutrition_tracker.enums.serving_enum import Serving_Enum as serving
import copy
import re
from nutrition_tracker.service.nutrition_tracker_interface import NutritionTrackerInterface


class NutritionalValue(NutritionTrackerInterface):
    def __init__(self):
        self.food_data = food_nutrition_repository.food_data

    def calculate_nutritional_value_for_single_food(self, food_name, quantity, serving_type=None):
        # Find the food item based on the given food_name
        food_item = next((item for item in self.food_data if item['food_name'] == food_name), None)

        if food_item is not None:
            # Extract the per serving or per piece value based on the serving_type
            if serving_type is None:
                serving_type = serving.PER_100_GRAMS
            else:
                serving_type = self.give_me_serving_enum_in_return_for_string(serving_type)

            if serving_type == serving.PER_SERVING:
                per_serving = float(food_item['data']['quantity'])
            elif serving_type == serving.PER_PIECE:
                per_piece = float(food_item['data']['quantity'])
            elif serving_type == serving.PER_100_GRAMS:
                per_100_grams = float(food_item['data']['quantity'])
            else:
                raise ValueError("Invalid serving type")

            nutritional_values = food_item['data'].copy()  # Make a copy of the original data

            # Multiply the values by the given quantity
            for key, value in nutritional_values.items():
                if isinstance(value, (int, float)):
                    if serving_type == serving.PER_SERVING:
                        nutritional_values[key] = value * (quantity / per_serving)
                    elif serving_type == serving.PER_PIECE:
                        nutritional_values[key] = value * (quantity / per_piece)
                    elif serving_type == serving.PER_100_GRAMS:
                        nutritional_values[key] = value * (quantity / per_100_grams)
            return nutritional_values
        else:
            return food_name + " is not available in the repository."

    def calculate_nutritional_value_for_a_meal(self, list_of_a_food_item_detail):
        # list_of_food_and_quantity_with_units = self.add_units_to_food_list(list_of_a_food_item_detail)
        local_operation_end_data = copy.deepcopy(output_format_without_units)

        foods_not_available = []
        for i in list_of_a_food_item_detail:
            food_name = i[0]
            quantity = i[1]
            if len(i) > 2:
                serving_type = i[2]
                single_food_data = self.calculate_nutritional_value_for_single_food(food_name,
                                                                                    quantity,
                                                                                    serving_type)

            else:
                single_food_data = self.calculate_nutritional_value_for_single_food(food_name,
                                                                                    quantity)
            if isinstance(single_food_data, str):
                foods_not_available.append(single_food_data)
            else:
                local_operation_end_data = self.add_up_data_to_desired_format(local_operation_end_data,
                                                                              single_food_data)

        rounded_off_data = self.value_round_off(local_operation_end_data, 2)
        nutritional_meal_data_without_units = copy.deepcopy(rounded_off_data)
        final_data_with_units = self.append_units_to_data(rounded_off_data, output_format_with_units)

        return [list_of_a_food_item_detail, final_data_with_units,
                foods_not_available, nutritional_meal_data_without_units]

        # return [list_of_food_and_quantity_with_units, final_data_with_units, foods_not_available]

    def calculate_nutritional_value_for_multiple_meals(self, mega_list_data):
        nutritional_data_of_multiple_meals = []
        meal_number = 1

        for i in mega_list_data:

            single_meals_nutritional_data = self.calculate_nutritional_value_for_a_meal(i)

            nutritional_data_of_multiple_meals.append("MEAL NUMBER: " + str(meal_number))
            meal_number += 1
            nutritional_data_of_multiple_meals.append(single_meals_nutritional_data)
        return nutritional_data_of_multiple_meals

    def add_up_data_to_desired_format(self, final_data, data_dict):
        for key, value in final_data.items():
            if isinstance(value, dict):
                if key in data_dict and isinstance(data_dict[key], dict):
                    self.add_up_data_to_desired_format(final_data[key], data_dict[key])
            elif isinstance(value, (int, float)):
                if key in data_dict and isinstance(data_dict[key], (int, float)):
                    data_dict[key] = round(float(data_dict[key]), 2)
                    final_data[key] += data_dict[key]  # Use addition to accumulate values

        return final_data

    def value_round_off(self, data, places):
        if isinstance(data, int) or isinstance(data, float):
            return round(data, places)
        elif isinstance(data, dict):
            for key, value in data.items():
                data[key] = self.value_round_off(value, places)
            return data
        elif isinstance(data, list):
            return [self.value_round_off(item, places) for item in data]
        else:
            return data

    def append_units_to_data(self, data, units):
        # processed_data = data.copy()
        processed_data = data

        for key, value in processed_data.items():
            if isinstance(value, dict):
                # Recursively process nested dictionaries
                processed_data[key] = self.append_units_to_data(value, units.get(key, {}))
            elif key in units:
                # If the key has a unit, append it
                unit = units[key]
                processed_data[key] = f"{value} {unit}"

        return processed_data

    def add_up_nutritional_data_without_units_for_a_day(self, raw_list_of_nutritional_dictionaries):
        days_nutritional_data_without_units = copy.deepcopy(output_format_without_units)

        for i in raw_list_of_nutritional_dictionaries:
            days_nutritional_data_without_units = self.add_up_data_to_desired_format(days_nutritional_data_without_units,
                                               i)

        return days_nutritional_data_without_units

    def print_a_days_nutritional_data_split_into_meals(self, raw_data):
        # raw_per_day_nutritional_information = []

        for i in range(0, len(raw_data), 2):
            meal_number = raw_data[i]
            ingredients_and_nutrition = raw_data[i + 1]

            # Process meal_number (e.g., 'MEAL NUMBER: 1')
            print(meal_number)

            # Process ingredients_and_nutrition, which is a list with two elements
            ingredients = ingredients_and_nutrition[0]
            nutrition = ingredients_and_nutrition[1]

            # Process ingredients and nutrition information
            for ingredient in ingredients:
                # Process ingredient data (e.g., ['dates', 17.0])
                ingredient_name, quantity = ingredient
                print(f"Ingredient: {ingredient_name}, Quantity: {quantity}")

            # Process nutrition information
            print("Nutrition Information: ", nutrition)

            if len(ingredients_and_nutrition[2]) > 0:
                # Handle messages like "['test1 is not available in the repository.']"
                message = ingredients_and_nutrition[2]
                print("Message:", message)
            print("\n")

            # print("Raw data: ",ingredients_and_nutrition[3], "\n")
            # raw_per_day_nutritional_information.append(ingredients_and_nutrition[3])

            # print(raw_per_day_nutritional_information)

    def serve_a_days_nutritional_data_split_into_meals_as_data_with_units(self, raw_data):
        raw_per_day_nutritional_information_per_meals_basis_with_units = []

        for i in range(0, len(raw_data), 2):
            meal_number = raw_data[i]
            ingredients_and_nutrition = raw_data[i + 1]

            # Process meal_number (e.g., 'MEAL NUMBER: 1')
            raw_per_day_nutritional_information_per_meals_basis_with_units.append(meal_number)

            # Process ingredients_and_nutrition, which is a list with two elements
            ingredients = ingredients_and_nutrition[0]
            nutrition = ingredients_and_nutrition[1]

            local_food_item_quantity = []
            # Process ingredients and nutrition information
            for ingredient in ingredients:
                # Process ingredient data (e.g., ['dates', 17.0])
                ingredient_name, quantity = ingredient
                local_food_item_quantity.append(f"Ingredient: {ingredient_name}, Quantity: {quantity}")

            raw_per_day_nutritional_information_per_meals_basis_with_units.append(local_food_item_quantity)

            # Process nutrition information
            ni = "Nutrition Information: ", nutrition
            raw_per_day_nutritional_information_per_meals_basis_with_units.append(ni)

            if len(ingredients_and_nutrition[2]) > 0:
                # Handle messages like "['test1 is not available in the repository.']"
                message = ingredients_and_nutrition[2]
                m = "Message:", message
                raw_per_day_nutritional_information_per_meals_basis_with_units.append(m)

        return raw_per_day_nutritional_information_per_meals_basis_with_units

    def get_raw_nutritional_data_of_meals_in_a_day(self, ultimate_data_compiled):
        raw_per_day_nutritional_information = []

        for i in range(0, len(ultimate_data_compiled), 2):
            meal_number = ultimate_data_compiled[i]
            ingredients_and_nutrition = ultimate_data_compiled[i + 1]

            # Process meal_number (e.g., 'MEAL NUMBER: 1')

            # Process ingredients_and_nutrition, which is a list with two elements
            ingredients = ingredients_and_nutrition[0]
            # nutrition = ingredients_and_nutrition[1]

            # Process ingredients and nutrition information
            for ingredient in ingredients:
                # Process ingredient data (e.g., ['dates', 17.0])
                ingredient_name, quantity = ingredient

            # Process nutrition information

            # if len(ingredients_and_nutrition[2]) > 0:
            #     # Handle messages like "['test1 is not available in the repository.']"
            #     message = ingredients_and_nutrition[2]

            raw_per_day_nutritional_information.append(ingredients_and_nutrition[3])

            # print(raw_per_day_nutritional_information)
        return raw_per_day_nutritional_information

    # def get_raw_nutritional_data_of_meals_in_a_day(self, ultimate_data_compiled):
    #     raw_per_day_nutritional_information = []
    #
    #     for i in range(0, len(ultimate_data_compiled), 2):
    #         meal_number = ultimate_data_compiled[i]
    #         meal_data = ultimate_data_compiled[i + 1]
    #
    #         ingredients = meal_data[0]
    #         nutrition = meal_data[1]
    #         messages = meal_data[2]
    #
    #         # Process ingredients
    #         processed_ingredients = []
    #         for ingredient_info in ingredients:
    #             if len(ingredient_info) == 3:
    #                 ingredient_name, quantity, unit = ingredient_info
    #                 # Process the ingredient name, quantity, and unit here
    #                 processed_ingredients.append({
    #                     'name': ingredient_name,
    #                     'quantity': quantity,
    #                     'unit': unit
    #                 })
    #             else:
    #                 # Handle invalid ingredient format
    #                 print(f"Skipping invalid ingredient format: {ingredient_info}")
    #
    #         # Process nutrition information
    #         # Handle messages if necessary
    #
    #         # Append processed data to raw_per_day_nutritional_information
    #         raw_per_day_nutritional_information.append({
    #             'meal_number': meal_number,
    #             'ingredients': processed_ingredients,
    #             'nutrition': nutrition,
    #             'messages': messages
    #         })
    #
    #     return raw_per_day_nutritional_information

    def add_units_to_food_list(self, list_of_food_and_quantity):
        # list_of_food_and_quantity = [['uncooked_oats', 100.0], ['test2', 12], ['on_gs_c', 1.0]]
        for i in list_of_food_and_quantity:
            food_item = next((item for item in self.food_data if item['food_name'] == i[0]), None)

            if food_item is not None:
                    if len(i) > 3:
                        temp = str(i[1]) + ' serving / piece'
                    else:
                        temp = str(i[1]) + ' grams'

                        i[1] = temp

        return list_of_food_and_quantity

    def process_measurement_unit(self, unit):
        # Lowercase the string
        unit = unit.lower()

        # Check if the string is 'gram' and convert it to 'g'
        if unit == 'gram':
            unit = 'g'
        # Check if the string ends with 's' and remove it if it does
        elif unit.endswith('s'):
            unit = unit[:-1]

        return unit

    def give_me_serving_enum_in_return_for_string(self, unit_in_string):
        if unit_in_string == 'g' or 'gram' or 'grams':
            return serving.PER_100_GRAMS
        elif unit_in_string == 'piece' or 'pieces':
            return serving.PER_PIECE
        elif unit_in_string == 'serving' or 'servings':
            return serving.PER_SERVING
        else:
            return None

    def return_quantity_as_number_from_a_string_combination(self, data):
        match = re.match(r'(\d*\.?\d+)([a-zA-Z]*)', data)
        if match:
            numeric_part, non_numeric_part = match.groups()
            # print(f"Original: {s}, Numeric: {numeric_part}, Non-Numeric: {non_numeric_part}")
            return (float(numeric_part))

    def parse_text_data_to_desired_initial_input_format(self, text_data):
        raw_data_list = text_data.split("\n")
        # print("c1", raw_data_list)

        list_data_by_meals = []

        for i in raw_data_list:
            temporary = []
            temporary.append(i)
            list_data_by_meals.append(temporary)
        # print("c2", list_data_by_meals)

        list_data_by_meals_food = []

        for i in list_data_by_meals:
            list_data_by_meals_food.append(i[0].strip().split(","))
        # print("c3", list_data_by_meals_food)

        list_data_by_meals_food_quantity = []

        for i in list_data_by_meals_food:
            outer = []

            for j in i:
                local = []
                temp = (j.strip().split(" "))
                # print("debug ", temp)
                local.append(temp[0].lower())
                if len(temp) == 3:
                    local.append(float(temp[1]))
                    # local.append(temp[2])

                elif len(temp) == 2:
                    number_without_unit = self.return_quantity_as_number_from_a_string_combination(temp[1])
                    local.append(number_without_unit)
                    # local.append(temp[1])

                else:
                    local.append(1.0)
                outer.append(local)
            list_data_by_meals_food_quantity.append(outer)
        return (list_data_by_meals_food_quantity)

    def take_in_raw_user_text_data_serve_nutritional_data_split_into_meals_with_units_and_days_nutritional_data_with_units(
            self, raw_text_data, consolidated_data = True, raw_meal_wise_data = False, print_meal_wise_data_for_the_day = False):

        parsed_data = self.parse_text_data_to_desired_initial_input_format(raw_text_data)

        ultimate_result = self.calculate_nutritional_value_for_multiple_meals(parsed_data)

        raw_per_day_nutritional_information = self.get_raw_nutritional_data_of_meals_in_a_day(
            ultimate_result)
        days_nutritional_data_without_units = self.add_up_nutritional_data_without_units_for_a_day(
            raw_per_day_nutritional_information)
        days_nutritional_data_without_units_rounded_off = self.value_round_off(
            days_nutritional_data_without_units, 2)

        raw_days_nutritional_data_with_units_in_meals_basis = self.serve_a_days_nutritional_data_split_into_meals_as_data_with_units(
            ultimate_result)
        days_nutritional_data_with_units = (
            self.append_units_to_data(days_nutritional_data_without_units_rounded_off,
                                                   output_format_with_units))

        list_to_serve = []
        if consolidated_data:
           list_to_serve.append(days_nutritional_data_with_units)
        if raw_meal_wise_data:
            list_to_serve.append(raw_days_nutritional_data_with_units_in_meals_basis)
        if print_meal_wise_data_for_the_day:
            print("debug found", print_meal_wise_data_for_the_day)
            self.print_a_days_nutritional_data_split_into_meals(ultimate_result)

        return list_to_serve

    def take_file_name_of_text_file_and_give_text_file(self, file_name):
        # file_path = '/Users/afzhalahmed/Documents/GitHub/nutrition-tracker/nutrition_tracker/assets/' + file_name
        file_path = file_name
        # from data in local system as text file
        with open(file_path, 'r') as file:
            text_file_content = file.read()
            return text_file_content

    def convert_request_to_boolean(self, one, two, three):
        one = one.lower()
        two = two.lower()
        three = three.lower()
        # print(one, two, three)

        ans = []
        if one == 'y' or one == 'true' or one == 'yes' or one == 't':
            ans.append(True)
        else:
            ans.append(False)

        if two == 'y' or two == 'true' or two == 'yes' or two == 't':
            ans.append(True)
        else:
            ans.append(False)

        if three == 'y' or three == 'true' or three == 'yes' or three == 't':
            ans.append(True)
        else:
            ans.append(False)

        return ans
