import matplotlib.pyplot as plt
import numpy as np

def start_route():
    return start_recording()

def start_recording():
    return record_gps()

def record_gps():
    return check_gps()

def check_gps():
    connection_gps = True
    if connection_gps:
        return start_mapping()
    else:
        return "No GPS Connection"

def start_mapping():
    return display_map()

def display_message(message):
    return f"Display Message: {message}"

def display_map():
    theta = np.linspace(0, 2*np.pi, 100)
    x = 16 * np.sin(theta)**3
    y = 13 * np.cos(theta) - 5 * np.cos(2*theta) - 2 * np.cos(3*theta) - np.cos(4*theta)

    plt.plot(x, y, marker='o')
    plt.title("Exercise Mapping with GPS Data")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.show()
