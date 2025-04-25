#Nghia Lam
#CSC 2720 Lab 014
#Lab time: 2:15 PM
#Due time: 04/07/2024 @ 11:59PM

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices  
        self.adj = {}  
        for i in range(vertices):
            self.adj[i] = []

    def add_edge(self, v, w):
        if v not in self.adj:
            self.adj[v] = []
        self.adj[v].append(w)

    def DFS(self):
        visited = set()  
        my_stack = []  
        
        if self.vertices > 0:
            my_stack.append(0)

        while my_stack:
            v = my_stack.pop() 
            if v not in visited:
                print(v, end=' ')
                visited.add(v)
            
            if v in self.adj:
                for neighbour in reversed(self.adj[v]):  
                    if neighbour not in visited:
                        my_stack.append(neighbour)

#GIVEN TEST CASE
g = Graph(6)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(2, 3)
g.add_edge(2, 4)
g.add_edge(4, 5)
g.add_edge(1, 3)
g.add_edge(3, 5)
print("\nDFS with an explicit stack:")
g.DFS()
print("\n")
#GIVEN TEST CASE

#LINEAR GRAPH TEST CASE
g1 = Graph(4)
g1.add_edge(0, 1)
g1.add_edge(1, 2)
g1.add_edge(2, 3)
print("\nDFS with linear graph: ")
g1.DFS()
print("\n")
#LINEAR GRAPH TEST CASE

#GRAPH FORMING A CYCLE TEST CASE
g2 = Graph(3)
g2.add_edge(0, 1)
g2.add_edge(1, 2)
g2.add_edge(2, 0)
print("\nDFS with cycle: ")
g2.DFS()
print("\n")
#GRAPH FORMING A CYCLE TEST CASE

#EMPTY GRAPH TEST CASE
g3 = Graph(0)
print("\nDFS with an empty graph: ")
g3.DFS()
print("\n")
#EMPTY GRAPH TEST CASE

