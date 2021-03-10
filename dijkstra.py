import math

# paste your MinHeap class here and modify it as needed
# for use by your dijkstra function
class Vertex:
    def __init__(self, label):
        self.label = label
        self.dist = math.inf
        self.prev = None

    def getPrev(self):
        return self.prev
    
    def setPrev(self, val):
        self.prev = val

    def getLabel(self):
        return self.label
    
    def getDist(self):
        return self.dist
    
    def setDist(self, value):
        self.dist = value

    def __lt__(self,other):
        if other != None:
            return self.dist < other.dist
    
    def __gt__(self,other):
        if other != None:
            return self.dist > other.dist
    
    def __eq__(self,other):
        if other != None:
            return self.dist == other.dist
    
    def __ge__(self,other):
        if other != None:
            return self.dist >= other.dist
    
    def __le__(self,other):
        return self.dist <= other.dist    

class MinHeap:
    def __init__(self, length):
        self.heap = [None for i in range(length)]
        self.length = length
        self.pos = {}
        self.n = 0

    def insert(self, value):
        if self.n >= self.length:
            return

        self.n += 1
        h = self.heap

        i = self.n - 1  # first empty slot
        h[i] = value
        self.pos[h[i].getLabel()] = i
        #print("Table here : " + str(self.pos))
        self.upHeap(i)

        # first_elm _ _ _
        # first_elm second_elm ...

    def upHeap(self, i):
        h = self.heap

        p = (i - 1) // 2
        while p >= 0 and h[p].__gt__(h[i]):
            h[i], h[p] = h[p], h[i]
            if h[i]:
                self.pos[h[i].getLabel()] = i
            if h[p]:
                self.pos[h[p].getLabel()] = p
            i = p
            p = (i - 1) // 2

    def extract_min(self):
        if self.n == 0:
            return None

        self.n -= 1

        h = self.heap

        # swap and delete old root, saving its value
        value = h[0]
        h[0] = h[self.n]
        h[self.n] = None
        del self.pos[value.getLabel()]
        self.downheap(0)

        return value

    def downheap(self, i):
        h = self.heap

        l = 2 * i + 1
        r = 2 * i + 2

        # if no left child, then no children
        no_children = l >= self.n
        no_right_child = r >= self.n

        if no_children or ( h[i].__le__(h[l]) and (no_right_child or h[i].__le__(h[r]) )):
            return

        min_child = l if no_right_child or h[l] <= h[r] else r
        h[i], h[min_child] = h[min_child], h[i]
        if h[i]:
            self.pos[h[i].getLabel()] = i
        if h[min_child]:
            self.pos[h[min_child].getLabel()] = min_child

        self.downheap(min_child)

    def isEmpty(self):
        if any(self.heap):
            return False
        return True
        
    def update(self, val):    
        self.upHeap(self.pos[val.getLabel()])

    def get_heap_array(self):
        return self.heap

def dijkstra(graph, edge_weights, source):
    vertexDict = {}
    vHeap = MinHeap(len(graph))

    for V in graph:
        vertexDict[V] = Vertex(V)
        if V == source:
            vertexDict[source].setDist(0)
        vHeap.insert(vertexDict[V])

    while not ( vHeap.isEmpty() ):
        curMin = vHeap.extract_min()
        curLabel = curMin.getLabel()
        curDist = curMin.getDist()
        neighbours = graph[curLabel]
        for N in neighbours:
#Rework this part. 
# so current_node to next_node distance is updated 
# insert this new value into the heap. Delete/Update the previous value in heap
            tempDistance = curDist + edge_weights[ (curLabel, N) ]
            adjVertex = vertexDict[N]
            if tempDistance < adjVertex.getDist():
                adjVertex.setDist(tempDistance)
                adjVertex.setPrev(curLabel)
                vHeap.update(adjVertex)
    for i in vertexDict:
        vertexDict[i] = vertexDict[i].getDist()
    return vertexDict



if __name__ == '__main__':
        # graph
    graph = {
        'a': ['b', 'c'], 
        'b': ['a', 'c', 'e'], 
        'c': ['b', 'd', 'e'], 
        'd': ['a'],
        'e': [],
        'f': [],
        'g': ['e'],
    }

    # edge weights
    edge_weights = {
        #(prev, next)
        ('a', 'b'): 2,
        ('a', 'c'): 7,
        ('b', 'a'): 4,
        ('b', 'c'): 3,
        ('b', 'e'): 10,
        ('c', 'b'): 6,
        ('c', 'd'): 4,
        ('c', 'e'): 1,
        ('d', 'a'): 3,
        ('g', 'e'): 2
    }
    distances = dijkstra(graph, edge_weights, 'a')
    print(distances) 
    # {'a': 0, 'b': 2, 'c': 5, 'd': 9, 'e': 6, 'f': inf, 'g': inf}

    distances = dijkstra(graph, edge_weights, 'c')
    print(distances)
    # {'a': 7, 'b': 6, 'c': 0, 'd': 4, 'e': 1, 'f': inf, 'g': inf}

    distances = dijkstra(graph, edge_weights, 'g')
    print(distances)
    # {'a': inf, 'b': inf, 'c': inf, 'd': inf, 'e': 2, 'f': inf, 'g': 0}

    graph = {'a': ['b', 'c'], 'b': ['c'], 'c': []}
    edges = {('a', 'b'): 1, ('a', 'c'): 4, ('b', 'c'): 2}
    source = 'a'
    print ( dijkstra(graph, edges, source) )