from repository.food_nutrition_repository import output_format_with_units, food_data
from enums.serving_enum import Serving_Enum as serving
import re
from service.nutrition_tracker_service import NutritionalValue

nutrition_tracker = NutritionalValue()


raw_data = ("Dates 17 g, Milk 200 g, Banana 150 g , Honey 10 g \n"
            "whole_egg 4, albumen 2, Peanut_Spinach_amla_salad_(medium), Rice 120 g\n"
            "Oats 30 g, ON_GS_C 1 serving , Peanut_butter 20 g \n"
            "Kodo_millet 300 g, Chicken 100 g, curd 50 g\n"
            "Rice 300 g, albumen 6 , yolk 1\n"
            "Chapati 240 g, chicken 100 g\n"
            "Milk 200 g\n"
            "Water 2.5 L ")

raw_data_2 = """Dates 20 g, cow_Milk 200g, Bananas 150g
Whole_boiled_eggs 6, amla 60g, cooked_rice 240g
cooked_rice 250g, cooked_chicken_normal_cut 100g, curd 40g
cooked_rice 310g, albumen 6, yolk 1
Wheat_dosa 400g, cooked_chicken_normal_cut 100g
cow_Milk 200g
Water 1L"""

print("RAW DATA 2: ", raw_data_2)



# raw_data_list = raw_data_2.split("\n")
# # print("c1", raw_data_list)
#
# list_data_by_meals = []
#
# for i in raw_data_list:
#     temporary = []
#     temporary.append(i)
#     list_data_by_meals.append(temporary)
# # print("c2", list_data_by_meals)
#
#
# list_data_by_meals_food = []
#
# for i in list_data_by_meals:
#     list_data_by_meals_food.append(i[0].strip().split(","))
# # print("c3", list_data_by_meals_food)
#
# list_data_by_meals_food_quantity = []
#
# for i in list_data_by_meals_food:
#     outer = []
#
#     for j in i:
#         local = []
#         temp = ( j.strip().split(" ") )
#         # print("debug ", temp)
#         local.append(temp[0].lower())
#         if len(temp) ==3 :
#             local.append(float(temp[1]))
#             # local.append(temp[2])
#
#         elif len(temp) == 2 :
#             number_without_unit = nutrition_tracker.return_quantity_as_number_from_a_string_combination(temp[1])
#             local.append(number_without_unit)
#             # local.append(temp[1])
#
#         else:
#             local.append(1.0)
#         outer.append(local)
#     list_data_by_meals_food_quantity.append(outer)
# print("c4", list_data_by_meals_food_quantity)



# def process_measurement_unit(unit):
#     # Lowercase the string
#     unit = unit.lower()
#
#     # Check if the string is 'gram' and convert it to 'g'
#     if unit == 'gram':
#         unit = 'g'
#     # Check if the string ends with 's' and remove it if it does
#     elif unit.endswith('s'):
#         unit = unit[:-1]
#
#     return unit
#
# # Examples
# units = ['g', 'grams', 'serving', 'servings', 'piece', 'pieces']
# processed_units = [process_measurement_unit(unit) for unit in units]
#
# print("source_units: ", units)
#
# print("processed_units: ", processed_units)


food_names = [food["food_name"] for food in food_data]

sl_no = 1
for e in food_names:
    print(sl_no, ". ", e)
    sl_no += 1



