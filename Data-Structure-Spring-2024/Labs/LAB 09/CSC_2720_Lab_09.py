#Nghia Lam
#CSC 2720 Lab 014
#Lab time: 2:15 PM
#Due time: 03/10/2024 @ 11:59PM

class MinStack:
    def __init__(self): #Initialize the MinStack with two lists.
        self.stack = [] #Storing all elements.
        self.min_stack = [] #Keeping track of minimum.

    def push(self, val): #Pushses an element into the stack. 
        self.stack.append(val) 
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self): #Pops the top element from the stack and reuturns it.
        if not self.stack:
            print("Stack is empty. No element to pop!")
            return None
        val = self.stack.pop() 
        if val == self.min_stack[-1]: #If the popped element is equal to the top of the min_stack, it's also removed from the min_stack.
            self.min_stack.pop()
        return val
    
    def top(self):
        return self.stack[-1] if self.stack else None #Return the top element of the stack without removing it. If the stack is empty, returns None.

    def getMin(self):
        return self.min_stack[-1] if self.min_stack else None #Return the current minimum element in the stack by retrieving the top element of the min_stack. If min_stack is empty, returns None.

#NORMAL TEST CASE
my_stack = MinStack()
my_stack.push(5)
my_stack.push(6)
my_stack.push(7)
my_stack.push(8)
my_stack.push(9)

pop_element = my_stack.pop() #Popping out the last element that was push into the stack.
print(f"The element that got popped was: {pop_element}")

top_element = my_stack.top() #Getting the top element
print(f"The top element is: {top_element}")

min_element = my_stack.getMin() #Getting the smallest element
print(f"The minimum element is: {min_element}\n")
#NORMAL TEST CASE


#SAME ELEMENT TEST CASE
my_stack = MinStack()
my_stack.push(7)
my_stack.push(7)
my_stack.push(7)
my_stack.push(7)
my_stack.push(7)

pop_element = my_stack.pop()
print(f"The element that got popped was: {pop_element}")

top_element = my_stack.top()
print(f"The top element is: {top_element}")

min_element = my_stack.getMin()
print(f"The minimum element is: {min_element}\n")
#SAME ELEMENT TEST CASE


#MIXED INCREASING AND DECREASING ELEMENTS TEST CASE
my_stack = MinStack()
my_stack.push(3)
my_stack.push(10)
my_stack.push(2)
my_stack.push(8)
my_stack.push(1)
my_stack.push(5)

pop_element = my_stack.pop() 
print(f"The element that got popped was: {pop_element}")

top_element = my_stack.top() 
print(f"The top element is: {top_element}")

min_element = my_stack.getMin() 
print(f"The minimum element is: {min_element}\n")
#MIXED INCREASING AND DECREASING ELEMENTS TEST CASE


#EMPTY STACK TEST CASE
my_stack = MinStack()

pop_element = my_stack.pop() 
print(f"Attempt to pop from an empty stack resulted in: {pop_element}") 

top_element = my_stack.top() 
print(f"Top element of an empty stack is: {top_element}") 

min_element = my_stack.getMin()
print(f"Minimum element of an empty stack is: {min_element}") 
#EMPTY STACK TEST CASE