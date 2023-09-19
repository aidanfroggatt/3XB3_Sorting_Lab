"""
This file corresponds to the first graded lab of 2XC3.
Feel free to modify and/or add functions to this file.
"""
import random
import time

# Create a random list length "length" containing whole numbers between 0 and max_value inclusive
def create_random_list(length, max_value):
    return [random.randint(0, max_value) for _ in range(length)]


# Creates a near sorted list by creating a random list, sorting it, then doing a random number of swaps
def create_near_sorted_list(length, max_value, swaps):
    L = create_random_list(length, max_value)
    L.sort()
    for _ in range(swaps):
        r1 = random.randint(0, length - 1)
        r2 = random.randint(0, length - 1)
        swap(L, r1, r2)
    return L


# I have created this function to make the sorting algorithm code read easier
def swap(L, i, j):
    L[i], L[j] = L[j], L[i]


# ******************* Insertion sort code *******************

# This is the traditional implementation of Insertion Sort.
def insertion_sort(L):
    for i in range(1, len(L)):
        insert(L, i)


# INSERTION SORT 2
def insertion_sort2(L):
    for i in range(1, len(L)):
        current_value = L[i]
        j = i - 1
        # Move elements of L[0..i-1], that are greater than current_value,
        # to one position ahead of their current position
        while j >= 0 and current_value < L[j]:
            L[j + 1] = L[j]
            j -= 1
        # Insert the current_value at the correct position
        L[j + 1] = current_value
    return L


def insert(L, i):
    while i > 0:
        if L[i] < L[i - 1]:
            swap(L, i - 1, i)
            i -= 1
        else:
            return


# ******************* Bubble sort code *******************

# Traditional Bubble sort
def bubble_sort(L):
    for i in range(len(L)):
        for j in range(len(L) - 1):
            if L[j] > L[j + 1]:
                swap(L, j, j + 1)


def bubble_sort2(L):
    n = len(L)
    for i in range(n):
        # This will be the position where the largest number will be placed
        position_to_insert = n - 1 - i
        max_index = 0

        # Find the largest number and its index
        for j in range(1, position_to_insert + 1):
            if L[j] > L[max_index]:
                max_index = j

        # Shift elements to the left of position_to_insert and right of max_index by 1
        temp = L[max_index]
        for k in range(max_index, position_to_insert):
            L[k] = L[k + 1]

        # Place the largest number at position_to_insert
        L[position_to_insert] = temp
    return L

# ******************* Selection sort code *******************

# Traditional Selection sort
def selection_sort(L):
    for i in range(len(L)):
        min_index = find_min_index(L, i)
        swap(L, i, min_index)


def find_min_index(L, n):
    min_index = n
    for i in range(n + 1, len(L)):
        if L[i] < L[min_index]:
            min_index = i
    return min_index


def multiple_runs(n):
    total_time = 0
    for i in range(n):
        start = time.time()
        # set sort method (insertion, bubble, selection) just replace function call below
        bubble_sort2(create_random_list(2000, 1000))
        end = time.time()
        total_time += (end - start)
    print("total elapsed time: ", total_time,
          "\nnumber of runs: ", n,
          "\naverage time:", total_time/n)


multiple_runs(100)