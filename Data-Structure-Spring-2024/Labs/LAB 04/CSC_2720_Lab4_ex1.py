#Nghia Lam
#CSC 2720 Lab 014
#Lab time: 2:15 PM
#Due time: 02/04/2024 @ 11:59PM

def insertion_sort(lst):
    for num in range(len(lst)):
        key = lst[num] 
        i = num - 1
        while i >= 0 and lst[i] > key:
            lst[i + 1] = lst[i]
            i = i - 1
        lst[i + 1] = key
    return lst

print(insertion_sort([50, 11, 33, 21, 40, 50, 40, 40, 21])) #Normal test case
print(insertion_sort([])) #Empty array test case
print(insertion_sort([1, 2, -5, -50, 10, 30])) #Negative number test case
print(insertion_sort([2, 2, 2, 2, 7, 10, 10, 23, 5])) #Duplicate number test case