import matplotlib.pyplot as plt
import numpy as np

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