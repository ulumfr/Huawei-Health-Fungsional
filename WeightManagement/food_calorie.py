def initialize_diet_log():
    return {'breakfast': [], 'lunch': [], 'dinner': [], 'extra_meal': []}

def add_calorie_log(diet_log, meal_type, calories):
    meal_type = meal_type.lower()
    if meal_type not in diet_log:
        return "Jenis makanan tidak valid. Gunakan breakfast, lunch, dinner, atau extra_meal."

    diet_log[meal_type].append(calories)

    return f"Log kalori untuk {meal_type.capitalize()} ditambahkan: {calories} kalori."

def display_diet_log(diet_log):
    return diet_log

def main():
    food_log = initialize_diet_log()

    while True:
        meal_type = input("Masukkan jenis makanan (breakfast, lunch, dinner, extra_meal) atau ketik 'selesai' untuk keluar: ")
        
        if meal_type.lower() == 'selesai':
            break

        calories = float(input("Masukkan jumlah kalori: "))
        result = add_calorie_log(food_log, meal_type, calories)
        print(result)

    diet_log = display_diet_log(food_log)
    print("\nLog Diet Saat Ini:")
    print(diet_log)

main()
