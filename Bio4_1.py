class Tree(object):
    def __init__(self,N=-1,bidirectional = True):
        self.nodes = list(range(N))
        self.edges = {}
        self.bidirectional = bidirectional
        self.N = N

    def half_unlink(self, a, b):
        links = [(e, w) for (e, w) in self.edges[a] if e != b]
        if len(links) < len(self.edges[a]):
            self.edges[a] = links
        else:
            print('Could not unlink {0} from {1}'.format(a, b))
            self.print()

    def unlink(self, i, k):
        try:
            self.half_unlink(i, k)
            if self.bidirectional:
                self.half_unlink(k, i)
        except KeyError:
            print('Could not unlink {0} from {1}'.format(i, k))
            self.print()

    def half_link(self,a,b,weight=1):
        if a not in self.nodes:
            self.nodes.append(a)
        if a in self.edges:
            self.edges[a] = [(b0,w0) for (b0,w0) in self.edges[a] if b0!=b] + [(b,weight)]
        else:
            self.edges[a] = [(b,weight)]

    def link(self,StartNode,StopNode,weight):
        self.half_link(StartNode,StopNode,weight)
        if self.bidirectional:
            self.half_link(StopNode,StartNode,weight)

    def next_node(self):
        return len(self.nodes)

    def traverse(self, i, k, path=[], weights=[]):
        if not i in self.edges: return (False, [])
        if len(path) == 0:
            path = [i]
            weights = [0]

        for j, w in self.edges[i]:
            if j in path: continue
            path1 = path + [j]
            weights1 = weights + [w]
            if j == k:
                return (True, list(zip(path1, weights1)))
            else:
                found_k, test = self.traverse(j, k, path1, weights1)
                if found_k:
                    return (found_k, test)
        return (False, [])


def AdditivePhelogeny(D,n , N=-1):

    def LimbLength(n, j, D):
        return int(
            min([D[i][j] + D[j][k] - D[i][k] for i in range(n) for k in range(n) if j != k and k != i and i != j]) / 2)

    def find_ikn(Dinput):
        for i in range(n):
            for k in range(n):
                if Dinput[i][k] == Dinput[i][n - 1] + Dinput[n - 1][k] and i != k:
                    return (i, k, n - 1, Dinput[i][n - 1])

    def node_position(traversal):
        d = 0
        for l, w in traversal:
            d0 = d
            d += w
            if d == x: return (True, l, l, d0, d)
            if d > x: return (False, l_previous, l, d0, d)
            l_previous = l
        return (False, l_previous, l, d0, d)

    if N==-1:
        N = n
    if n == 2:
        T = Tree(N)
        T.link(0,1,D[0][1])
        return T
    else:
        limbLen = LimbLength(n,n-1,D)
        D_bald = [d_row[:] for d_row in D]
        for j in range(n-1):
            D_bald[j][n-1] = D_bald[j][n-1]-limbLen
            D_bald[n-1][j] = D_bald[j][n-1]

        Finded_i, Finded_k, node, x = find_ikn(D_bald)
        D_trimmed = list()
        for i in range(n-1):
            D_trimmed.append(D_bald[i][:-1])

        T = AdditivePhelogeny(D_trimmed,n-1,N)
        found_k, traversal = T.traverse(Finded_i,Finded_k)
        path, weights = zip(*traversal)
        found, l0, l1, d, d0 = node_position(traversal)

        if found:
            v = l0
            T.link(node, v, limbLen)
        else:
            v = T.next_node()
            weight_i = LimbLength(n,Finded_i,D)
            weight_k = LimbLength(n,Finded_k,D)
            T.unlink(l0, l1)
            T.link(v, l0, x - d)
            T.link(v, l1, d0 - x)

        T.link(node, v, limbLen)
        return T

def main():
    n = 4
    D = """0   19  17  15
           19  0   20  18
           17  20  0   16
           15  18  6  0"""
    SplitedD = D.split("\n")
    NumericalD = [[0]*n for i in range(n)]
    for i in range(n):
        NumericalD[i] = list(map(int,SplitedD[i].split()))

    myTree = AdditivePhelogeny(NumericalD,n)

    for node in myTree.nodes:
        if node in myTree.edges:
            for edge in myTree.edges[node]:
                end,weight=edge
                print ('{0}->{1}:{2}'.format(node,end,weight))

main()