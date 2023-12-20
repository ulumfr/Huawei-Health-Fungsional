from datetime import datetime

def calculate_duration(start_time, end_time):
    start_datetime = parse_time(start_time)
    end_datetime = parse_time(end_time)
    duration_minutes = calculate_minutes_between_datetimes(start_datetime, end_datetime)
    return int(duration_minutes)

def calculate_calories_burned(duration, average_heart_rate, weight, age, gender):
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

def main():
    heart_rate_data = [65, 66, 70, 80, 88, 90, 93, 100, 102, 109, 115, 130, 140, 139, 145, 146, 148, 152, 160, 166, 171, 169, 170,
                       169, 164, 160, 158, 155, 150, 149, 145, 143, 135, 129, 110, 105, 101, 97, 93, 90, 88, 75]

    start_time = input("Mulai Latihan - Masukkan waktu mulai (hh:mm:ss): ")
    end_time = input("Latihan Selesai - Masukkan waktu selesai (hh:mm:ss): ")

    weight = float(input("Masukkan berat badan (kg): "))
    age = int(input("Masukkan usia (tahun): "))
    gender = input("Masukkan jenis kelamin (women/men): ")

    duration = calculate_duration(start_time, end_time)

    average_heart_rate = calculate_average_heart_rate(heart_rate_data)

    calories_burned = calculate_calories_burned(duration, average_heart_rate, weight, age, gender)

    print("\n=== Hasil Rekaman Latihan ===")
    print(f"Durasi Latihan: {duration} menit")
    print(f"Kalori Terbakar: {calories_burned} kalori")
    print(f"Rata-rata Heart Rate: {average_heart_rate} BPM")

main()
