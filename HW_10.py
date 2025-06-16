import time
import random
import numpy as np
import matplotlib.pyplot as plt

def deterministic_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # Вибір середнього елемента як опорного
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return deterministic_quick_sort(left) + middle + deterministic_quick_sort(right)

def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)  # Випадковий вибір опорного елемента
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)

def measure_time(sort_func, arr, runs=5):
    times = []
    for _ in range(runs):
        arr_copy = arr.copy()
        start_time = time.time()
        sort_func(arr_copy)
        times.append(time.time() - start_time)
    return np.mean(times)

# Розміри масивів для тестування
sizes = [10_000, 50_000, 100_000, 500_000]
randomized_times = []
deterministic_times = []

for size in sizes:
    test_array = [random.randint(0, 10**6) for _ in range(size)]
    rand_time = measure_time(randomized_quick_sort, test_array)
    det_time = measure_time(deterministic_quick_sort, test_array)
    randomized_times.append(rand_time)
    deterministic_times.append(det_time)
    print(f"Розмір масиву: {size}")
    print(f"  Рандомізований QuickSort: {rand_time:.4f} секунд")
    print(f"  Детермінований QuickSort: {det_time:.4f} секунд")


import matplotlib
matplotlib.use('TkAgg')  # Використання інтерфейсу для відображення в PyCharm

# Побудова графіка
plt.figure(figsize=(8, 6))
plt.plot(sizes, randomized_times, label="Рандомізований QuickSort", color='blue')
plt.plot(sizes, deterministic_times, label="Детермінований QuickSort", color='orange')
plt.xlabel("Розмір масиву")
plt.ylabel("Середній час виконання (секунди)")
plt.title("Порівняння рандомізованого та детермінованого QuickSort")
plt.legend()
plt.grid()
plt.show()
