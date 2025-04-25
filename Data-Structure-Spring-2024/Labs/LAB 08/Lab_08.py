#Nghia Lam
#CSC 2720 Lab 014
#Lab time: 2:15 PM
#Due time: 03/03/2024 @ 11:59PM
from collections import deque

class MaxQueue:
    def __init__(self):
        self.main_queue = deque() #Main queue to store all the elements
        self.max_queue = deque() #Max queue to keep elements in decreasing order for max lookup

    def enqueue(self, element): 
        self.main_queue.append(element) #Add the new element to the end of the main queue
        
        while self.max_queue and self.max_queue[-1] < element: #Remove elements from the max queue that are smaller than the new element
            self.max_queue.pop()
        self.max_queue.append(element) #Add the new element to the max queue

    def dequeue(self):
        element = self.main_queue.popleft() #Remove the front element form the main queue
        if element == self.max_queue[0]: #If the removed element is also at the front of the max queue, remove it
            self.max_queue.popleft()
        return element

    def get_max(self):
        return self.max_queue[0] if self.max_queue else None #Return the front elemnet of the max queue, which is the current maximum


#Test Case 1: Basic 
max_queue = MaxQueue()
max_queue.enqueue(1); assert max_queue.get_max() == 1, "Test Case 1a Failed"
max_queue.enqueue(2); assert max_queue.get_max() == 2, "Test Case 1b Failed"
max_queue.enqueue(3); assert max_queue.get_max() == 3, "Test Case 1c Failed"
print("Test Case 1: Passed")

# Test Case 2: Decreasing Order Insertions
max_queue = MaxQueue()
max_queue.enqueue(3); max_queue.enqueue(2); max_queue.enqueue(1)
assert max_queue.get_max() == 3, "Test Case 2 Failed"
print("Test Case 2: Passed")

# Test Case 3: Mixed Order Insertions
max_queue = MaxQueue()
max_queue.enqueue(2); max_queue.enqueue(3); max_queue.enqueue(1)
assert max_queue.get_max() == 3, "Test Case 3 Failed"
print("Test Case 3: Passed")

# Test Case 4: Dequeue Operations Affecting Max
max_queue = MaxQueue()
max_queue.enqueue(5); max_queue.enqueue(1); max_queue.enqueue(3)
max_queue.dequeue()  # Removes 5
assert max_queue.get_max() == 3, "Test Case 4 Failed"
print("Test Case 4: Passed")