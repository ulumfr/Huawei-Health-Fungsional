def initialize_diet_log():
    return {'breakfast': [], 'lunch': [], 'dinner': [], 'extra_meal': []}

def add_calorie_log(diet_log, meal_type, calories):
    meal_type = meal_type.lower()
    if meal_type not in diet_log:
        return "The food type is invalid. Use breakfast, lunch, dinner, or extra_meal."

    diet_log[meal_type].append(calories)
    return f"Calorie log for {meal_type.capitalize()} added: {calories} calories.\n"

def calculate_total_calories(food_log):
    total_calories = 0

    for meal_type, calories_list in food_log.items():
        total_calories += sum(calories_list)

    return total_calories

def display_diet_log(diet_log):
    return diet_log