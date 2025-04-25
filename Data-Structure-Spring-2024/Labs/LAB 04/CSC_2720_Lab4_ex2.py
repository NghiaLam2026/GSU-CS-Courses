#Nghia Lam
#CSC 2720 Lab 014
#Lab time: 2:15 PM
#Due time: 02/04/2024 @ 11:59PM

def selection_sort(lst):
    n = len(lst)
    for i in range(n - 1):
        min_ind = i
        for j in range(i + 1, n):
            if lst[j] < lst[min_ind]:
                min_ind = j
        lst[i], lst[min_ind] = lst[min_ind], lst[i]
    return lst

print(selection_sort([50, 11, 33, 21, 40, 50, 40, 40, 21])) #Normal test case 
print(selection_sort([])) #Empty test case
print(selection_sort([-1, -5, -50, 5, 6, -100, 200])) #Negative number test case
print(selection_sort([2, 2, 2, 2, 7, 10, 10, 23, 5])) #Duplicate number test case