def heart_rate_zones(age, heart_rate_data):
    max_heart_rate = calculate_max_heart_rate(age)
    zones = calculate_heart_rate_zones(max_heart_rate)
    
    print_heart_rate_zones(zones)

    print("\nHeart Rate Data Analysis:")
    for heart_rate in heart_rate_data:
        zone = get_heart_rate_zone(heart_rate, zones)
        print(f"Heart Rate: {heart_rate} bpm - Zone: {zone}")

def calculate_max_heart_rate(age):
    return 220 - age

def calculate_heart_rate_zones(max_heart_rate):
    return {
        'Recovery': (0.5 * max_heart_rate, 0.6 * max_heart_rate),
        'Aerobic': (0.6 * max_heart_rate, 0.7 * max_heart_rate),
        'Aerobic/Anaerobic': (0.7 * max_heart_rate, 0.8 * max_heart_rate),
        'Anaerobic': (0.8 * max_heart_rate, 0.9 * max_heart_rate),
        'Maximal': (0.9 * max_heart_rate, 1.0 * max_heart_rate),
    }

def print_heart_rate_zones(zones):
    print("Heart Rate Training Zones:")
    for zone, (lower, upper) in zones.items():
        print(f"{zone}: {lower:.2f} - {upper:.2f} bpm")

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

age = 40
heart_rate_data = [65, 66, 70, 80, 88, 90, 93, 100, 102, 109, 115, 130, 140, 139, 145, 146, 148, 152, 160, 166, 171, 169, 170,
                   169, 164, 160, 158, 155, 150, 149, 145, 143, 135, 129, 110, 105, 101, 97, 93, 90, 88, 75]
resting_heart_rate = 60

heart_rate_zones(age, heart_rate_data)

max_heart_rate = max_heartrate(heart_rate_data)
vo2max = calculate_vo2max(max_heart_rate, resting_heart_rate)
print(f"\nVO2 Max: {vo2max:.2f}")

peak_heart_rate = max_heart_rate
heart_rate_after_one_minute = heart_rate_data[-1]  # Assuming the last heart rate is the last data in the array
heart_rate_recovery = calculate_heart_rate_recovery(peak_heart_rate, heart_rate_after_one_minute)
print(f"Heart Rate Recovery: {heart_rate_recovery:.2f} bpm")
