import datetime

def add_record_weight(data, date, time, weight, body_fat_input):
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
    for record in data:
        print(f"Date: {record['date']}, Time: {record['time']}, Weight: {record['weight']} kg, Body Fat: {record['body_fat']}%")
    return data
