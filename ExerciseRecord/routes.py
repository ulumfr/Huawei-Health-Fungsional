import matplotlib.pyplot as plt
import numpy as np

def start_route():
    print("\n=== Routes Exercise ===")
    print("Start Exercise Route")
    start_recording()

def start_recording():
    print("Start Exercise Recording")
    record_gps()

def record_gps():
    print("Record GPS Data")
    check_gps()

def check_gps():
    print("Checking GPS Connection")
    connection_gps = True
    if connection_gps:
        start_mapping()
    else:
        print("No GPS Connection")
        display_message("No Connection")

def start_mapping():
    print("Start Exercise Mapping")
    display_map()

def display_message(message):
    print(f"Display Message: {message}")

def display_map():
    print("Display Map with GPS Data")

    theta = np.linspace(0, 2*np.pi, 100)
    x = 16 * np.sin(theta)**3
    y = 13 * np.cos(theta) - 5 * np.cos(2*theta) - 2 * np.cos(3*theta) - np.cos(4*theta)

    plt.plot(x, y, marker='o')
    plt.title("Exercise Mapping with GPS Data")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.show()

    recording_complete()

def recording_complete():
    print("Exercise Recording Completed")
