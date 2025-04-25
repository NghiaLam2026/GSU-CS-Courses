#Nghia Lam
#CSC 2720 Lab 014
#Lab time: 2:00 PM
#Due time: 01/21/2024 @ 11:59PM

def binary_search(sorted_list, target):
    start = 0
    end = len(sorted_list) - 1
    checks = 0

    while start <= end:
        checks += 1
        mid = (start + end) // 2
        if sorted_list[mid] == target:
            print(f"The number {target} is found!")
            return (f"It took {checks} checks to find the integer!")
        elif sorted_list[mid] < target:
            start = mid + 1
        else:
            end = mid - 1


    return(f"Failed to find the number {target}!")

print(binary_search([11, 21, 33, 40, 50], 40),"\n") #Normal test case
print(binary_search([11, 21, 33, 40, 50], 15), "\n") #Target is not in the array test case
print(binary_search([], 15)) #Empty array test case