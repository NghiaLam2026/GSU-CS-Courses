#Nghia Lam
#CSC 2720 Lab 014
#Lab time: 2:15 PM
#Due time: 01/28/2024 @ 11:59PM

def counting_sort(my_list):
    if not my_list: #If the array is empty, just return an empty array
        return []
    
    max_num = my_list[0] #Manually search for the max value in the array.
    for num in my_list:
        if num > max_num:
            max_num = num

    min_num = my_list[0] #Manually search for the min value in the array.
    for num in my_list:
        if num < min_num:
            min_num = num
    
    negative_num = -min_num #Calculate the offset for negative numbers
    
    count_list = [0] * (max_num - min_num + 1) #This list will be used to count the frequency of each number in the array.

    for num in my_list: 
        count_list[num + negative_num] += 1 #Increment the count for this number in count_list
    
    my_result = [] #Initalize an empty list for the result
    for num in range(len(count_list)): 
        my_result.extend([num - negative_num] * count_list[num]) #Extend the result list with current number, repeated as many times as the frequency
    
    return my_result

print(counting_sort([50, 11, 33, 21, 40, 50, 40, 40, 21])) #Normal array test case
print(counting_sort([])) #Empty array test case
print(counting_sort([5])) #Single digit test case
print(counting_sort([-11, -12, -15, 50, 70, 100])) #Negative number and positive number test case