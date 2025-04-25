#Nghia Lam
#CSC 2720 Lab 014
#Lab time: 2:00 PM
#Due time: 01/21/2024 @ 11:59PM

def De_duplication(arr):
    if not arr: #If the array is empty, just return an empty array
        return []
    
    max_num = arr[0] #Manually search for the max value in the array.
    for num in arr:
        if num > max_num:
            max_num = num
    
    count_list = [0] * (max_num + 1) #This list will be used to count the frequency of each number in the array.

    for num in arr: 
        count_list[num] += 1 #Increment the count for this number in count_list
    
    my_result = [] #Initalize an empty list for the result
    for num in range(len(count_list)): 
            my_result.extend([num] * count_list[num])
    
    return my_result

print(De_duplication([50, 11, 33, 21, 40, 50, 40, 40, 21])) #Basic test case
print(De_duplication([])) #Empty array test case
print(De_duplication([5, 10, 15, 20])) #All unique element test case
print(De_duplication([5, 5, 5, 5, 5])) #All identical number test case


def De_duplication(arr):
    new_arr = set()
    for num in arr:
        if num not in new_arr:
            new_arr.add(num)
    return new_arr