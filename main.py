from SleepRecord.sleeprecord import calculate_sleep_stats, analyze_sleep_quality
from WeightManagement import calorie_record, food_calorie, set_goal, weight_record
from ExerciseRecord import charts_hr, detail_exercise, performance_analysis, routes
import HeartRate.heartrate_chart as hr_chart

dummy_account = {
    "users": {
        "u": {
            "name": "Bahrul Ulum Fadhlur R",
            "password": "u",
        },
        "gus@gmail.com": {
            "name": "Muhammad Gus Nadir",
            "password": "userGus",
        }
    },
}

def login():
    while True:
        print("\n===== LOGIN HUAWEI HEALTH =====")
        email = input("\nEmail\t : ")
        password = input("Password : ")
        
        if email in dummy_account["users"] and password == dummy_account["users"][email]["password"]:
            name = dummy_account["users"][email]["name"]
            print("\n===============================")
            print(f"\n\nWelcome, {name}")
            huawei_dashboard()
        else: 
            print("\n### Account not found, Please try again...")

def huawei_dashboard():
    while True:
        print("\n=== Huawei Dashboard ===")
        print("1. Exercise Record\n2. Heart Rate\n3. Sleep Record\n4. Weight Management\n0. Logout")
        
        choice = int(input("Choose an option (1/2/3/4/0): "))
        if choice == 1:
            exercise_record()
        elif choice == 2:
            heart_rate()
        elif choice == 3:
            sleep_record()
        elif choice == 4:
            weight_management()
        elif choice == 0:
            print("\n## Successfully Logged Out..")
            login()
        else:
            print("\n### Invalid Choice, Please try again...")
    
def exercise_record():
    while True:
        print("\n\n=== Exercise Record ===")
        print("1. Chart Heart Rate\n2. Detail Exercise\n3. Performance Analysis\n4. Routes\n0. Back to Main Menu")

        choice = int(input("Choose an option (1/2/3/4/0): "))
        if choice == 1:
            chart_hr()
        elif choice == 2:
            detail_exercise.main()
        elif choice == 3:
            perform_analysis()
        elif choice == 4:
            routes.start_route()
        elif choice == 0:
            print("\n## Returning to Main Menu...")
            break
        else:
            print("\n### Invalid Choice, Please try again...")

def chart_hr(): 
    heart_rate_data = [65, 66, 70, 80, 88, 90, 93, 100, 102, 109, 115, 130, 140, 139, 145, 146, 148, 152, 160, 166, 171, 169, 170, 169, 164, 160, 158, 155, 150, 149, 145, 143, 135, 129, 110, 105, 101, 97, 93, 90, 88, 75]
    average_heart_rate, max_heart_rate = charts_hr.calculate_statistics(heart_rate_data)

    print("\nOpen Heart Rate Chart")
    charts_hr.plot_heart_rate_chart(heart_rate_data, average_heart_rate, max_heart_rate)
    print("Close Heart Rate Chart")

def perform_analysis():
    age = 40
    heart_rate_data = [65, 66, 70, 80, 88, 90, 93, 100, 102, 109, 115, 130, 140, 139, 145, 146, 148, 152, 160, 166, 171, 169, 170, 169, 164, 160, 158, 155, 150, 149, 145, 143, 135, 129, 110, 105, 101, 97, 93, 90, 88, 75]
    resting_heart_rate = 60

    performance_analysis.heart_rate_zones(age, heart_rate_data)
    max_heart_rate = performance_analysis.max_heartrate(heart_rate_data)
    vo2max = performance_analysis.calculate_vo2max(max_heart_rate, resting_heart_rate)
    print(f"\nVO2 Max\t\t\t: {vo2max:.2f}")

    peak_heart_rate = max_heart_rate
    heart_rate_after_one_minute = heart_rate_data[-1]
    heart_rate_recovery = performance_analysis.calculate_heart_rate_recovery(peak_heart_rate, heart_rate_after_one_minute)
    print(f"Heart Rate Recovery\t: {heart_rate_recovery:.2f} bpm")

def heart_rate():
    start_time = hr_chart.datetime.strptime('2023-01-01 08:00:00', '%Y-%m-%d %H:%M:%S')
    interval = 5
    additional_heart_rate_data = [
        65, 66, 70, 80, 88, 90, 93, 100, 102, 109, 115, 130, 140, 139, 145, 146, 148, 152, 160, 166, 171, 169, 170,
        169, 164, 160, 158, 155, 150, 149, 145, 143, 135, 129, 110, 105, 101, 97, 93, 90, 88, 75
    ]

    print("\n=== Heart Rate ===")
    print("\nOpen Heart Rate Chart")
    hr_chart.create_and_plot_heart_rate_chart(start_time, interval, additional_heart_rate_data)
    print("Close Heart Rate Chart")

def sleep_record():
    heart_rate_data = [
        55, 53, 50, 52, 48, 45, 47, 43, 41, 42, 44, 41, 46, 56, 60, 59, 62, 66, 75
    ]
    sleep_hours = 8

    sleep_stats = calculate_sleep_stats(heart_rate_data, sleep_hours)
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

def weight_management():
    while True:
        print("\n\n=== Weight Management ===")
        print("1. Calorie Record\n2. Food Calorie\n3. Set Goal\n4. Weight Record\n0. Back to Main Menu")

        choice = int(input("Choose an option (1/2/3/4/0): "))
        if choice == 1:
            calorie_tracking()
        elif choice == 2:
            food_calorie.main()
        elif choice == 3:
            set_weight_goal()
        elif choice == 4:
            set_weight_record()
        elif choice == 0:
            print("\n## Returning to Main Menu...")
            break
        else:
            print("\n### Invalid Choice, Please try again...")

def calorie_tracking():
    tracker = calorie_record.CalorieTracker()
    updated_tracker = tracker.add_record(burned_calories=300, consumed_calories=500)
    updated_tracker.display_totals()

def set_weight_goal():
    initial_weight = 70.0
    goal = 'lose'
    target_weight = 65.0
    completed_by = '2023-12-31'
    height_cm = 175
    age = 30
    gender = 'male'
    activity_level = 'moderately_active'
    
    print("\n=== Set Weight Goal ===")
    result_advanced = set_goal.calculate_calorie_deficit_advanced(
        initial_weight, goal, target_weight, completed_by, height_cm, age, gender, activity_level
    )

    for key, value in result_advanced.items():
        print(f"{key}: {value}")

def set_weight_record():
    weight_data = [] 
    result_weight = weight_record.add_record_weight(weight_data)
    weight_record.display_records(result_weight)

login()