import psutil
import time

def measure_energy_consumption():
    # Initialize a CPU usage object
    cpu_usage = psutil.cpu_percent(interval=1)  # 1-second interval

    while True:
        # Update CPU usage
        cpu_usage = psutil.cpu_percent(interval=1)

        # Perform your project's computations here

        print(f"Current CPU Usage: {cpu_usage}%")

        # Add a delay to simulate real-time processing
        time.sleep(5)

if __name__ == "__main__":
    measure_energy_consumption()
