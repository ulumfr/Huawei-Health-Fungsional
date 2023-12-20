import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from matplotlib.dates import HourLocator, DateFormatter

def extract_heart_rate_info(heart_rate_data):
    heart_rates = [data_point['heart_rate'] for data_point in heart_rate_data]
    timestamps = [datetime.strptime(data_point['timestamp'], '%Y-%m-%d %H:%M:%S') for data_point in heart_rate_data]
    max_heart_rate = max(heart_rates)
    min_heart_rate = min(heart_rates)
    heart_rate_range = f'{min_heart_rate}-{max_heart_rate} BPM'
    return heart_rates, timestamps, heart_rate_range, max_heart_rate, min_heart_rate

def configure_plot_axes():
    ax = plt.gca()
    ax.xaxis.set_major_locator(HourLocator())
    ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d %H:%M:%S'))

def format_legend_text(heart_rate_range, max_heart_rate, min_heart_rate):
    return f'Heart Rate Range: {heart_rate_range}\nHigh Heart Rate: {max_heart_rate} BPM\nLow Heart Rate: {min_heart_rate} BPM'

def plot_heart_rate_chart(heart_rates, timestamps, heart_rate_range, max_heart_rate, min_heart_rate):
    plt.plot(timestamps, heart_rates, label='Heart Rate (BPM)')
    plt.xlabel('Timestamp')
    plt.ylabel('Heart Rate (BPM)')
    plt.title('Heart Rate Chart')
    configure_plot_axes()
    legend_text = format_legend_text(heart_rate_range, max_heart_rate, min_heart_rate)
    plt.legend([legend_text])
    plt.xticks(rotation=15, ha="right")
    plt.show()

def generate_timestamps(start_time, interval, data_length):
    return [(start_time + timedelta(minutes=i * interval)).strftime('%Y-%m-%d %H:%M:%S') for i in range(data_length)]

def create_heart_rate_data(timestamps, heart_rate_values):
    return [{'timestamp': timestamp, 'heart_rate': heart_rate} for timestamp, heart_rate in zip(timestamps, heart_rate_values)]

def create_and_plot_heart_rate_chart(start_time, interval, heart_rate_values):
    timestamps = generate_timestamps(start_time, interval, len(heart_rate_values))
    heart_rate_data = create_heart_rate_data(timestamps, heart_rate_values)
    plot_heart_rate_chart(*extract_heart_rate_info(heart_rate_data))

start_time = datetime.strptime('2023-01-01 08:00:00', '%Y-%m-%d %H:%M:%S')
interval = 5
additional_heart_rate_data = [65, 66, 70, 80, 88, 90, 93, 100, 102, 109, 115, 130, 140, 139, 145, 146, 148, 152, 160, 166, 171, 169, 170,
                               169, 164, 160, 158, 155, 150, 149, 145, 143, 135, 129, 110, 105, 101, 97, 93, 90, 88, 75]

create_and_plot_heart_rate_chart(start_time, interval, additional_heart_rate_data)
