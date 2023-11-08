from service import nutrition_tracker_service
from enums.serving_enum import Serving_Enum as serving
import json
from repository.food_nutrition_repository import output_format_with_units

nutrition_tracker = nutrition_tracker_service.NutritionalValue()

# sample data
sample_data_for_a_meal_1 = [
    ["cooked_rice", 300],
    ["on_gs_c", 2, serving.PER_SERVING],
    ["yolk", 3],
    ["whole_boiled_egg", 10, serving.PER_PIECE],
    ["peanut_butter", 20],
    ["albumen", 3]
]

sample_data_for_a_meal_2 = [
    ["water", 2],
    ["peanut_butter", 30],
    ["honey", 100]
]

sample_data_for_a_meal_3 = [
    ["honey", 100]
]

sample_data_meals_for_a_day_1 = [
    [["cooked_rice", 300],
     ["on_gs_c", 2, serving.PER_SERVING],
     ["yolk", 3]],
    [["whole_boiled_egg", 10, serving.PER_PIECE],
     ["peanut_butter", 20],
     ["albumen", 3]]
]

sample_data_meals_for_a_day_2 = [
    [['dates', 17.0], ['milk', 200.0], ['banana', 150.0], ['honey', 10.0]],
    [['whole_egg', 4.0], ['albumen', 2.0], ['peanut_spinach_amla_salad_(medium)', 1.0], ['rice', 120.0]],
    [['oats', 30.0], ['on_gs_c', 1.0], ['peanut_butter', 20.0]],
    [['kodo_millet', 300.0], ['chicken', 100.0], ['curd', 50.0]],
    [['rice', 300.0], ['albumen', 6.0], ['yolk', 1.0]],
    [['chapati', 240.0], ['chicken', 100.0]],
    [['milk', 200.0]], [['water', 2.5]]
]

sample_data_meals_for_a_day_3 = [
    [['dates', 17.0], ['cow_milk', 200.0], ['banana', 150.0], ['test1', 12]],
    [['uncooked_oats', 100.0], ['test2', 12], ['on_gs_c', 1.0]],
    [['cow_milk', 200.0]],
    [['water', 2.5], ['honey', 100]]
]


# operations
single_food_data = (nutrition_tracker.calculate_nutritional_value_for_single_food("whole_boiled_egg", 2, serving.PER_PIECE))

result = nutrition_tracker.calculate_nutritional_value_for_a_meal(sample_data_for_a_meal_1)
result2 = nutrition_tracker.calculate_nutritional_value_for_a_meal(sample_data_for_a_meal_2)
result3 = nutrition_tracker.calculate_nutritional_value_for_a_meal(sample_data_for_a_meal_3)

ultimate_result = nutrition_tracker.calculate_nutritional_value_for_multiple_meals(sample_data_meals_for_a_day_3)
raw_per_day_nutritional_information = nutrition_tracker.get_raw_nutritional_data_of_meals_in_a_day(ultimate_result)
days_nutritional_data_without_units = nutrition_tracker.add_up_nutritional_data_without_units_for_a_day(raw_per_day_nutritional_information)
days_nutritional_data_without_units_rounded_off = nutrition_tracker.value_round_off(days_nutritional_data_without_units, 2)


# display
# print("Solo: ",single_food_data)
#
# print("Nutritional information without units for a meal: ", "\n", result[0], "\n", result[1])
# print("Nutritional information without units for a meal: ", "\n", result2[0], "\n", result2[1])
# print("Nutritional information without units for a meal: ", "\n", result3[0], "\n", result3[1])
# print("Nutritional information with units: ", result[1])
# print("Foods not available: ", result[2])

# print(ultimate_result)
nutrition_tracker.print_a_days_nutritional_data_split_into_meals(ultimate_result)
# print(days_nutritional_data_without_units, "\n")
# print(nutrition_tracker.append_units_to_data(days_nutritional_data_without_units_rounded_off, output_format_with_units))