import math
class Vertex:
    def __init__(self, name = None, parent = None, distance = None):
        self.name = name
        self.parent = parent
        self.distance = distance

    def __str__(self):
        return str(self.name)

    def __repr__(self):
        return str(self.name)
    def getDistance(self):
        return (self.name,self.distance)

class Edge:
    def __init__(self, src = None, dst = None, weight = None):
        self.src = src
        self.dst = dst
        self.weight = weight
    def __str__(self) -> str:
        return f"src:{self.src} -> dst:{self.dst} , w:{self.weight}"

class Graph:
    def __init__(self):
        self.vertices = []
        self.edges = []

    def getNode(self, name):
        for v in self.vertices:
            if v.name == name:
                return v

    def GetInDegrees(self):
        list = []

        for v in self.vertices:
            counter = 0

            for e in self.edges:
                if e.dst == v:
                    counter += 1

            list.append(counter)

        return list

    def GetOutDegrees(self):
        list = []

        for v in self.vertices:
            counter = 0

            for e in self.edges:
                if e.src == v:
                    counter += 1

            list.append(counter)

        return list

    def initialiseSingleSource(self, s):
        for v in self.vertices:
            v.distance = math.inf
            v.parent = None

        s.distance = 0

    def relax(self, u, v, w):
        if v.distance > u.distance + w:
            v.distance = u.distance + w
            v.parent = u

    def extractMin(self, Q):
        min = Q[0]

        for v in Q:
            if v.distance < min.distance:
                min = v

        Q.remove(min)

        return min

    def getAdj(self, x):
        list = []

        for e in self.edges:
            if e.src == x:
                list.append(e.dst)

        return list

    def getWeight(self, u, v):
        for e in self.edges:
            if e.src == u and e.dst == v:
                return e.weight

    def Dijkstra(self, a):
        self.initialiseSingleSource(a)
        S = []
        Q = self.vertices[:]

        while len(Q) > 0:
            u = self.extractMin(Q)
            S.append(u)
            for v in self.getAdj(u):
                self.relax(u, v, self.getWeight(u, v))

    def printShortestPath(self, a, b, list):
        if a == b:
            list.append(a)
        elif b.parent is not None:
            self.printShortestPath(a, b.parent, list)
            list.append(b)
        else:
            print("There is no such a path")
            list.clear()
            return

    def Bellman_Ford(self, a):
        self.initialiseSingleSource(a)
        for v in self.vertices:
            for e in self.edges:
                self.relax(e.src, e.dst, e.weight)

        for e in self.edges:
            if e.dst.distance > e.src.distance + e.weight:
                return False

        return True

    def UpdateEdge(self, a, b, w):
        for e in self.edges:
            if e.src == a and e.dst == b:
                e.weight = w
                return

        e = Edge(src = a, dst = b, weight = w)
        self.edges.append(e)
    def addVertex(self, v):
        self.vertices.append(v)
    def addEdge(self, v1 ,v2 , w):
        self.edges.append(Edge(v1,v2,w))
    def __str__(self) -> str:
        output=""
        for e in self.edges:
            output += f"{e}\n"
        return output