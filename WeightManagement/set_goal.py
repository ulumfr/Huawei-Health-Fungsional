from datetime import datetime

def calculate_bmr(initial_weight, height_cm, age, gender):
    if gender.lower() == 'male':
        return (10 * initial_weight) + (6.25 * height_cm) - (5 * age) + 5
    elif gender.lower() == 'female':
        return (10 * initial_weight) + (6.25 * height_cm) - (5 * age) - 161
    else:
        raise ValueError("Gender should be 'male' or 'female'.")

def calculate_tdee(bmr, activity_level):
    activity_multipliers = {
        'sedentary': 1.2,
        'lightly_active': 1.375,
        'moderately_active': 1.55,
        'very_active': 1.725,
        'extremely_active': 1.9
    }
    return bmr * activity_multipliers.get(activity_level.lower())

def calculate_weeks_to_goal(initial_weight, target_weight, weight_loss_rate):
    weight_loss_needed = initial_weight - target_weight
    return weight_loss_needed / weight_loss_rate

def calculate_macronutrients(weight_kg, activity_level, tdee):
    protein_range = (1, 1.2) if activity_level.lower() in ['sedentary', 'lightly_active'] else (1.4, 2.2)
    protein_needs = weight_kg * protein_range[0], weight_kg * protein_range[1]

    fat_needs = weight_kg  

    carb_calories_low = int(0.45 * tdee)
    carb_calories_high = int(0.65 * tdee)
    carb_needs_low = carb_calories_low // 4
    carb_needs_high = carb_calories_high // 4

    return protein_needs, fat_needs, carb_needs_low, carb_needs_high

def format_output(goal, initial_weight, target_weight, weight_loss_needed, completed_by, bmr, tdee, weeks_to_goal_1_5kg, weeks_to_goal_1kg, weeks_to_goal_0_5kg, protein_needs, fat_needs, carb_needs_low, carb_needs_high):
    calorie_deficit = weight_loss_needed * 7700 if goal.lower() == 'lose' else 0
    calorie_surplus = -weight_loss_needed * 7700 if goal.lower() == 'gain' else 0

    return {
        'goal\t\t\t': goal,
        'initial_weight\t\t': initial_weight,
        'target_weight\t\t': target_weight,
        'calorie_deficit\t\t': calorie_deficit,
        'calorie_surplus\t\t': calorie_surplus,
        'completed_by\t\t': completed_by.strftime("%Y-%m-%d"),
        'bmr\t\t\t': bmr,
        'tdee\t\t\t': tdee,
        'weeks_to_goal_1.5kg\t': abs(weeks_to_goal_1_5kg),
        'weeks_to_goal_1kg\t': abs(weeks_to_goal_1kg),
        'weeks_to_goal_0.5kg\t': abs(weeks_to_goal_0_5kg),
        'protein_needs\t\t': protein_needs,
        'fat_needs\t\t': fat_needs,
        'carb_needs_low\t\t': carb_needs_low,
        'carb_needs_high\t\t': carb_needs_high
    }

def calculate_calorie_deficit_advanced(initial_weight, goal, target_weight, completed_by, height_cm, age, gender, activity_level):
    bmr = calculate_bmr(initial_weight, height_cm, age, gender)
    tdee = calculate_tdee(bmr, activity_level)

    weeks_1_5kg = calculate_weeks_to_goal(initial_weight, target_weight, 1.5)
    weeks_1kg = calculate_weeks_to_goal(initial_weight, target_weight, 1)
    weeks_0_5kg = calculate_weeks_to_goal(initial_weight, target_weight, 0.5)

    protein_needs, fat_needs, carb_needs_low, carb_needs_high = calculate_macronutrients(initial_weight, activity_level, tdee)

    completed_by_date = datetime.strptime(completed_by, "%Y-%m-%d")

    return format_output(goal, initial_weight, target_weight, initial_weight - target_weight, completed_by_date, bmr, tdee, weeks_1_5kg, weeks_1kg, weeks_0_5kg, protein_needs, fat_needs, carb_needs_low, carb_needs_high)