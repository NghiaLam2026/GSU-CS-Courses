#Nghia Lam
#CSC 2720 Lab 014
#Lab time: 2:15 PM
#Due time: 02/04/2024 @ 11:59PM



#                           INSERTION SORT                         #
def insertion_sort(lst):
    for num in range(len(lst)): #n times | #1 space for n 
        key = lst[num] #1 step | #no space
        i = num - 1 #1 step | #no space
        while i >= 0 and lst[i] > key: #n - 1 times | 1 space for n
            lst[i + 1] = lst[i] #1 step | #no space
            i = i - 1 #1 step | #no space
        lst[i + 1] = key #1 step | #no space
    return lst #1 step | #no space

    #TIME COMPLEXITY: O(n^2) for average and worst-case
    #SPACE COMPLEXITY: O(1) 
#                           INSERTION SORT                         #




#                           SELECTION SORT                         #
def selection_sort(lst):
    n = len(lst) #1 step | #no space
    for i in range(n - 1): #n step | #1 space for n
        min_ind = i #1 step | #no space
        for j in range(i + 1, n): #n step | #1 space for n
            if lst[j] < lst[min_ind]: #2 step | #no space
                min_ind = j #1 step | #no space
        lst[i], lst[min_ind] = lst[min_ind], lst[i] #2 step | #no space
    return lst #1 step

    #TIME COMPLEXITY: O(n^2) for worst-case 
    #SPACE COMPLEXITY: O(1)
#                           SELECTION SORT                         #




