import datetime

def add_record_weight(data):
    print("\n=== Input Record Weight ===")
    date = input("Enter date (format: YYYY-MM-DD)\t\t: ")
    time = input("Enter time (format: HH:MM)\t\t: ")
    weight = float(input("Enter weight (kg)\t\t\t: "))

    body_fat_input = input("Enter body fat percentage (optional)\t: ")
    body_fat = float(body_fat_input) if body_fat_input else None

    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        raise ValueError("The date format is incorrect. Please use YYYY-MM-DD format.")

    new_record = {
        'date': date,
        'time': time,
        'weight': weight,
        'body_fat': body_fat
    }

    return data + [new_record]

def display_records(data):
    print("\nList of Weight Records:")
    print("----------------------------")
    for record in data:
        print(f"Date: {record['date']}, Time: {record['time']}, Weight: {record['weight']} kg, Body Fat: {record['body_fat']}%")
