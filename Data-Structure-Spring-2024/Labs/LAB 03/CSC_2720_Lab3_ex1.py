#Nghia Lam
#CSC 2720 Lab 014
#Lab time: 2:15 PM
#Due time: 01/28/2024 @ 11:59PM

def Bubble_sort(my_list):

    if my_list == []: #If my_list is empty, we return an empty list
        return []
    
    n = len(my_list) # Get the number of elements in the list

    swapped = True #Initialize a flag to track whether a swap has occured

    while swapped:
        #Set swapped to False at the start of each pass
        swapped = False 
        for i in range(1, n): #Iterate over the list, stopping on element before the end
            if my_list[i - 1] > my_list[i]: #Swap the elements
                my_list[i - 1], my_list[i] = my_list[i], my_list[i - 1] #Set swapped to True to indicate that a swap has occured
                swapped = True

        n -= 1 #After each pass, reduce n by 1 since the last element of the previous pass is now in the correct position

    return my_list
print(Bubble_sort([50, 11, 33, 21, 40, 50, 40, 40, 21])) #Normal unsorted list test case
print(Bubble_sort([])) #Empty list test case
print(Bubble_sort([50, -11, 33, 21, -40, -50, 40, 40, 21])) #Negative number list test case
print(Bubble_sort([5, 5, 5, 5, 5, 5, 5])) #All identical number list test case
print(Bubble_sort([1, 2, 3, 4, 5])) #Sorted list test case