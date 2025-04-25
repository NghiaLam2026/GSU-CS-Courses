#Nghia Lam
#CSC 2720 Lab 014
#Lab time: 2:15 PM
#Due time: 04/14/2024 @ 11:59PM

import heapq as hq

def kBiggest(lst, k):
    min_heap = []

    if not lst or k > len(lst):
        return None
    
    for num in lst: #Iterate through each number in the list.
        if len(min_heap) < k: #If the heap has fewer than k elements, push the current number onto the heap.
            hq.heappush(min_heap, num)
        elif num > min_heap[0]: #Else, if the current number is greater than the smallest number in the heap, replace the smallest with the current number
            hq.heapreplace(min_heap, num)
    
    #After processing all numbers, the smallest number in the heap is the k-th biggest number in the list.
    return min_heap[0]

"""
Time Complexity: O(nlogk), where n is the number of elements in the list. Each of the n insertions into a heap of size k cost O(logk), which lead to O(nlogk)
Space Complexity: O(k), where k is for storing the size of heap
"""
#Normal test case
print(kBiggest([3, 2, 1, 5, 6, 4], 4), "\n")
#Normal test case

#Empty list test case
print(kBiggest([], 4), "\n")
#Empty list test case

#Duplicate elements test case
print(kBiggest([5, 5, 5, 5, 5, 5], 2), "\n")
#Duplicate elements test case

#Test case with k being more than the size of the list
print(kBiggest([1, 2, 3], 4))
#Test case with k being more than the size of the list