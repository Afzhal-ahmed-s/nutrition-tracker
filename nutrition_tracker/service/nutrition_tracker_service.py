from repository import food_nutrition_repository
from repository.food_nutrition_repository import output_format_with_units, output_format_without_units
from enums.serving_enum import Serving_Enum as serving
import copy


class NutritionalValue:
    def __init__(self):
        self.food_data = food_nutrition_repository.food_data

    def calculate_nutritional_value_for_single_food(self, food_name, quantity, serving_type=None):
        # Find the food item based on the given food_name
        food_item = next((item for item in self.food_data if item['food_name'] == food_name), None)

        if food_item is not None:
            # Extract the per serving or per piece value based on the serving_type
            if serving_type is None:
                serving_type = serving.PER_100_GRAMS

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

            # print(food_name, nutritional_values)
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
            # print("debug lv3", food_name, quantity)
            if len(i) > 2:
                serving_type = i[2]
                single_food_data = self.calculate_nutritional_value_for_single_food(food_name,
                                                                                    quantity,
                                                                                    serving_type)

            else:
                single_food_data = self.calculate_nutritional_value_for_single_food(food_name,
                                                                                    quantity)
            # print("debug lv6", food_name, single_food_data)
            if isinstance(single_food_data, str):
                foods_not_available.append(single_food_data)
            else:
                # print("debug lv8", local_operation_end_data)
                local_operation_end_data = self.add_up_data_to_desired_format(local_operation_end_data,
                                                                              single_food_data)
                # print("debug lv7", local_operation_end_data)

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
            # print("debug lv1", i)

            single_meals_nutritional_data = self.calculate_nutritional_value_for_a_meal(i)
            # print("debug lv2",single_meals_nutritional_data)
            # nutritional_data_of_multiple_meals.append( single_meals_nutritional_data[0] )
            # nutritional_data_of_multiple_meals.append( single_meals_nutritional_data[2] )
            nutritional_data_of_multiple_meals.append("MEAL NUMBER: " + str(meal_number))
            meal_number += 1
            nutritional_data_of_multiple_meals.append(single_meals_nutritional_data)
        return nutritional_data_of_multiple_meals

    def add_up_data_to_desired_format(self, final_data, data_dict):
        for key, value in final_data.items():
            if isinstance(value, dict):
                if key in data_dict and isinstance(data_dict[key], dict):
                    # print("debug lv5",final_data[key])
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

        # print("days_nutritional_data_without_units: ", days_nutritional_data_without_units)
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
                print("Message:", message, "\n")

            # print("Raw data: ",ingredients_and_nutrition[3], "\n")
            # raw_per_day_nutritional_information.append(ingredients_and_nutrition[3])

            # print(raw_per_day_nutritional_information)

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

