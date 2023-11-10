from abc import ABC, abstractmethod


class NutritionTrackerInterface(ABC):

    @abstractmethod
    def calculate_nutritional_value_for_a_meal(self, list_of_a_food_item_detail):
        pass

    @abstractmethod
    def calculate_nutritional_value_for_multiple_meals(self, mega_list_data):
        pass

    @abstractmethod
    def calculate_nutritional_value_for_single_food(self, food_name, quantity, serving_type):
        pass

    @abstractmethod
    def get_raw_nutritional_data_of_meals_in_a_day(self, ultimate_data_compiled):
        pass

    @abstractmethod
    def give_me_serving_enum_in_return_for_string(self, unit_in_string):
        pass

    @abstractmethod
    def parse_text_data_to_desired_initial_input_format(self, text_data):
        pass

    @abstractmethod
    def print_a_days_nutritional_data_split_into_meals(self, raw_data):
        pass

    @abstractmethod
    def process_measurement_unit(self, unit):
        pass

    @abstractmethod
    def return_quantity_as_number_from_a_string_combination(self, data):
        pass

    @abstractmethod
    def serve_a_days_nutritional_data_split_into_meals_as_data_with_units(self, raw_data):
        pass

    @abstractmethod
    def take_in_raw_user_text_data_serve_nutritional_data_split_into_meals_with_units_and_days_nutritional_data_with_units(
            self, raw_text_data, consolidated_data, raw_meal_wise_data, print_meal_wise_data_for_the_day):
        pass

    @abstractmethod
    def value_round_off(self, data, places):
        pass

    @abstractmethod
    def add_up_data_to_desired_format(self, final_data, data_dict):
        pass

    @abstractmethod
    def append_units_to_data(self, data, units):
        pass

    @abstractmethod
    def add_up_nutritional_data_without_units_for_a_day(self, raw_list_of_nutritional_dictionaries):
        pass

    @abstractmethod
    def add_units_to_food_list(self, list_of_food_and_quantity):
        pass

    @abstractmethod
    def take_file_name_of_text_file_and_give_text_file(self, file_name):
        pass

    @abstractmethod
    def convert_request_to_boolean(self, one, two, three):
        pass
