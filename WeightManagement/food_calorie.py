def initialize_diet_log():
    return {'breakfast': [], 'lunch': [], 'dinner': [], 'extra_meal': []}

def add_calorie_log(diet_log, meal_type, calories):
    meal_type = meal_type.lower()
    if meal_type not in diet_log:
        return "The food type is invalid. Use breakfast, lunch, dinner, or extra_meal."

    diet_log[meal_type].append(calories)

    return f"Calorie log for {meal_type.capitalize()} added: {calories} calories.\n"

def display_diet_log(diet_log):
    return diet_log

def main():
    food_log = initialize_diet_log()
    print("\n=== Input Food Calorie ===")
    
    while True:
        meal_type = input("Enter the meal type (breakfast, lunch, dinner, extra_meal), or type 'done' to exit: ")

        if meal_type.lower() == 'done':
            break

        calories = float(input("Enter the number of calories: "))
        result = add_calorie_log(food_log, meal_type, calories)
        print(result)

    diet_log = display_diet_log(food_log)
    print("\nCurrent Diet Log: ")
    print(diet_log)