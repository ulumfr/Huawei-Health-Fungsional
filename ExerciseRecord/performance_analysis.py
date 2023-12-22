def heart_rate_zones(age, heart_rate_data):
    max_heart_rate = calculate_max_heart_rate(age)
    zones = calculate_heart_rate_zones(max_heart_rate)
    
    print_heart_rate_zones(zones)
    
    for heart_rate in heart_rate_data:
        zone = get_heart_rate_zone(heart_rate, zones)
        print(f"Heart Rate: {heart_rate} bpm - Zone: {zone}")
    return heart_rate_data

def calculate_max_heart_rate(age):
    return 220 - age

def calculate_heart_rate_zones(max_heart_rate):
    return {
        'Recovery\t  ': (0.5 * max_heart_rate, 0.6 * max_heart_rate),
        'Aerobic\t\t  ': (0.6 * max_heart_rate, 0.7 * max_heart_rate),
        'Aerobic/Anaerobic ': (0.7 * max_heart_rate, 0.8 * max_heart_rate),
        'Anaerobic\t  ': (0.8 * max_heart_rate, 0.9 * max_heart_rate),
        'Maximal\t\t  ': (0.9 * max_heart_rate, 1.0 * max_heart_rate),
    }

def print_heart_rate_zones(zones):
    for zone, (lower, upper) in zones.items():
        print(f"{zone}: {lower:.2f} - {upper:.2f} bpm")
    return zones

def get_heart_rate_zone(heart_rate, zones):
    for zone, (lower, upper) in zones.items():
        if lower <= heart_rate <= upper:
            return zone
    return "Unknown"

def calculate_vo2max(max_heart_rate, resting_heart_rate):
    vo2max = (max_heart_rate / resting_heart_rate) * 15.3
    return vo2max

def calculate_heart_rate_recovery(peak_heart_rate, heart_rate_after_one_minute):
    heart_rate_recovery = peak_heart_rate - heart_rate_after_one_minute
    return heart_rate_recovery

def max_heartrate(heart_rate_data):
    return max(heart_rate_data)

def min_heartrate(heart_rate_data):
    return min(heart_rate_data)