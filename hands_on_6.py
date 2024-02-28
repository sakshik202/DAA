import random

def partition(arr, low, high):
    pivot_value = arr[high]
    i = low - 1
    j = low
    while j < high:
        if arr[j] <= pivot_value:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        j += 1
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort_recursive(arr, low, high):
    while low < high:
        pivot_index = partition(arr, low, high)
        quicksort_recursive(arr, low, pivot_index - 1)
        low = pivot_index + 1

def quicksort_random_pivot(arr):
    quicksort_recursive(arr, 0, len(arr) - 1)

def quicksort_non_random_pivot(arr):
    quicksort_recursive(arr, 0, len(arr) - 1)

def generate_random_array(size):
    return [random.randint(0, 1000) for _ in range(size)]

def generate_sorted_array(size):
    return [i for i in range(size)]

def generate_reverse_sorted_array(size):
    return [size - i for i in range(size)]

# Usage examples
arr = generate_random_array(10)
print("Original array:", arr)
quicksort_random_pivot(arr)
print("Sorted array (random pivot):", arr)

arr = generate_random_array(10)
print("Original array:", arr)
quicksort_non_random_pivot(arr)
print("Sorted array (non-random pivot):", arr)
import random
import timeit
import matplotlib.pyplot as plt
import numpy as np

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    j = low
    while j < high:
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        j += 1
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    while low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        low = pi + 1

def quick_sort_random_pivot(arr):
    random.shuffle(arr)
    quick_sort(arr, 0, len(arr) - 1)

def benchmark(sort_func, input_generator, input_sizes, repetitions=5):
    avg_runtimes = []
    for size in input_sizes:
        runtimes = []
        i = 0
        while i < repetitions:
            arr = input_generator(size)
            runtime = timeit.timeit(lambda: sort_func(arr.copy()), number=1)
            runtimes.append(runtime)
            i += 1
        avg_runtime = np.mean(runtimes)
        avg_runtimes.append(avg_runtime)
    return avg_runtimes

def generate_best_case_input(size):
    return list(range(size))

def generate_worst_case_input(size):
    return list(range(size, 0, -1))

def generate_average_case_input(size):
    return random.sample(range(size), size)

input_sizes = [100, 500, 1000, 5000, 10000]
repetitions = 3

# Benchmarking non-random pivot quicksort
avg_runtimes_best_case = benchmark(quick_sort, generate_best_case_input, input_sizes, repetitions)
avg_runtimes_worst_case = benchmark(quick_sort, generate_worst_case_input, input_sizes, repetitions)
avg_runtimes_average_case = benchmark(quick_sort, generate_average_case_input, input_sizes, repetitions)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(input_sizes, avg_runtimes_best_case, label='Best Case')
plt.plot(input_sizes, avg_runtimes_worst_case, label='Worst Case')
plt.plot(input_sizes, avg_runtimes_average_case, label='Average Case')
plt.title('Quicksort Non-Random Pivot Benchmarks')
plt.xlabel('Input Size')
plt.ylabel('Average Runtime (s)')
plt.legend()
plt.grid(True)
plt.show()
