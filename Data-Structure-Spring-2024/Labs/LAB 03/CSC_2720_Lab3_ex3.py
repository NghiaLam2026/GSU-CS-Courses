#Nghia Lam
#CSC 2720 Lab 014
#Lab time: 2:15 PM
#Due time: 01/28/2024 @ 11:59PM

#                                BUBBLE SORT ANALYSIS                            #

def Bubble_sort(my_list):

    if my_list == []: # 2 steps #No space
        return [] # 1 step #No space
    
    n = len(my_list) # 1 step #No space
    swapped = True # 1 step #No space

    while swapped: # n times #1 space
        swapped = False # 1 step #No space
        for i in range(1, n): # n times #1 space for i
            if my_list[i - 1] > my_list[i]: # 2 step #No space
                my_list[i - 1], my_list[i] = my_list[i], my_list[i - 1] # 4 step #No space
                swapped = True # 1 step #No space
 
        n -= 1 # 1 step #No space

    return my_list # 1 step

    #TIME COMPLEXITY = O(n^2) in both average and worst case
    #SPACE COMPLEXITY = O(1) as it only uses a constant amount of additional space
#                              BUBBLE SORT ANALYSIS                                #



#                             COUNTING SORT ANALYSIS                               #
def counting_sort(my_list):
    if not my_list: # 1 step #No space
        return [] # 1 step #No space
    
    max_num = my_list[0] # 1 step #No space
    for num in my_list: # n times #n space
        if num > max_num: # 2 steps #No space
            max_num = num # 1 step #No space

    min_num = my_list[0] # 1 step #No space
    for num in my_list: # n times #n space
        if num < min_num: # 2 steps #No space
            min_num = num # 1 step #No space
    
    negative_num = -min_num # 1 step #No space
    
    count_list = [0] * (max_num - min_num + 1) # O(K) #O(K)

    for num in my_list: # n times #n space
        count_list[num + negative_num] += 1 # 1 step #No space
    
    my_result = [] # 1 step #No space
    for num in range(len(count_list)): # n times #n times
        my_result.extend([num - negative_num] * count_list[num]) # 2 step #No space
    
    return my_result # 1 step #No space

    #TIME COMPLEXITY = O(n + K) in both average and worst case
    #SPACE COMPLEXITY = O(n + K)
#                               COUNTING SORT ANALYSIS#                            #



#                                    CONCLUSION                                    #
"""
In the case where our data sets are small, using bubble sort would be more suitable. It's time complexity is O(n^2) in both average and worst cases, which make it inefficient for 
large data set. On the other hand, counting sort is more efficient for larger datasets. Its time complexity is O(n + K), which can be significantly faster than O(n^2) 
when the range of input values (K) is not significant larger than the number of elements (n). However, its space complexity depends on the range of input values, as it requires additional
space to count arrays.
"""