import matplotlib.pyplot as plt
import numpy as np

def mulai_route():
    print("Mulai Route Exercise")
    mulai_perekaman()

def mulai_perekaman():
    print("Mulai Perekaman Latihan")
    rekam_gps_data()

def rekam_gps_data():
    print("Rekam GPS Data")
    cek_koneksi_gps()

def cek_koneksi_gps():
    print("Memeriksa Koneksi GPS")
    koneksi_gps = True
    if koneksi_gps:
        mulai_pemetaan_latihan()
    else:
        print("Tidak Ada Koneksi GPS")
        tampilkan_pesan("Tidak Ada Koneksi")

def mulai_pemetaan_latihan():
    print("Mulai Pemetaan Latihan")
    tampilkan_peta()

def tampilkan_pesan(pesan):
    print(f"Tampilkan Pesan: {pesan}")

def tampilkan_peta():
    print("Tampilkan Peta dengan GPS Data")

    theta = np.linspace(0, 2*np.pi, 100)
    x = 16 * np.sin(theta)**3
    y = 13 * np.cos(theta) - 5 * np.cos(2*theta) - 2 * np.cos(3*theta) - np.cos(4*theta)

    plt.plot(x, y, marker='o')
    plt.title("Pemetaan Latihan dengan GPS Data")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.show()

    selesai_rekaman()

def selesai_rekaman():
    print("Selesai Rekaman Latihan")

mulai_route()
