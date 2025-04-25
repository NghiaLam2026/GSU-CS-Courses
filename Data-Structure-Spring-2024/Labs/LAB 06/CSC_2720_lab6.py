#Nghia Lam
#CSC 2720 Lab 014
#Lab time: 2:15 PM
#Due time: 02/18/2024 @ 11:59PM

def quick_sort(arr, low, high):
    if low < high: #Base case
        pi = partition(arr, low, high) #Partition the array around a pivot and get hte pivot index
        quick_sort(arr, low, pi-1) #Recursively sort elemnts before and after paritition
        quick_sort(arr, pi + 1, high) #Recursively sort elemnts before and after paritition

def partition(arr, low, high):
    pivot = arr[high] #Select the last element as pivot
    i = low - 1 #Pointer for the smaller element index
    for ind in range(low, high):
        if arr[ind] < pivot: #If current element is smaller than or equal to pivot
            i += 1
            arr[i], arr[ind] = arr[ind], arr[i] #Swapping the element
    arr[i + 1], arr[high] = arr[high], arr[i + 1] #Swapping the pivot element with the element at i + 1 position
    return i + 1 #Return the partitioning index

def deduplicate_sorted_array(arr):
    i = 0
    while i < len(arr) - 1: #Iterate thourhg the array to find duplicates
        if arr[i] == arr[i + 1]: #Of duplicate is found, remove it by pop()
            arr.pop(i)
        else:
             i += 1
    return arr

def sorted_deduplication(arr):
    if arr is None:
        return "Null"
    quick_sort(arr, 0, len(arr) - 1)
    deduplicated_array = deduplicate_sorted_array(arr)
    return deduplicated_array

print(sorted_deduplication([50, 11, 33, 21, 40, 50, 40, 40, 21])) #Normal test case
print(sorted_deduplication([])) #Empty test case
print(sorted_deduplication([5, 5, 5, 5])) #Same element test case
print(sorted_deduplication([-3, -1, 2, -3, 4, -1, 2, 4])) #Negative number test case