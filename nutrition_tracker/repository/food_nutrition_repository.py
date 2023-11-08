from enums.serving_enum import Serving_Enum as serving

food_data = [
    {
        "food_name": "cooked_rice",
        "data": {
            "quantity": serving.PER_100_GRAMS.value,
            "calories": 130,
            "fat": {
                "total": 0.2,
                "saturated": 0.1,
                "polyunsaturated": 0.1,
                "monounsaturated": 0.1
            },
            "cholesterol": 0,
            "sodium": 1,
            "potassium": 35,
            "carbohydrates": {
                "total": 28,
                "fiber": 0.4,
                "sugar": 0.1
            },
            "protein": 2.7,
            "vitamins": {
                "vitamin D": 0
            },
            "minerals": {
                "calcium": 10,
                "iron": 1.2
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/a/ae/Cooked_white_rice_in_a_bowl.jpg",
            "additional information": {"sources": ["bard AI"]}
        }
    },
    {
        "food_name": "cooked_brown_rice",
        "data": {
            "quantity": serving.PER_100_GRAMS.value,
            "calories": 112,
            "fat": {
                "total": 0.89,
                "saturated": 0.2,
                "polyunsaturated": 0.18,
                "monounsaturated": 0.51
            },
            "cholesterol": 0,
            "sodium": 1,
            "potassium": 79,
            "carbohydrates": {
                "total": 24.9,
                "fiber": 1.8,
                "sugar": 0.1
            },
            "protein": 2.32,
            "vitamins": {
                "vitamin D": 0
            },
            "minerals": {
                "calcium": 10,
                "iron": 0.5
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/78/Brown_rice_closeup.jpg/330px-Brown_rice_closeup.jpg",
            "additional information": {"sources": ["bard AI"]}
        }
    },
    {
        "food_name": "cooked_chicken_normal_cut",
        "data": {
            "quantity": serving.PER_100_GRAMS.value,
            "calories": 239,
            "fat": {
                "total": 13,
                "saturated": 3.7,
                "polyunsaturated": 2.9,
                "monounsaturated": 5.2
            },
            "cholesterol": 73,
            "sodium": 95,
            "potassium": 353,
            "carbohydrates": {
                "total": 0,
                "fiber": 0,
                "sugar": 0
            },
            "protein": 25,
            "vitamins": {
                "vitamin D": 0.1,
                "vitamin B3": 16.5,
                "vitamin B6": 0.4
            },
            "minerals": {
                "calcium": 18,
                "iron": 2,
                "zinc": 3.4
            },
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
            "fat": {
                "total": 3.3,
                "saturated": 1.8,
                "polyunsaturated": 0.4,
                "monounsaturated": 1.1
            },
            "cholesterol": 10,
            "sodium": 43,
            "potassium": 141,
            "carbohydrates": {
                "total": 4.8,
                "fiber": 0,
                "sugar": 4.8
            },
            "protein": 3.2,
            "vitamins": {
                "vitamin A": 32,
                "vitamin B12": 0.4,
                "vitamin D": 7.4,
                "riboflavin": 0.2
            },
            "minerals": {
                "calcium": 125,
                "phosphorus": 98,
                "zinc": 0.9
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/4/4e/Cow_white_black_on_grass.jpg"
        }
    },
    {
        "food_name": "whole_boiled_egg",
        "data": {
            "quantity": serving.PER_PIECE.value,
            "calories": 78,
            "fat": {
                "total": 5.3,
                "saturated": 1.6,
                "polyunsaturated": 0.7,
                "monounsaturated": 2.0
            },
            "cholesterol": 212,
            "sodium": 62,
            "potassium": 63,
            "carbohydrates": {
                "total": 0.7,
                "fiber": 0,
                "sugar": 0.7
            },
            "protein": 6.0,
            "vitamins": {
                "vitamin A": 98,
                "vitamin B12": 0.6,
                "vitamin B2": 0.2,
                "vitamin B5": 0.5
            },
            "minerals": {
                "selenium": 15.4,
                "phosphorus": 95,
                "iron": 1.1
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Hard-boiled_egg.jpg/1200px-Hard-boiled_egg.jpg"
        }
    },
    {
        "food_name": "peanut_butter",
        "data": {
            "quantity": serving.PER_100_GRAMS.value,
            "calories": 637.5,
            "fat": {
                "total": 50.0,
                "saturated": 6.3,
                "polyunsaturated": 12.5,
                "monounsaturated": 31.2
            },
            "cholesterol": 0,
            "sodium": 0,
            "potassium": 350,
            "carbohydrates": {
                "total": 16.8,
                "fiber": 7.2,
                "sugar": 7.5
            },
            "protein": 30.0,
            "vitamins": {
                "vitamin A": 130,
                "vitamin E": 12.5,
                "niacin": 19,
                "vitamin B6": 0.6
            },
            "minerals": {
                "magnesium": 265,
                "phosphorus": 240,
                "manganese": 3.65,
                "copper": 0.6
            },
            "image": "https://www.pintola.in/wp-content/uploads/2022/09/All-Natural-Peanut-Butter-Crunchy-1.jpg"
        }
    },
    {
        "food_name": "honey",
        "data": {
            "quantity": serving.PER_100_GRAMS.value,
            "calories": 304,
            "fat": {
                "total": 0,
                "saturated": 0,
                "polyunsaturated": 0,
                "monounsaturated": 0
            },
            "cholesterol": 0,
            "sodium": 4,
            "potassium": 75,
            "carbohydrates": {
                "total": 82.4,
                "fiber": 0,
                "sugar": 82.4
            }
            ,
            "protein": 0.3,
            "vitamins": {
                "vitamin A": 2,
                "vitamin C": 0.5,
                "vitamin B1": 0.1,
                "vitamin B2": 0.03,
                "vitamin B6": 0.02
            },
            "minerals": {
                "calcium": 7,
                "iron": 0.4,
                "magnesium": 2,
                "phosphorus": 12,
                "potassium": 52,
                "zinc": 0.34
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Honey_in_a_jar.jpg/1200px-Honey_in_a_jar.jpg"
        }
    },
    {
        "food_name": "uncooked_oats",
        "data": {
            "quantity": serving.PER_100_GRAMS.value,
            "calories": 407,
            "fat": {
                "total": 9.5,
                "saturated": 1,
                "polyunsaturated": 2.9,
                "monounsaturated": 1.8
            },
            "cholesterol": 0,
            "sodium": 6,
            "potassium": 520,
            "carbohydrates": {
                "total": 68.5,
                "fiber": 10,
                "sugar": 1.1
            }
            ,
            "protein": 11.8,
            "vitamins": {
                "vitamin A": 14,
                "vitamin B1": 0.3,
                "vitamin B2": 0.1,
                "vitamin B3": 0.9,
                "vitamin B6": 0.1
            },
            "minerals": {
                "calcium": 110,
                "iron": 4.3,
                "magnesium": 170,
                "phosphorus": 240,
                "potassium": 520,
                "zinc": 3.8
            },
            "image": "https://www.quaker.co.uk/products/traditional-wholegrain-oats-porridge"
        }
    },
    {
        "food_name": "on_gs_c",
        "data": {
            "quantity": serving.PER_SERVING.value,
            "calories": 120,
            "fat": {
                "total": 1.5,
                "saturated": 0.5,
                "polyunsaturated": 0.5,
                "monounsaturated": 0.5
            },
            "cholesterol": 60,
            "sodium": 65,
            "potassium": 190,
            "carbohydrates": {
                "total": 2,
                "fiber": 0.4,
                "sugar": 1.6
            }
            ,

            "protein": 24,
            "vitamins": {
                "vitamin A": 10,
                "vitamin C": 10,
                "vitamin D": 15,
                "vitamin E": 10,
                "vitamin B1": 1.5,
                "vitamin B2": 1.7,
                "vitamin B3": 16,
                "vitamin B6": 1.4,
                "vitamin B12": 1.25,
                "vitamin B5": 6,
                "vitamin K": 12
            },
            "minerals": {
                "calcium": 200,
                "iron": 1.5,
                "magnesium": 40,
                "phosphorus": 200,
                "zinc": 11
            },
            "image": "https://www.optimumnutrition.com/wp-content/uploads/2021/11/ON_Gold_Standard_100_Whey_Protein_Powder_Chocolate-1024x1024.jpg"
        }
    },
    {
        "food_name": "water",
        "data": {
            "quantity": serving.PER_SERVING.value,
            "calories": 0,
            "fat": {
                "total": 0,
                "saturated": 0,
                "polyunsaturated": 0,
                "monounsaturated": 0
            },
            "cholesterol": 0,
            "sodium": 6,
            "potassium": 0,
            "carbohydrates": {
                "total": 0,
                "fiber": 0,
                "sugar": 0
            },
            "protein": 0,
            "vitamins": {
                "vitamin A": 0,
                "vitamin B1": 0,
                "vitamin B2": 0,
                "vitamin B3": 0,
                "vitamin B6": 0
            },
            "minerals": {
                "calcium": 0,
                "iron": 0,
                "magnesium": 0,
                "phosphorus": 0,
                "potassium": 0,
                "zinc": 0
            },
            "image": "https://www.quaker.co.uk/products/traditional-wholegrain-oats-porridge"
        }
    },
    {
        "food_name": "dates",
        "data": {
            "quantity": serving.PER_100_GRAMS.value,
            "calories": 277,
            "fat": {
                "total": 0.2,
                "saturated": 0.1,
                "polyunsaturated": 0.1,
                "monounsaturated": 0.1
            },
            "cholesterol": 0,
            "sodium": 66,
            "potassium": 696,
            "carbohydrates": {
                "total": 75,
                "fiber": 8.1,
                "sugar": 64.5
            },
            "protein": 2.1,
            "vitamins": {
                "vitamin A": 15,
                "vitamin C": 0.4,
                "vitamin D": 0,
                "vitamin E": 0.1,
                "vitamin B1": 0.06,
                "vitamin B2": 0.05,
                "vitamin B3": 1.6,
                "vitamin B6": 0.3,
                "vitamin B12": 0.01,
                "vitamin B5": 0.5,
                "vitamin K": 2.7
            },
            "minerals": {
                "calcium": 34,
                "iron": 0.9,
                "magnesium": 54,
                "phosphorus": 69,
                "zinc": 0.3
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Medjool_dates.jpg/1200px-Medjool_dates.jpg"
        }
    },
    {
        "food_name": "banana",
        "data": {
            "quantity": serving.PER_100_GRAMS.value,
            "calories": 89,
            "fat": {
                "total": 0.3,
                "saturated": 0.1,
                "polyunsaturated": 0.2,
                "monounsaturated": 0.01
            },
            "cholesterol": 0,
            "sodium": 1,
            "potassium": 422,
            "carbohydrates": {
                "total": 22.8,
                "fiber": 2.6,
                "sugar": 12.6
            },
            "protein": 1.1,
            "vitamins": {
                "vitamin A": 81,
                "vitamin C": 8.7,
                "vitamin D": 0,
                "vitamin E": 0.1,
                "vitamin B1": 0.09,
                "vitamin B2": 0.07,
                "vitamin B3": 0.8,
                "vitamin B6": 0.3,
                "vitamin B12": 0.001,
                "vitamin B5": 0.3,
                "vitamin K": 0.5
            },
            "minerals": {
                "calcium": 5,
                "iron": 0.3,
                "magnesium": 32,
                "phosphorus": 24,
                "zinc": 0.1
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Yellow_Banana_Single.jpg/1200px-Yellow_Banana_Single.jpg"
        }
    },
    {
        "food_name": "cooked_wheat_chapati",
        "data": {
            "quantity": serving.PER_100_GRAMS.value,
            "calories": 264,
            "fat": {
                "total": 1.3,
                "saturated": 0.22,
                "polyunsaturated": 0.15,
                "monounsaturated": 0.55
            },
            "cholesterol": 0,
            "sodium": 210,
            "potassium": 200,
            "carbohydrates": {
                "total": 55.81,
                "fiber": 7,
                "sugar": 4
            },
            "protein": 9.6,
            "vitamins": {
                "vitamin A": 22,
                "vitamin C": 0.1,
                "vitamin D": 0,
                "vitamin E": 0.1,
                "vitamin B1": 0.07,
                "vitamin B2": 0.05,
                "vitamin B3": 1,
                "vitamin B6": 0.1,
                "vitamin B12": 0,
                "vitamin B5": 0.6,
                "vitamin K": 0.7
            },
            "minerals": {
                "calcium": 10,
                "iron": 1.2,
                "magnesium": 38,
                "phosphorus": 118,
                "zinc": 1.3
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/9/9a/Chapati.jpg"
        }
    },
    {
        "food_name": "coconut_oil",
        "data": {
            "quantity": serving.PER_100_GRAMS.value,
            "calories": 862,
            "fat": {
                "total": 100,
                "saturated": 82,
                "polyunsaturated": 1.7,
                "monounsaturated": 6.3
            },
            "cholesterol": 0,
            "sodium": 0,
            "potassium": 0,
            "carbohydrates": {
                "total": 0,
                "fiber": 0,
                "sugar": 0
            },
            "protein": 0,
            "vitamins": {
                "vitamin A": 0,
                "vitamin C": 0,
                "vitamin D": 0,
                "vitamin E": 1.4,
                "vitamin K": 0.1
            },
            "minerals": {
                "calcium": 0,
                "iron": 0,
                "magnesium": 0,
                "phosphorus": 0,
                "zinc": 0
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Virgin_Coconut_Oil_225px.jpg/220px-Virgin_Coconut_Oil_225px.jpg"
        }
    },
    {
        "food_name": "walnuts",
        "data": {
            "quantity": serving.PER_100_GRAMS.value,
            "calories": 654,
            "fat": {
                "total": 65,
                "saturated": 5.6,
                "polyunsaturated": 46.7,
                "monounsaturated": 12.7
            },
            "cholesterol": 0,
            "sodium": 2,
            "potassium": 705,
            "carbohydrates": {
                "total": 14,
                "fiber": 6,
                "sugar": 1.7
            },
            "protein": 15,
            "vitamins": {
                "vitamin A": 23,
                "vitamin C": 2.3,
                "vitamin D": 3,
                "vitamin E": 7.4,
                "vitamin K": 15,
                "vitamin B1": 0.8,
                "vitamin B2": 0.1,
                "vitamin B3": 1.2,
                "vitamin B6": 0.5,
                "vitamin B12": 0,
                "vitamin B5": 1
            },
            "minerals": {
                "calcium": 98,
                "iron": 2.1,
                "magnesium": 177,
                "phosphorus": 486,
                "zinc": 2
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/33/Walnuts_in_shell.jpg/1200px-Walnuts_in_shell.jpg"
        }
    },
    {
        "food_name": "almonds",
        "data": {
            "quantity": serving.PER_100_GRAMS.value,
            "calories": 579,
            "fat": {
                "total": 50,
                "saturated": 4.4,
                "polyunsaturated": 12,
                "monounsaturated": 34
            },
            "cholesterol": 0,
            "sodium": 18,
            "potassium": 733,
            "carbohydrates": {
                "total": 15.5,
                "fiber": 5,
                "sugar": 2.1
            },
            "protein": 21,
            "vitamins": {
                "vitamin A": 13,
                "vitamin C": 1.1,
                "vitamin D": 57,
                "vitamin E": 7.4,
                "vitamin K": 28,
                "vitamin B1": 0.7,
                "vitamin B2": 1.3,
                "vitamin B3": 3,
                "vitamin B6": 0.1,
                "vitamin B12": 0,
                "vitamin B5": 0.5
            },
            "minerals": {
                "calcium": 75,
                "iron": 1.7,
                "magnesium": 270,
                "phosphorus": 481,
                "zinc": 2.1
            },
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b2/Handful_of_almonds.jpg/220px-Handful_of_almonds.jpg"
        }
    },
    {
        "food_name": "raisins",
        "data": {
            "quantity": serving.PER_100_GRAMS.value,
            "calories": 299,
            "fat": {
                "total": 0.5,
                "saturated": 0.1,
                "polyunsaturated": 0.2,
                "monounsaturated": 0.2
            },
            "cholesterol": 0,
            "sodium": 13,
            "potassium": 749,
            "carbohydrates": {
                "total": 79.5,
                "fiber": 3.7,
                "sugar": 62.5
            },
            "protein": 3,
            "vitamins": {
                "vitamin A": 15,
                "vitamin C": 0.4,
                "vitamin D": 0,
                "vitamin E": 0.1,
                "vitamin K": 2.7,
                "vitamin B1": 0.06,
                "vitamin B2": 0.05,
                "vitamin B3": 1.6,
                "vitamin B6": 0.3,
                "vitamin B12": 0.01,
                "vitamin B5": 0.5
            },
            "minerals": {
                "calcium": 34,
                "iron": 0.9,
                "magnesium": 54,
                "phosphorus": 69,
                "zinc": 0.3
            },
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
            "carbohydrates": {
                "total": 13.3,
                "fiber": 3.9,
                "sugar": 0.9
            },
            "protein": 0.5,
            "vitamins": {
                "vitamin A": 30,
                "vitamin C": 817,
                "vitamin D": 0,
                "vitamin E": 0.2,
                "vitamin K": 0.5,
                "vitamin B1": 0.05,
                "vitamin B2": 0.03,
                "vitamin B3": 0.7,
                "vitamin B6": 0.02,
                "vitamin B12": 0.01,
                "vitamin B5": 0.02
            },
            "minerals": {
                "calcium": 10,
                "iron": 0.4,
                "magnesium": 10,
                "phosphorus": 22,
                "zinc": 0.2
            },
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
            "carbohydrates": {
                "total": 75.5,
                "fiber": 6,
                "sugar": 0.6
            },
            "protein": 7.3,
            "vitamins": {
                "vitamin A": 20,
                "vitamin C": 0.9,
                "vitamin D": 0,
                "vitamin E": 0.3,
                "vitamin K": 0.9,
                "vitamin B1": 0.1,
                "vitamin B2": 0.07,
                "vitamin B3": 3.2,
                "vitamin B6": 0.1,
                "vitamin B12": 0,
                "vitamin B5": 0.3
            },
            "minerals": {
                "calcium": 344,
                "iron": 8.2,
                "magnesium": 130,
                "phosphorus": 281,
                "zinc": 2.5
            },
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
            "carbohydrates": {
                "total": 76,
                "fiber": 9.2,
                "sugar": 0.3
            },
            "protein": 12.8,
            "vitamins": {
                "vitamin A": 1,
                "vitamin C": 0,
                "vitamin D": 0,
                "vitamin E": 0.1,
                "vitamin K": 0.3,
                "vitamin B1": 0.4,
                "vitamin B2": 0.05,
                "vitamin B3": 6.1,
                "vitamin B6": 0.4,
                "vitamin B12": 0,
                "vitamin B5": 1.2
            },
            "minerals": {
                "calcium": 41,
                "iron": 4.5,
                "magnesium": 177,
                "phosphorus": 345,
                "zinc": 1.4
            },
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
            "carbohydrates": {
                "total": 3.6,
                "fiber": 2.1,
                "sugar": 1.4
            },
            "protein": 2.9,
            "vitamins": {
                "vitamin A": 5747,
                "vitamin C": 28.1,
                "vitamin D": 0,
                "vitamin E": 2.03,
                "vitamin K": 547,
                "vitamin B1": 0.06,
                "vitamin B2": 0.16,
                "vitamin B3": 0.81,
                "vitamin B6": 0.06,
                "vitamin B12": 0,
                "vitamin B5": 0.05
            },
            "minerals": {
                "calcium": 99,
                "iron": 3.6,
                "magnesium": 78,
                "phosphorus": 73,
                "zinc": 0.5
            },
            "image": "https://images.unsplash.com/photo-1589941142534-b9e51c541cf5?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8c3BpbmFjaCUyMHJlZCUyMGljb258ZW58MHx8MHx8&w=1000&q=80"
        }
    },
]

output_format_without_units = {
    "calories": 0,
    "fat": {
        "total": 0,
        "saturated": 0,
        "polyunsaturated": 0,
        "monounsaturated": 0
    },
    "cholesterol": 0,
    "sodium": 0,
    "potassium": 0,
    "carbohydrates": {
        "total": 0,
        "fiber": 0,
        "sugar": 0
    },
    "protein": 0,
    "vitamins": {
        "vitamin D": 0
    },
    "minerals": {
        "calcium": 0,
        "iron": 0
    },
}

output_format_with_units = {
    "quantity": "g",
    "calories": "kcal",
    "fat": {
        "total": "g",
        "saturated": "g",
        "polyunsaturated": "g",
        "monounsaturated": "g",
    },
    "cholesterol": "mg",
    "sodium": "mg",
    "potassium": "mg",
    "carbohydrates": {
        "total": "g",
        "fiber": "g",
        "sugar": "g",
    },
    "protein": "g",
    "vitamins": {
        "vitamin D": "IU",
    },
    "minerals": {
        "calcium": "mg",
        "iron": "mg",
    },
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


to_add_foods = ["albumen per egg", "yolk per egg", "idly", "normal dosa", "kolaputtu", "ragi kolaputtu", "dal gravy"]
