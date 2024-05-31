import math
import time
import subprocess
import os
import psutil

# Function to compute the cube of a number and divide it by 2
def cube_and_divide(x):
    return (x ** 3) / 2

# Function to get the memory usage of the current process
def get_memory_usage():
    process = psutil.Process(os.getpid())
    memory_info = process.memory_info()
    return memory_info.rss  # Resident Set Size (physical memory usage)

# Function to get the total memory usage of the current process and its child processes
def get_total_memory_usage(child_pids):
    total_memory = get_memory_usage()  # Start with the memory of the parent process
    for pid in child_pids:
        try:
            child_process = psutil.Process(pid)
            total_memory += child_process.memory_info().rss
        except psutil.NoSuchProcess:
            pass  # Ignore if the process no longer exists
    return total_memory

# Main function to run the script
def main():
    x = 2
    expected_values = {math.sqrt(2), (math.sqrt(2) ** 3) / 2, 2}
    tolerance = 1e-9

    iteration = 0
    script_name = os.path.basename(__file__)
    child_pids = []

    try:
        while True:
            iteration += 1
            x = cube_and_divide(x)
            
            if abs(x - 2) < tolerance:
                # Spawn a new instance of the script
                child_process = subprocess.Popen(["python", __file__])
                child_pids.append(child_process.pid)
                print(f"Spawned a new instance at iteration {iteration} with value 2")

            if not any(abs(x - ev) < tolerance for ev in expected_values):
                print(f"Deviation detected at iteration {iteration} with value {x}")
                break
            
            total_memory_usage = get_total_memory_usage(child_pids)
            print(f"{script_name} - Total memory usage: {total_memory_usage / (1024 ** 2):.2f} MB")
            time.sleep(1)
    except KeyboardInterrupt:
        # Clean up child processes on exit
        for pid in child_pids:
            try:
                os.kill(pid, signal.SIGTERM)
            except Exception as e:
                print(f"Error terminating process {pid}: {e}")

if __name__ == "__main__":
    main()
