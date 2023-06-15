import graph

g = Graph()

g.addVertex('A')
g.addVertex('B')
g.addVertex('C')
g.addVertex('D')
g.addVertex('E')
g.addVertex('F')

g.addEdge('A', 'B', 5)
g.addEdge('A', 'E', 23)
g.addEdge('B', 'C', 3)
g.addEdge('B', 'E', 7)
g.addEdge('C', 'D', 6)
g.addEdge('C', 'F', 13)
g.addEdge('D', 'E', 11)
g.addEdge('E', 'F', 2)

print(g)
print()

g.shortestPath('A', 'F')