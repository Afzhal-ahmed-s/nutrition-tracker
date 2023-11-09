from nutrition_tracker.enums.serving_enum import Serving_Enum as serving

food_data = [
    {
        "food_name": "cooked_rice",
        "data": {
            "quantity": serving.PER_100_GRAMS.value,
            "calories": 130,
            "fat": 0.2,
            "saturated": 0.1,
            "polyunsaturated": 0.1,
            "monounsaturated": 0.1,
            "cholesterol": 0,
            "sodium": 1,
            "potassium": 35,
            "carbohydrates": 28,
            "fiber": 0.4,
            "sugar": 0.1,
            "protein": 2.7,
            "image": "https://upload.wikimedia.org/wikipedia/commons/a/ae/Cooked_white_rice_in_a_bowl.jpg",
            "additional information": {"sources": ["bard AI"]}
        }
    },
    {
        "food_name": "cooked_brown_rice",
        "data": {
            "quantity": serving.PER_100_GRAMS.value,
            "calories": 112,
            "fat": 0.89,
            "saturated": 0.2,
            "polyunsaturated": 0.18,
            "monounsaturated": 0.51,
            "cholesterol": 0,
            "sodium": 1,
            "potassium": 79,
            "carbohydrates": 24.9,
            "fiber": 1.8,
            "sugar": 0.1,
            "protein": 2.32,
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/78/Brown_rice_closeup.jpg/330px-Brown_rice_closeup.jpg",
            "additional information": {"sources": ["bard AI"]}
        }
    },
    {
        "food_name": "cooked_chicken_normal_cut",
        "data": {
            "quantity": serving.PER_100_GRAMS.value,
            "calories": 239,
            "fat": 13,
            "saturated": 3.7,
            "polyunsaturated": 2.9,
            "monounsaturated": 5.2,
            "cholesterol": 73,
            "sodium": 95,
            "potassium": 353,
            "carbohydrates": 0,
            "fiber": 0,
            "sugar": 0,
            "protein": 25,
            "image": "https://upload.wikimedia.org/wikipedia/commons/d/d3/Chicken_pieces_2.jpg",
            "additional information": {"sources": ["bard AI", "nutritionix.com"],
                                       "protein-range": "varies between 24-28g"}
        }
    },
    {
        "food_name": "cow_milk",
        "data": {
            "quantity": serving.PER_100_GRAMS.value,
            "calories": 61,
            "fat": 3.3,
            "saturated": 1.8,
            "polyunsaturated": 0.4,
            "monounsaturated": 1.1,
            "cholesterol": 10,
            "sodium": 43,
            "potassium": 141,
            "carbohydrates": 4.8,
            "fiber": 0,
            "sugar": 4.8,
            "protein": 3.2,
            "image": "https://upload.wikimedia.org/wikipedia/commons/4/4e/Cow_white_black_on_grass.jpg"
        }
    },
    {
        "food_name": "whole_boiled_egg",
        "data": {
            "quantity": serving.PER_PIECE.value,
            "calories": 78,
            "fat": 5.3,
            "saturated": 1.6,
            "polyunsaturated": 0.7,
            "monounsaturated": 2.0,
            "cholesterol": 212,
            "sodium": 62,
            "potassium": 63,
            "carbohydrates": 0.7,
            "fiber": 0,
            "sugar": 0.7,
            "protein": 6.0,
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Hard-boiled_egg.jpg/1200px-Hard-boiled_egg.jpg"
        }
    },
    {
        "food_name": "peanut_butter",
        "data": {
            "quantity": serving.PER_100_GRAMS.value,
            "calories": 637.5,
            "fat": 50.0,
            "saturated": 6.3,
            "polyunsaturated": 12.5,
            "monounsaturated": 31.2,
            "cholesterol": 0,
            "sodium": 0,
            "potassium": 350,
            "carbohydrates": 20,
            "fiber": 7.2,
            "sugar": 7.5,
            "protein": 30.0,
            "image": "https://www.pintola.in/wp-content/uploads/2022/09/All-Natural-Peanut-Butter-Crunchy-1.jpg"
        }
    },
    {
        "food_name": "honey",
        "data": {
            "quantity": serving.PER_100_GRAMS.value,
            "calories": 304,
            "fat": 0,
            "saturated": 0,
            "polyunsaturated": 0,
            "monounsaturated": 0,
            "cholesterol": 0,
            "sodium": 4,
            "potassium": 75,
            "carbohydrates": 82.4,
            "fiber": 0,
            "sugar": 82.4,
            "protein": 0.3,
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Honey_in_a_jar.jpg/1200px-Honey_in_a_jar.jpg"
        }
    },
    {
        "food_name": "uncooked_oats",
        "data": {
            "quantity": serving.PER_100_GRAMS.value,
            "calories": 407,
            "fat": 9.5,
            "saturated": 1,
            "polyunsaturated": 2.9,
            "monounsaturated": 1.8,
            "cholesterol": 0,
            "sodium": 6,
            "potassium": 520,
            "carbohydrates": 68.5,
            "fiber": 10,
            "sugar": 1.1,
            "protein": 11.8,
            "image": "https://www.quaker.co.uk/products/traditional-wholegrain-oats-porridge"
        }
    },
    {
        "food_name": "on_gs_c",
        "data": {
            "quantity": serving.PER_SERVING.value,
            "calories": 120,
            "fat": 1.5,
            "saturated": 0.5,
            "polyunsaturated": 0.5,
            "monounsaturated": 0.5,
            "cholesterol": 60,
            "sodium": 65,
            "potassium": 190,
            "carbohydrates": 2,
            "fiber": 0.4,
            "sugar": 1.6,
            "protein": 24,
            "image": "https://www.optimumnutrition.com/wp-content/uploads/2021/11/ON_Gold_Standard_100_Whey_Protein_Powder_Chocolate-1024x1024.jpg"
        }
    },
    {
        "food_name": "water",
        "data": {
            "quantity": serving.PER_SERVING.value,
            "calories": 0,
            "fat": 0,
            "saturated": 0,
            "polyunsaturated": 0,
            "monounsaturated": 0,
            "cholesterol": 0,
            "sodium": 6,
            "potassium": 0,
            "carbohydrates": 0,
            "fiber": 0,
            "sugar": 0,
            "protein": 0,
            "image": "https://www.quaker.co.uk/products/traditional-wholegrain-oats-porridge"
        }
    },
    {
        "food_name": "dates",
        "data": {
            "quantity": serving.PER_100_GRAMS.value,
            "calories": 277,
            "fat": 0.2,
            "saturated": 0.1,
            "polyunsaturated": 0.1,
            "monounsaturated": 0.1,
            "cholesterol": 0,
            "sodium": 66,
            "potassium": 696,
            "carbohydrates": 75,
            "fiber": 8.1,
            "sugar": 64.5,
            "protein": 2.1,
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Medjool_dates.jpg/1200px-Medjool_dates.jpg"
        }
    },
    {
        "food_name": "banana",
        "data": {
            "quantity": serving.PER_100_GRAMS.value,
            "calories": 89,
            "fat": 0.3,
            "saturated": 0.1,
            "polyunsaturated": 0.2,
            "monounsaturated": 0.01,
            "cholesterol": 0,
            "sodium": 1,
            "potassium": 422,
            "carbohydrates": 22.8,
            "fiber": 2.6,
            "sugar": 12.6,
            "protein": 1.1,
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Yellow_Banana_Single.jpg/1200px-Yellow_Banana_Single.jpg"
        }
    },
    {
        "food_name": "cooked_wheat_chapati",
        "data": {
            "quantity": serving.PER_100_GRAMS.value,
            "calories": 264,
            "fat": 1.3,
            "saturated": 0.22,
            "polyunsaturated": 0.15,
            "monounsaturated": 0.55,
            "cholesterol": 0,
            "sodium": 210,
            "potassium": 200,
            "carbohydrates": 55.81,
            "fiber": 7,
            "sugar": 4,
            "protein": 9.6,
            "image": "https://upload.wikimedia.org/wikipedia/commons/9/9a/Chapati.jpg"
        }
    },
    {
        "food_name": "coconut_oil",
        "data": {
            "quantity": serving.PER_100_GRAMS.value,
            "calories": 862,
            "fat": 100,
            "saturated": 82,
            "polyunsaturated": 1.7,
            "monounsaturated": 6.3,
            "cholesterol": 0,
            "sodium": 0,
            "potassium": 0,
            "carbohydrates": 0,
            "fiber": 0,
            "sugar": 0,
            "protein": 0,
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Virgin_Coconut_Oil_225px.jpg/220px"
                     "-Virgin_Coconut_Oil_225px.jpg"
        }
    },
    {
        "food_name": "walnuts",
        "data": {
            "quantity": serving.PER_100_GRAMS.value,
            "calories": 654,
            "fat": 65,
            "saturated": 5.6,
            "polyunsaturated": 46.7,
            "monounsaturated": 12.7,
            "cholesterol": 0,
            "sodium": 2,
            "potassium": 705,
            "carbohydrates": 14,
            "fiber": 6,
            "sugar": 1.7,
            "protein": 15,
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/33/Walnuts_in_shell.jpg/1200px-Walnuts_in_shell.jpg"
        }
    },
    {
        "food_name": "almonds",
        "data": {
            "quantity": serving.PER_100_GRAMS.value,
            "calories": 579,
            "fat": 50,
            "saturated": 4.4,
            "polyunsaturated": 12,
            "monounsaturated": 34,
            "cholesterol": 0,
            "sodium": 18,
            "potassium": 733,
            "carbohydrates": 15.5,
            "fiber": 5,
            "sugar": 2.1,
            "protein": 21,
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b2/Handful_of_almonds.jpg/220px-Handful_of_almonds.jpg"
        }
    },
    {
        "food_name": "raisins",
        "data": {
            "quantity": serving.PER_100_GRAMS.value,
            "calories": 299,
            "fat": 0.5,
            "saturated": 0.1,
            "polyunsaturated": 0.2,
            "monounsaturated": 0.2,
            "cholesterol": 0,
            "sodium": 13,
            "potassium": 749,
            "carbohydrates": 79.5,
            "fiber": 3.7,
            "sugar": 62.5,
            "protein": 3,
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Medjool_dates.jpg/1200px-Medjool_dates.jpg"
        }
    },
    {
        "food_name": "amla",
        "data": {
            "quantity": serving.PER_100_GRAMS.value,
            "calories": 60,
            "fat": 0.5,
            "saturated": 0.1,
            "polyunsaturated": 0.1,
            "monounsaturated": 0.3,
            "cholesterol": 0,
            "sodium": 1,
            "potassium": 238,
            "carbohydrates": 13.3,
            "fiber": 3.9,
            "sugar": 0.9,
            "protein": 0.5,
            "image": "https://upload.wikimedia.org/wikipedia/commons/d/da/Phyllanthus_emblica_fruit_with_leaves.jpg"
        }
    },
    {
        "food_name": "uncooked_ragi_flour",
        "data": {
            "quantity": serving.PER_100_GRAMS.value,
            "calories": 341,
            "fat": 2.3,
            "saturated": 0.6,
            "polyunsaturated": 0.9,
            "monounsaturated": 0.8,
            "cholesterol": 0,
            "sodium": 3,
            "potassium": 418,
            "carbohydrates": 75.5,
            "fiber": 6,
            "sugar": 0.6,
            "protein": 7.3,
            "image": "https://static.toiimg.com/photo/msid-78005890/78005890.jpg"
        }
    },
    {
        "food_name": "uncooked_broken_wheat",
        "data": {
            "quantity": serving.PER_100_GRAMS.value,
            "calories": 342,
            "fat": 1.3,
            "saturated": 0.3,
            "polyunsaturated": 0.4,
            "monounsaturated": 0.6,
            "cholesterol": 0,
            "sodium": 2,
            "potassium": 126,
            "carbohydrates": 76,
            "fiber": 9.2,
            "sugar": 0.3,
            "protein": 12.8,
            "image": "https://www.thespicemanindia.com/wp-content/uploads/2018/12/Dalia-Broken-Wheat-1.jpg"
        }
    },
    {
        "food_name": "cooked_spinach",
        "data": {
            "quantity": serving.PER_100_GRAMS.value,
            "calories": 23,
            "fat": 0.4,
            "saturated": 0.07,
            "polyunsaturated": 0.17,
            "monounsaturated": 0.16,
            "cholesterol": 0,
            "sodium": 87,
            "potassium": 558,
            "carbohydrates": 3.6,
            "fiber": 2.1,
            "sugar": 1.4,
            "protein": 2.9,
            "image": "https://images.unsplash.com/photo-1589941142534-b9e51c541cf5?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8c3BpbmFjaCUyMHJlZCUyMGljb258ZW58MHx8MHx8&w=1000&q=80"
        }
    },
    {
        "food_name": "albumen",
        "data": {
            "quantity": serving.PER_PIECE.value,
            "calories": 17,
            "fat": 0.1,
            "saturated": 0,
            "polyunsaturated": 0,
            "monounsaturated": 0.1,
            "cholesterol": 0,
            "sodium": 52,
            "potassium": 126,
            "carbohydrates": 0.6,
            "fiber": 0,
            "sugar": 0,
            "protein": 3.6,
            "image": "https://en.wikipedia.org/wiki/Egg_white",
            "additional information": {
                "sources": ["USDA National Nutrient Database for Standard Reference"]
            }
        }
    },
    {
        "food_name": "yolk",
        "data": {
            "quantity": serving.PER_PIECE.value,
            "calories": 57,
            "fat": 5,
            "saturated": 2.7,
            "polyunsaturated": 1.3,
            "monounsaturated": 1,
            "cholesterol": 147,
            "sodium": 128,
            "potassium": 231,
            "carbohydrates": 0.3,
            "fiber": 0,
            "sugar": 0.1,
            "protein": 2.7,
            "image": "https://en.wikipedia.org/wiki/Egg_yolk",
            "additional information": {
                "sources": ["USDA National Nutrient Database for Standard Reference"]
            }
        }
    },
    {
        "food_name": "curd",
        "data": {
            "quantity": serving.PER_100_GRAMS.value,
            "calories": 70,
            "fat": 4,
            "saturated": 2,
            "polyunsaturated": 0.1,
            "monounsaturated": 1.2,
            "cholesterol": 15,
            "sodium": 52,
            "potassium": 175.8,
            "carbohydrates": 4.8,
            "fiber": 0,
            "sugar": 4.8,
            "protein": 3.9,
            "image": "https://en.wikipedia.org/wiki/Yogurt",
            "additional information": {
                "sources": ["USDA National Nutrient Database for Standard Reference"]
            }
        }
    },
    {
        "food_name": "cooked_kodo_millet",
        "data": {
            "quantity": serving.PER_100_GRAMS.value,
            "calories": 123,
            "fat": 1.3,
            "saturated": 0.2,
            "polyunsaturated": 0.5,
            "monounsaturated": 0.4,
            "cholesterol": 0,
            "sodium": 5,
            "potassium": 38,
            "carbohydrates": 25,
            "fiber": 1.3,
            "sugar": 0.2,
            "protein": 3.5,
            "vitamins": {
                "vitamin D": 0
            },
            "minerals": {
                "calcium": 17,
                "iron": 0.5
            },
            "image": "image_url_of_cooked_kodo_millet",
            "additional information": {"sources": ["GPT"]}
        }
    }

]

output_format_without_units = {
    "calories": 0,
    "protein": 0,
    "carbohydrates": 0,
    "fat": 0,
    "saturated": 0,
    "polyunsaturated": 0,
    "monounsaturated": 0,
    "potassium": 0,
    "fiber": 0,
    "sugar": 0,
    "cholesterol": 0,
    "sodium": 0
}

output_format_with_units = {
    "quantity": "g",
    "calories": "kcal",
    "protein": "g",
    "carbohydrates": "g",
    "fat": "g",
    "saturated": "g",
    "polyunsaturated": "g",
    "monounsaturated": "g",
    "potassium": "mg",
    "fiber": "g",
    "sugar": "g",
    "cholesterol": "mg",
    "sodium": "mg"
}

# output_format2 = {
#             "calories": 0,
#             "fat": {
#                 "total": 0,
#                 "saturated": 0,
#                 "polyunsaturated": 0,
#                 "monounsaturated": 0
#             },
#             "cholesterol": 0,
#             "sodium": 0,
#             "potassium": 0,
#             "carbohydrates": {
#                 "total": 0,
#                 "fiber": 0,
#                 "sugar": 0
#             },
#             "protein": 0,
#             "vitamins": {
#                 "vitamin D": 0
#             },
#             "minerals": {
#                 "calcium": 0,
#                 "iron": 0
#             },
#         }


to_add_foods = ["rice_idly", "millet_idly", "normal_dosa",
                "kolaputtu", "ragi_kolaputtu", "dal_gravy",
                "orange", "apple", "cooked_peanuts", "kodo_millet",
                "foxtail_millet", "cooked_foxtail_millet",
                "general_vegetable_salad(consisting of 2-3 vegetable)", "guava"]

excess_details = ["cooked_kodo_millet"]
