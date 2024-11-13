import random
import time 

def generate_sorted_data(size):
    '''create a small data set'''
    small_data = [random.randint(1, 100) for i in range(size)]

    '''Begin insertion sort'''
    for i in range(1, len(small_data)):
        key = small_data[i]
       
        j = i - 1
        while j >= 0 and small_data[j] > key:
            small_data[j + 1] = small_data[j]
            j -= 1
        small_data[j + 1] = key
    
    '''Create a new array with 1000 elements which combines the previous array named large_data'''
    large_data = small_data + [random.randint(1,100) for l in range(1000 - size)]
    merge_sort(large_data)
    return large_data, small_data
    
    
    

def merge_sort(arr):
    '''merge sort'''
    if len(arr) > 1:
        mid = len(arr) // 2 
        left_half = arr[:mid]  
        right_half = arr[mid:]

        merge_sort(left_half)  
        merge_sort(right_half)  

    
        i = 0
        j = 0
        k = 0

        
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def binary_search(sorted_data, target):
    '''Binary search to locate the index position of a specified value'''
    start = 0
    end = len(sorted_data) - 1
    while start <= end:
        mid = (start + end) // 2
        if sorted_data[mid] == target:
            return mid
        elif sorted_data[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return None

def linear_search(sorted_data, target):
    '''Linear search to check if target is present in the sorted array'''

    for i in range(len(sorted_data))  :
        if sorted_data[i] == target:
            return i
        
    return None
    

def main():
    
    large_data,small_data = generate_sorted_data(10)
    print(large_data)
    

    target = int(input("Enter the target number you are searching for: "))
    print(small_data)
    Binary_result=binary_search(small_data,target)
    if Binary_result==None:
        print("Target value was not found")
    else:
        print(target, "was found at", Binary_result)

    '''Linear search'''
    start_time = time.perf_counter()
    index = linear_search(large_data, target)
    end_time = time.perf_counter()

    linear_search_time = end_time - start_time
    if index is None:
        print(f"Target : {target}(Expected result: None, as it is not in the array completed in : {linear_search_time})")

    else:
        print(f"Linear Search: Target {target} found at index {index} completed in : {linear_search_time}")
        
    
    '''Binarysearch'''
    start_time = time.perf_counter()
    binary_index = binary_search(large_data, target)
    end_time = time.perf_counter()

    binary_search_time = end_time - start_time

    if binary_index is not None:
        print(f"Binary Search: Target {target} found at index {binary_index} completed in : {binary_search_time}")
    else:
        print(f"Binary Search: Target {target} not found completed in : {binary_search_time}")

    '''Which searching algorithm is more efficient'''
    if binary_search_time > linear_search_time:
        print("Linear search is more efficient as it requires less time in worse case ")
    else:
        print("Binary search is more efficient as it requires less time in worse case")


if __name__ == "__main__":
    main()
'''The choice of searching algorithms is very important as it effects the overll efficiency and speed of
the program. Suppose you had a list of 10 elements and the target integer is located in the first position, 
linear search would be the most efficient solution as it is the best case. However if there was a list with 
10,000 elements linear search would need to go through each and every element in the array in order to find it
while in binary search it immediately reduces the possible results to half, if the target isnt located in the middle. 
This increased efficiency results in a faster excecution time and improved performance'''