#Nghia Lam
#CSC 2720 Lab 014
#Lab time: 2:15 PM
#Due time: 02/11/2024 @ 11:59PM


def merge_sort(arr):
    if len(arr) <= 1: #This is the base case. If the list is empty or contains a single element, it is already sorted
        return arr
    
    mid = len(arr) // 2 #Find the middle index of the list
    left_half = merge_sort(arr[:mid]) #All of the element up to mid but does not include mid
    right_half = merge_sort(arr[mid:]) #All of the element from mid to the end of the array

    sorted_array = merge(left_half, right_half)
    return deduplicate(sorted_array) #Call dedplication on the sorted array

def merge(left, right):
    sorted_array = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right): #Continue looping until we reach the end of either left or right list.
        if left[left_index] < right[right_index]: #Compare the elements at the current indices of the left and right lists.
            sorted_array.append(left[left_index]) #Append the smaller element to the sorted list.
            left_index += 1 #Move the pointer forward in the left list.
        else:
            sorted_array.append(right[right_index]) #Append the smaller element to the sorted list.
            right_index += 1 #Move the poitner fowrard in the right list

    #Append any remaining elements from either lsit
    sorted_array.extend(left[left_index:])
    sorted_array.extend(right[right_index:])

    return sorted_array

def deduplicate(arr):
    # Check if the array is empty or has a single element
    if len(arr) < 2:
        return arr
    
    write_index = 1 # Start from the second element
    for i in range(1, len(arr)): #Iterate through the array starting from the second element
        if arr[i] != arr[i-1]: #If the current element is not equal to the previous, it means the current element is unique.
            arr[write_index] = arr[i] #Write the unique element to the write_index position
            write_index += 1 #Increment write_index to prepare for the next unique element.

    return arr[:write_index]
    


print(merge_sort([50, 11, 33, 21, 40, 50, 40, 40, 21])) #Normal test case
print(merge_sort([])) #Empty array test case
print(merge_sort([-1, 5, -10, 15, 20, -100])) #Negative number test case
print(merge_sort([1])) #Single digit test case

