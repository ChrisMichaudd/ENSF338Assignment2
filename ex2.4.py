import json
import matplotlib.pyplot as plt
import time
import sys
sys.setrecursionlimit(20000)
#---------------------------------ADDED-------------------------------------#
with open("ex2.json", "r") as f:
    file_data = json.load(f)
#---------------------------------ADDED-------------------------------------#

#---------------------------------CHANGED-------------------------------------#

import random

def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi - 1)
        func1(arr, pi + 1, high)

def func2(array, start, end):
    pivot_index = random.randint(start, end)
    pivot = array[pivot_index]
    array[pivot_index], array[start] = array[start], array[pivot_index]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= pivot:
            high = high - 1
        while low <= high and array[low] <= pivot:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high

#---------------------------------CHANGED-------------------------------------#

#---------------------------------SAME-------------------------------------#
#array = file_data[0]
#start_time = time.perf_counter()
#func1(array, 0, len(array) - 1)
#end_time = time.perf_counter()
#time_taken = end_time - start_time

array_ = []
indexes = []

for i in range(len(file_data)):
    arr = file_data[i]
    start_time = time.perf_counter()
    func1(file_data[i], 0, len(file_data[i]) - 1)
    end_time = time.perf_counter()
    
    time_taken = end_time - start_time
    array_.append(time_taken)
    indexes.append(len(arr))
    
print("Time taken: ", time_taken, "seconds")

plt.plot(indexes, array_)
plt.title(" Optimized Line Graph of Quicksort List by pivot randomization")
plt.xlabel("Indexes used")
plt.ylabel("Time taken")
plt.show()
#---------------------------------SAME-------------------------------------#