from datetime import datetime

def calculate_duration(start_time, end_time):
    start_datetime = parse_time(start_time)
    end_datetime = parse_time(end_time)
    duration_minutes = calculate_minutes_between_datetimes(start_datetime, end_datetime)
    return int(duration_minutes)

def calculate_calories_burned(duration, average_heart_rate, weight, age, gender, calories_burned=None):
    if calories_burned is None:
        calories_burned = 0

    if gender.lower() == 'women':
        calories_burned = (duration * (0.4472 * average_heart_rate - 0.1263 * weight + 0.074 * age - 20.4022)) / 4.184
    elif gender.lower() == 'men':
        calories_burned = (duration * (0.6309 * average_heart_rate + 0.1988 * weight + 0.2017 * age - 55.0969)) / 4.184
    else:
        raise ValueError("Invalid gender. Please enter 'women' or 'men'.")
    return calories_burned


def calculate_average_heart_rate(heart_rate_per_second):
    average_heart_rate = sum(heart_rate_per_second) / len(heart_rate_per_second)
    return round(average_heart_rate, 2)

def parse_time(time_string):
    return datetime.strptime(time_string, "%H:%M:%S")

def calculate_minutes_between_datetimes(start_datetime, end_datetime):
    return ((end_datetime - start_datetime).total_seconds()) / 60

