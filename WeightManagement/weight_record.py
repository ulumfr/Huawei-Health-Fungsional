import datetime

def add_record_weight(data):
    
    date = input("Masukkan tanggal (format: YYYY-MM-DD): ")
    time = input("Masukkan jam (format: HH:MM): ")
    weight = float(input("Masukkan berat badan (kg): "))


    body_fat_input = input("Masukkan persentase lemak tubuh (opsional): ")
    body_fat = float(body_fat_input) if body_fat_input else None

    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Format tanggal tidak benar. Gunakan format YYYY-MM-DD.")

    new_record = {
        'date': date,
        'time': time,
        'weight': weight,
        'body_fat': body_fat
    }

    return data + [new_record]

def display_records(data):

    print("\nDaftar Rekaman Berat Badan:")
    print("----------------------------")
    for record in data:
        print(f"Tanggal: {record['date']}, Jam: {record['time']}, Berat: {record['weight']} kg, Lemak Tubuh: {record['body_fat']}%")


data_berat_badan = [] 

data_berat_badan = add_record_weight(data_berat_badan)

display_records(data_berat_badan)
