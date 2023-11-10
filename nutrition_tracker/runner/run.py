from nutrition_tracker.enums.serving_enum import Serving_Enum as serving
from nutrition_tracker.service import nutrition_tracker_service


nutrition_tracker = nutrition_tracker_service.NutritionalValue()

print("*** This is git version *** \n")

raw_data_2 = """Dates 20 g, cow_Milk 200g, Banana 150g
Whole_boiled_egg 6, amla 60g, cooked_rice 240g
cow_milk 200g
cooked_rice 250g, cooked_chicken_normal_cut 100g, curd 40g
cooked_rice 310g, albumen 6, yolk 1
Wheat_dosa 400g, cooked_chicken_normal_cut 100g
cow_Milk 200g
Water 1L"""

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
    [['dates', 17.0], ['cow_milk', 200.0], ['banana', 150.0], ['honey', 10.0]],
    [['whole_egg', 4.0], ['albumen', 2.0], ['peanut_spinach_amla_salad_(medium)', 1.0], ['cooked_rice', 120.0]],
    [['oats', 30.0], ['on_gs_c', 1.0], ['peanut_butter', 20.0]],
    [['kodo_millet', 300.0], ['cooked_chicken_normal_cut', 100.0], ['curd', 50.0]],
    [['rice', 300.0], ['albumen', 6.0], ['yolk', 1.0]],
    [['cooked_wheat_chapati', 240.0], ['cooked_chicken_normal_cut', 100.0]],
    [['cow_milk', 200.0]], [['water', 2.5]]
]
sample_data_meals_for_a_day_3 = [
    [['dates', 17.0], ['cow_milk', 200.0], ['banana', 150.0], ['test1', 12]],
    [['uncooked_oats', 100.0], ['test2', 12], ['on_gs_c', 1.0]],
    [['cow_milk', 200.0]],
    [['water', 2.5], ['honey', 100]]
]
sample_data_meals_for_a_day_feeder_1 = [
    [['dates', 17.0, 'g'], ['cow_milk', 200.0, 'g'], ['banana', 150.0, 'g'], ['honey', 10.0, 'g']],
    [['whole_boiled_egg', 4.0], ['albumen', 2.0], ['peanut_spinach_amla_salad_(medium)', 1.0],
     ['cooked_white_rice', 120.0, 'g']],
    [['oats', 30.0, 'g'], ['on_gs_c', 1.0, 'serving'], ['peanut_butter', 20.0, 'g']],
    [['kodo_millet', 300.0, 'g'], ['chicken', 100.0, 'g'], ['curd', 50.0, 'g']],
    [['rice', 300.0, 'g'], ['albumen', 6.0], ['yolk', 1.0]], [['chapati', 240.0, 'g'], ['chicken', 100.0, 'g']],
    [['milk', 200.0, 'g']], [['water', 2.5, 'L']]
]
sample_data_meals_for_a_day_feeder_2 = [
    [['dates', 17.0], ['cow_milk', 200.0], ['banana', 150.0], ['honey', 10.0]],
    [['whole_boiled_egg', 4.0], ['albumen', 2.0], ['peanut_spinach_amla_salad_(medium)', 1.0],
     ['cooked_brown_rice', 120.0]],
    [['uncooked_oats', 30.0], ['on_gs_c', 1.0], ['peanut_butter', 20.0]],
    [['cooked_kodo_millet', 300.0], ['cooked_chicken_normal_cut', 100.0], ['curd', 50.0]],
    [['cooked_brown_rice', 300.0], ['albumen', 6.0], ['yolk', 1.0]],
    [['cooked_wheat_chapati', 240.0], ['cooked_chicken_normal_cut', 100.0]],
    [['cow_milk', 200.0]], [['water', 2.5]],
]


# # single food
# single_food_data = (nutrition_tracker.calculate_nutritional_value_for_single_food("peanut_butter", 10))
# single_food_data2 = (nutrition_tracker.calculate_nutritional_value_for_single_food("peanut_butter", 110))
# print("Single food data: ", single_food_data)
# print("Single food data: ", single_food_data2, "\n")
#
# # a single meal
# result = nutrition_tracker.calculate_nutritional_value_for_a_meal(sample_data_for_a_meal_1)
# result2 = nutrition_tracker.calculate_nutritional_value_for_a_meal(sample_data_for_a_meal_2)
# result3 = nutrition_tracker.calculate_nutritional_value_for_a_meal(sample_data_for_a_meal_3)
# print("Result for a day: ", result)
# print("Result for a day: ", result2)
# print("Result for a day: ", result3, "\n")


# a day's meal data


#


# day's consolidated nutritional data from local text file
text_file = nutrition_tracker.take_file_name_of_text_file_and_give_text_file("sample_nov_9_2023_data")
ans = nutrition_tracker.take_in_raw_user_text_data_serve_nutritional_data_split_into_meals_with_units_and_days_nutritional_data_with_units(
        text_file, True,False, False)

for e in ans:
    print(e)

# # from data in script
# ans = nutrition_tracker.take_in_raw_user_text_data_serve_nutritional_data_split_into_meals_with_units_and_days_nutritional_data_with_units(
#     raw_data_2)
# print("Consolidated day's data: ", ans[0], "\n")
# print(" Day's data in meals basis: ", ans[1])
