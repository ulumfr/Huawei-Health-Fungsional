from SleepRecord.sleeprecord import calculate_sleep_stats, analyze_sleep_quality
from WeightManagement import calorie_record, weight_record, set_goal, food_calorie
from ExerciseRecord import charts_hr, detail_exercise, performance_analysis, routes
import HeartRate.heartrate_chart as hr_chart

heart_rate_data = [65, 66, 70, 80, 88, 90, 93, 100, 102, 109, 115, 130, 140, 139, 145, 146, 148, 152, 160, 166, 171, 169, 170, 169, 164, 160, 158, 155, 150, 149, 145, 143, 135, 129, 110, 105, 101, 97, 93, 90, 88, 75]
sleep_heart_rate_data = [55, 53, 50, 52, 48, 45, 47, 43, 41, 42, 44, 41, 46, 56, 60, 59, 62, 66, 75]
resting_heart_rate = 60
consumed_calories_data = {}
burned_calories_data = {}
weight_data = []

dummy_account = {
    "users": {
        "ulum@gmail.com": {
            "name": "Bahrul Ulum Fadhlur R",
            "password": "userUlum",
        },
        "gus@gmail.com": {
            "name": "Muhammad Gus Nadir",
            "password": "userGus",
        }
    },
}

def calculate_heart_rate_statistics(heart_rate_data):
    return charts_hr.calculate_statistics(heart_rate_data)

def plot_heart_rate(heart_rate_data, average_heart_rate, max_heart_rate):
    return charts_hr.plot_heart_rate_chart(heart_rate_data, average_heart_rate, max_heart_rate)

def calculate_exercise_calories(email, start_time, end_time, heart_rate_data, weight, age, gender):
    duration = detail_exercise.calculate_duration(start_time, end_time)
    average_heart_rate = detail_exercise.calculate_average_heart_rate(heart_rate_data)
    calories_burned = detail_exercise.calculate_calories_burned(duration, average_heart_rate, weight, age, gender)

    burned_calories_data[email] = calories_burned
    return duration, calories_burned, average_heart_rate

def perform_analysis(age, heart_rate_data, resting_heart_rate):
    heart_rate_zones = performance_analysis.heart_rate_zones(age, heart_rate_data)
    max_heart_rate = performance_analysis.max_heartrate(heart_rate_data)
    vo2max = performance_analysis.calculate_vo2max(max_heart_rate, resting_heart_rate)

    peak_heart_rate = max_heart_rate
    heart_rate_after_one_minute = heart_rate_data[-1]
    heart_rate_recovery = performance_analysis.calculate_heart_rate_recovery(peak_heart_rate, heart_rate_after_one_minute)
    return heart_rate_zones, vo2max, heart_rate_recovery

def calorie(email):
    tracker = calorie_record.CalorieTracker()
    exercise_calories = burned_calories_data.get(email, 0) 
    consumed_calories = consumed_calories_data.get(email, 0)
    updated_tracker = tracker.add_record(burned_calories=exercise_calories, consumed_calories=consumed_calories)
    updated_tracker.display_totals()
    return updated_tracker

def food_calorie_detail(email, food_log):
    consumed_calories = food_calorie.calculate_total_calories(food_log)
    consumed_calories_data[email] = consumed_calories
    return consumed_calories

while True:
    print("\n===== LOGIN HUAWEI HEALTH =====")
    email = input("\nEmail\t : ")
    password = input("Password : ")
    
    if email in dummy_account["users"] and password == dummy_account["users"][email]["password"]:
        name = dummy_account["users"][email]["name"]
        print("\n===============================")
        print(f"\n\nWelcome, {name}")

        while True:
            print("\n=== Huawei Dashboard ===")
            print("1. Exercise Record\n2. Heart Rate\n3. Sleep Record\n4. Weight Management\n0. Logout")
            choice = int(input("Choose an option (1/2/3/4/0): "))
            
            if choice == 1:
                while True:
                    print("\n\n=== Exercise Record ===")
                    print("1. Chart Heart Rate\n2. Detail Exercise\n3. Performance Analysis\n4. Routes\n0. Back to Main Menu")
                    choice = int(input("Choose an option (1/2/3/4/0): "))

                    if choice == 1:
                         average_heart_rate, max_heart_rate = calculate_heart_rate_statistics(heart_rate_data)
                         print("\nOpen Heart Rate Chart")
                         plot_heart_rate(heart_rate_data, average_heart_rate, max_heart_rate)
                         print("Close Heart Rate Chart")

                    elif choice == 2:
                        print("\n=== Input Exercise Recording ===")
                        start_time = input("Start Exercise - Enter start time (HH:MM:SS)\t: ")
                        end_time = input("Exercise Completed - Enter end time (HH:MM:SS)\t: ")
                        weight = float(input("Enter your weight (kg): "))
                        age = int(input("Enter your age (years): "))
                        gender = input("Enter your gender (women/men): ")

                        duration, calories_burned, average_heart_rate = calculate_exercise_calories(email, start_time, end_time, heart_rate_data, weight, age, gender)

                        print("\n=== Exercise Recording Result ===")
                        print(f"Exercise Duration\t: {duration} minutes")
                        print(f"Calories Burned\t\t: {calories_burned} calories")
                        print(f"Average Heart Rate\t: {average_heart_rate} BPM")
 
                    elif choice == 3:
                        print("\n\n=== Performance Analysis ===")
                        age = int(input("Enter your age: "))

                        print("\n=== Heart Rate Training Zones ===")
                        hr_zones, vo2_max, hr_recovery = perform_analysis(age, heart_rate_data, resting_heart_rate)
                        
                        print("\n=== Heart Rate Data Analysis ===")
                        print(f"VO2 Max\t\t\t: {vo2_max:.2f}")
                        print(f"Heart Rate Recovery\t: {hr_recovery:.2f} bpm")

                    elif choice == 4:
                        print("\n=== Routes Exercise ===")
                        print("Start Exercise Route")
                        routes.start_route()              
                        print("Exercise Recording Completed")

                    elif choice == 0:
                        print("\n## Returning to Main Menu...")
                        break
                    else:
                        print("\n### Invalid Choice, Please try again...")
                        
            elif choice == 2:
                    start_time_str = input("Enter start time (YYYY-MM-DD HH:MM:SS): ")
                    start_time = hr_chart.datetime.strptime(start_time_str, '%Y-%m-%d %H:%M:%S')

                    interval = int(input("Enter interval in minutes: "))

                    print("\n=== Heart Rate ===")
                    print("\nOpen Heart Rate Chart")
                    hr_chart.create_and_plot_heart_rate_chart(start_time, interval, heart_rate_data)
                    print("Close Heart Rate Chart")

            elif choice == 3:
                sleep_hours = float(input("Enter the number of sleep hours: "))

                sleep_stats = calculate_sleep_stats(sleep_heart_rate_data, sleep_hours)
                print("\n=== Sleep Record ===")
                print(f"Total Sleep Time\t: {sleep_stats['total_sleep_time'][0]} hours and {sleep_stats['total_sleep_time'][1]} minutes")
                print(f"Deep Sleep Percentage\t: {sleep_stats['deep_sleep_percentage']}%")
                print(f"Light Sleep Percentage\t: {sleep_stats['light_sleep_percentage']}%")
                print(f"REM Sleep Percentage\t: {sleep_stats['rem_sleep_percentage']}%")

                quality_indicators = analyze_sleep_quality(sleep_stats)
                print("\n=== Sleep Quality Analysis ===")
                print(f"Deep Sleep Indicator\t: {quality_indicators['deep_sleep_indicator']}")
                print(f"Light Sleep Indicator\t: {quality_indicators['light_sleep_indicator']}")
                print(f"REM Sleep Indicator\t: {quality_indicators['rem_sleep_indicator']}")

            elif choice == 4:
                while True:
                    print("\n\n=== Weight Management ===")
                    print("1. Calorie Record\n2. Food Calorie\n3. Set Goal\n4. Weight Record\n0. Back to Main Menu")

                    choice = int(input("Choose an option (1/2/3/4/0): "))
                    if choice == 1:
                        calorie(email)

                    elif choice == 2:
                        print("\n=== Input Food Calorie ===")
                        food_log = food_calorie.initialize_diet_log()

                        while True:
                            meal_type = input("Enter the meal type (breakfast, lunch, dinner, extra_meal), or type 'done' to exit: ")

                            if meal_type.lower() == 'done':
                                break

                            calories = float(input("Enter the number of calories: "))
                            food_calorie.add_calorie_log(food_log, meal_type, calories)

                        food_calorie_detail(email, food_log)

                        diet_log = food_calorie.display_diet_log(food_log)
                        print(f"\nCurrent Diet Log: {diet_log}")

                    elif choice == 3:
                        print("\n=== Set Weight Goal ===")

                        initial_weight = float(input("Enter your initial weight in kg: "))
                        goal = input("Enter your goal ('lose' or 'gain'): ")
                        target_weight = float(input("Enter your target weight in kg: "))
                        completed_by = input("Enter the completion date (YYYY-MM-DD): ")
                        height_cm = float(input("Enter your height in cm: "))
                        age = int(input("Enter your age: "))
                        gender = input("Enter your gender ('male' or 'female'): ")
                        activity_level = input("Enter your activity level ('sedentary', 'lightly_active', 'moderately_active', 'very_active', 'extremely_active'): ")

                        result_advanced = set_goal.calculate_calorie_deficit_advanced(initial_weight, goal, target_weight, completed_by, height_cm, age, gender, activity_level)

                        print("\n=== Weight Goal Calculation Results ===")
                        for key, value in result_advanced.items():
                            print(f"{key}: {value}")

                    elif choice == 4:
                        print("\n=== Input Record Weight ===")
                        date = input("Enter date (format: YYYY-MM-DD)\t\t: ")
                        time = input("Enter time (format: HH:MM)\t\t: ")
                        weight = float(input("Enter weight (kg)\t\t\t: "))

                        body_fat_input = input("Enter body fat percentage (optional)\t: ")
                        result_weight = weight_record.add_record_weight(weight_data, date, time, weight, body_fat_input)
                        
                        print("\nList of Weight Records:")
                        print("----------------------------")
                        weight_record.display_records(result_weight)

                    elif choice == 0:
                        print("\n## Returning to Main Menu...")
                        break

                    else:
                        print("\n### Invalid Choice, Please try again...")

            elif choice == 0:
                print("\n## Successfully Logged Out..")
                break

            else:
                print("\n### Invalid Choice, Please try again...")
        
    else: 
        print("\n### Account not found, Please try again...")