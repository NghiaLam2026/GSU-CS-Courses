#Nghia Lam
#CSC 2720 Lab 014
#Lab time: 2:15 PM
#Due time: 02/25/2024 @ 11:59PM

class Node: #Define the Node class to represent each element in a linked list
    def __init__(self, data):
        self.data = data #Store data in the node
        self.next = None #Initialize next as None
        
class LinkedList: #Define the LinkedList class to represent the linked list itself
    def __init__(self): 
        self.head = None #Initalize the head of the list as None

    def print_list(self): #Method to print all elements in the linked list
        elements = []
        temp = self.head #Start with the head of the list
        while (temp):
            elements.append(str(temp.data))
            temp = temp.next #Move to the next node
        print(", ".join(elements))

    def delete_nth(self, n): #Method to detel the Nth node from the end of the list
        temp = Node(0) #Create a dummy node to simplify edge cases
        temp.next = self.head #Point dummy node to the head of the list
        fast = slow = temp #Initalize both fast and slow pointers at dummy

        for i in range(n + 1): #Move the fast pointer n+1 steps ahead to create a gap
            fast = fast.next
        
        while fast: #Move both pointers until fast reaches the end of the list
            slow = slow.next #Slow moves one step
            fast = fast.next #Fast moves one step
        
        slow.next = slow.next.next #Delete the node after the slow pointer
        self.head = temp.next #Update the head in case the first node was deleted

llist = LinkedList() #Initialize the linked list
llist.head = Node(50) #Create node and link them together
node1 = Node(11)
node2 = Node(33)
node3 = Node(21)
node4 = Node(40)
node5 = Node(71)

llist.head.next = node1 #Link nodes together to from the list
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

llist.delete_nth(2)
llist.print_list()