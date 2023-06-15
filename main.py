import graph

g = graph.Graph()

v1 = graph.Vertex(name="0")
v2 = graph.Vertex(name="1")
v3 = graph.Vertex(name="2")
v4 = graph.Vertex(name="3")
v5 = graph.Vertex(name="4")
v6 = graph.Vertex(name="5")

g.addVertex(v1)
g.addVertex(v2)
g.addVertex(v3)
g.addVertex(v4)
g.addVertex(v5)
g.addVertex(v6)

e0 = g.addEdge(v1, v3, 2)
e1 = g.addEdge(v1, v5, 5)
e2 = g.addEdge(v1, v6, 4)

e3 = g.addEdge(v2, v5, 4)
e4 = g.addEdge(v2, v6, 3)

e5 = g.addEdge(v3, v4, 11)
e6 = g.addEdge(v3, v5, 0)

e7 = g.addEdge(v5, v6, 1)


print(g)

v = g.getNode("0")
names = []
output = []
for v in g.vertices:
    names.append(v.name)
print (names)
for v in g.vertices:
    row = []
    


