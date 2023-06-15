import math
import copy
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
        return self.distance

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
    def getShortestPath(self , v):
        x = v
        stringOutput =""
        names = []
        while x!=None:
           names.append(x.name)
           x = x.parent
        names.reverse()

        for i in range(len(names)):
            stringOutput+= names[i]
            if i != len(names)-1:
                stringOutput += " -> "
        return (stringOutput,v.distance) 

    def getMatrix(self):
        names = []
        output = []
        print("  ",end="")
        for v in self.vertices:
            names.append(v.name)
            print(v.name,end=" ")
        print()
        print("--------------------")
        for v in self.vertices:
            print(v.name , end="|")
            row = []
            self.Bellman_Ford(v)
            for i in self.vertices:
                if i.getDistance() == math.inf:
                    row.append(0)
                    print(0,end=" ")
                else:
                    row.append(self.getShortestPath(i))
                    print(1,end=" ")
            print()
            output.append(row)
        return output
    def printMatrix(self, l):
        weights = []
        start = 0
        stop = len(l)
        step = 1
        indexes = list(range(start, stop))
        for i in range(0,len(l)):
            for j in indexes:
                if l[i][j] != 0 and i!=j:
                    print(l[i][j][0] + "  ,w:" + str(l[i][j][1])) 
                    weights.append(l[i][j][1])
            indexes.reverse()
        return weights