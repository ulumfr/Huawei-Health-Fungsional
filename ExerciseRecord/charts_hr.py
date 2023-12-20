import matplotlib.pyplot as plt
import numpy as np


heart_rate_data = [65, 66, 70, 80, 88, 90, 93, 100, 102, 109, 115, 130, 140, 139, 145, 146, 148, 152, 160, 166, 171, 169, 170, 169, 164, 160, 158, 155, 150, 149, 145, 143, 135, 129, 110, 105, 101, 97, 93, 90, 88, 75]

def calculate_statistics(heart_rate_data):
    average_heart_rate = np.mean(heart_rate_data)
    max_heart_rate = np.max(heart_rate_data)
    return average_heart_rate, max_heart_rate

def plot_heart_rate_chart(heart_rate_data, average_heart_rate, max_heart_rate):

    plt.figure(figsize=(10, 5))
    plt.plot(range(len(heart_rate_data)), heart_rate_data, marker='o', color='green', label='Heart Rate')
    plt.legend([f'Average: {average_heart_rate:.2f}\nMaximum: {max_heart_rate}'], loc='upper left')
    plt.title("Heart Rate Over Time")
    plt.xlabel("Time (minutes)")
    plt.ylabel("Heart Rate")
    plt.grid(True)
    plt.show()

heart_rate_data = heart_rate_data
average_heart_rate, max_heart_rate = calculate_statistics(heart_rate_data)
plot_heart_rate_chart(heart_rate_data, average_heart_rate, max_heart_rate)
