def calculate_sleep_stats(heart_rate_data, sleep_hours):
    total_minutes = sleep_hours * 60

    deep_sleep_percentage = calculate_percentage(heart_rate_data, 40, 50)
    light_sleep_percentage = calculate_percentage(heart_rate_data, 50, 60)
    rem_sleep_percentage = calculate_percentage(heart_rate_data, 60, float('inf'))

    total_sleep_time = divmod(total_minutes, 60)

    return {
        "total_sleep_time": total_sleep_time,
        "deep_sleep_percentage": deep_sleep_percentage,
        "light_sleep_percentage": light_sleep_percentage,
        "rem_sleep_percentage": rem_sleep_percentage
    }

def calculate_percentage(data, lower_limit, upper_limit):
    valid_data = [value for value in data if lower_limit <= value <= upper_limit]
    percentage = (len(valid_data) / len(data)) * 100 if len(data) > 0 else 0
    return round(percentage, 2)

def analyze_sleep_quality(stats):
    deep_sleep_indicator = "Normal" if stats["deep_sleep_percentage"] >= 10 else "Low"
    light_sleep_indicator = "Normal" if stats["light_sleep_percentage"] >= 60 else "Low"
    rem_sleep_indicator = "Normal" if stats["rem_sleep_percentage"] >= 20 else "Low"

    return {
        "deep_sleep_indicator": deep_sleep_indicator,
        "light_sleep_indicator": light_sleep_indicator,
        "rem_sleep_indicator": rem_sleep_indicator
    }