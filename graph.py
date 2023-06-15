import copy

class Vertex:
    def __init__(self, id):
        self.id = id
        self.edges = []

    def addEdge(self, vertex, edge):
        self.edges.append((vertex, edge))

    def __str__(self):
        return str(self.id)

class Edge:
    def __init__(self, vertex1, vertex2, weigth = 1):
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.weigth = weigth

    def __str__(self):
        return str(self.vertex1) + ' -> ' + str(self.vertex2) + ', w = ' + str(self.weigth)


class Graph:
    def __init__(self):
        self.vertexes = []
        self.edges = []

    def __str__(self):
        out = str(self.edges[0])
        for edge in self.edges[1:]:
            out = out + '\n' + str(edge)

        return out

    def getVertexById(self, id):
        for vertex in self.vertexes:
            if vertex.id == id:
                return vertex

        return None

    def getIndexById(self, id):
        for i in range(len(self.vertexes)):
            if self.vertexes[i].id == id:
                return i

        return None

    def addVertex(self, id):
        self.vertexes.append(Vertex(id))

    def addEdge(self, vertex1_id, vertex2_id, weigth = 1):
        vertex1 = self.getVertexById(vertex1_id)
        vertex2 = self.getVertexById(vertex2_id)

        if (vertex1 == None or vertex2 == None):
            print('Missing a vertex!')
            return
        
        self.edges.append(Edge(vertex1, vertex2, weigth))
        vertex1.addEdge(vertex2, self.edges[-1])

    def shortestPath(self, source, end):
        paths = []
        checked = []
        checkedNum = 0
        trace = []
        for vertex in self.vertexes:
            checked.append(False)
            trace.append([])
            if vertex.id == source:
                paths.append(0)
            else:
                paths.append(9999)
        
        vertexSrc = self.getVertexById(source)
        vertexEnd = self.getVertexById(end)
        
        minPath = 10000
        minVertex = None

        while checkedNum < len(checked):
            minPath = 10000
            for i, path in enumerate(paths):
                if path < minPath and checked[i] == False:
                    minPath = path
                    minVertex = self.vertexes[i]

            checked[self.getIndexById(minVertex.id)] = True
            checkedNum += 1

            for neigh, edge in self.vertexes[self.getIndexById(minVertex.id)].edges:
                if paths[self.getIndexById(minVertex.id)] + edge.weigth < paths[self.getIndexById(neigh.id)]:
                    paths[self.getIndexById(neigh.id)] = paths[self.getIndexById(minVertex.id)] + edge.weigth
                    trace[self.getIndexById(neigh.id)] = copy.deepcopy(trace[self.getIndexById(minVertex.id)])
                    trace[self.getIndexById(neigh.id)].append(minVertex)

        #print(paths)
        print('Min. path =', paths[self.getIndexById(end)])
        for vertex in trace[self.getIndexById(end)]:
            print(vertex.id, '-> ', end='')
        print(end)


        

