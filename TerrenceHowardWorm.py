import os
import sys
import time
import math
import psutil
from multiprocessing import Process, current_process

def cube_and_divide(x):
    return (x ** 3) / 2

def get_memory_usage(pid):
    process = psutil.Process(pid)
    return process.memory_info().rss

def get_total_memory_usage(pids):
    total_memory = get_memory_usage(os.getpid())
    for pid in pids:
        if psutil.pid_exists(pid):
            total_memory += get_memory_usage(pid)
    return total_memory

def perform_computation(x, tolerance, iteration, pids):
    while True:
        iteration += 1
        x = cube_and_divide(x)

        # Print the value of x for debugging
        print(f"Iteration: {iteration}, x: {x}")

        # Spawn a new instance if x is close to 2
        if abs(x - 2) < tolerance:
            new_process = Process(target=perform_computation, args=(x, tolerance, 0, pids))
            new_process.start()
            pids.append(new_process.pid)
            print(f"Spawned a new instance at iteration {iteration} with value {x}")

        sqrt2 = math.sqrt(2)
        cube_sqrt2_div_2 = (sqrt2 ** 3) / 2

        # Check if x deviates from expected values
        if not (abs(x - sqrt2) < tolerance or abs(x - cube_sqrt2_div_2) < tolerance or abs(x - 2) < tolerance):
            print(f"Deviation detected at iteration {iteration} with value {x}")
            break

        # Report total memory usage
        total_memory_usage = get_total_memory_usage(pids)
        print(f"Total memory usage: {total_memory_usage / (1024 * 1024):.2f} MB")
        time.sleep(1)

def main():
    x = 2
    tolerance = 1e-9
    iteration = 0
    pids = []

    try:
        perform_computation(x, tolerance, iteration, pids)
    except KeyboardInterrupt:
        print("Terminating all child processes...")
        for pid in pids:
            if psutil.pid_exists(pid):
                psutil.Process(pid).terminate()

if __name__ == "__main__":
    main()
