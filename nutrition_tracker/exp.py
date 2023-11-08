from repository.food_nutrition_repository import output_format_with_units
from enums.serving_enum import Serving_Enum as serving
import re


raw_data = ("Dates 17g, Milk 200g, Bananas 150g, Honey 10g \n"
            "4 whole_eggs,  2 whites, Peanut_Spinach_amla_salad_(medium), Rice_120g\n"
            "Oats_30g, ON_GS_C 1 , Peanut_butter 20g \n"
            "Kodo_millet 300g, Chicken 100g, curd 50g\n"
            "Rice 300g, 6 egg_whites, 1 yolk\n"
            "Chapati 240g, chicken 100g\n"
            "Milk 200g\n"
            "Water 2.5L ")


raw_data_list = raw_data.split("\n")
print("c1", raw_data_list)

list_data_by_meals = []

for i in raw_data_list:
    temporary = []
    temporary.append(i)
    list_data_by_meals.append(temporary)

print(list_data_by_meals)



list_data_by_meals_food = []

for i in list_data_by_meals:
    list_data_by_meals_food.append(i[0].strip().split(","))
print("c3", list_data_by_meals_food)

# list_data_by_meals_food_quantity = []
#
# for i in list_data_by_meals_food:
#     outer = []
#
#     for j in i:
#         local = []
#         temp = ( j.strip().split(" ") )
#         local.append(temp[0].lower())
#         if len(temp) > 1:
#             list_of_quantity_and_unit = temp[1]
#             # local.append(float(temp[1]))
#             local.append((temp[1]))
#
#         else:
#             local.append(1.0)
#         outer.append(local)
#     list_data_by_meals_food_quantity.append(outer)
#
# print("c4", list_data_by_meals_food_quantity)

# Examples of strings
strings = ['1', '1.3', '1.3g', '1g', '1serving', '2pcs', 'sadfsf']
ans = []

for s in strings:
    match = re.match(r'(\d*\.?\d+)([a-zA-Z]*)', s)
    temp = []
    if match:
        numeric_part, non_numeric_part = match.groups()
        print(f"Original: {s}, Numeric: {numeric_part}, Non-Numeric: {non_numeric_part}")
        temp.append(float(numeric_part))
        if non_numeric_part == '':
            pass
        else:
            temp.append(non_numeric_part)
    else:
        print(f"String '{s}' doesn't match the pattern.")

    ans.append(temp)

print(ans)


# def traverse_nested_dict(dictionary, depth=0):
#     for key, value in dictionary.items():
#         if isinstance(value, dict):
#             print("  " * depth + f"{key}:")
#             traverse_nested_dict(value, depth + 1)
#         else:
#             print("  " * depth + f"{key}: {value}")
