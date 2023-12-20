from HeartRate.heartrate_chart import create_and_plot_heart_rate_chart

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

def login():
    while True:
        print("\n===== LOGIN HUAWEI HEALTH =====")
        email = input("\nEmail\t : ")
        password = input("Password : ")
        
        if email in dummy_account["users"] and password == dummy_account["users"][email]["password"]:
            nama = dummy_account["users"][email]["name"]
            print("\n===============================")
            print(f"\n\nSelamat Datang, {nama}")
            huawei_dashboard(email)
        else: 
            print("\n### Account tidak ditemukan, Coba lagi...")

def huawei_dashboard(email):
    while True:
        print("\n=== Huawei Dashboard ===")
        print("1. Exercise Record\n2. Heart Rate\n3. Sleep Record\n4. Weight Management\n0. Logout")
        
        pilih = int(input("Pilih menu (1/2/3/4/0): "))
        if pilih == 1:
            exercise_record()
        elif pilih == 2:
            heart_rate()
        elif pilih == 3:
            sleep_record()
        elif pilih == 4:
            weight_management()
        elif pilih == 0:
            print("\n## Berhasil Logout..")
            login()
        else:
            print("\n### Pilihan tidak ada, Coba lagi...")
    
def exercise_record():
    print("hello ini exercise record")
    
def heart_rate():
    create_and_plot_heart_rate_chart()

def sleep_record():
    print("hello ini sleep record")
    
def weight_management():
    print("hello ini weight management")

login()