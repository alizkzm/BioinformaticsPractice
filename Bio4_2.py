import math
class Tree(object):
    def __init__(self,N=-1,bidirectional = True):
        self.nodes = list(range(N)) # {node : age}
        self.edges = {}
        self.bidirectional = bidirectional
        self.N = N
        self.weight = {}

    def half_unlink(self, a, b):
        links = [(e, w) for (e, w) in self.edges[a] if e != b]
        if len(links) < len(self.edges[a]):
            self.edges[a] = links
        else:
            print('Could not unlink {0} from {1}'.format(a, b))
            self.print()

    def get_nodes(self):
        for node in self.nodes:
            yield(node)


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

    def link(self,StartNode,StopNode,weight=1):
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


def UPGMA(D,n):


    def closest_clusters():
        ii = -1
        jj = -1
        best_distance = float('inf')
        for i in range(len(D)):
            for j in range(i):
                if i in Clusters and j in Clusters and D[i][j] < best_distance:
                    ii = i
                    jj = j
                    best_distance = D[i][j]
        return (ii, jj, best_distance)


    T = Tree(n)
    Clusters = {}
    Age = {}
    for i in range(n):
        Clusters[i] =[i]

    for node in T.get_nodes():
        Age[node] = 0

    while len(Clusters) > 1 :
        def d(i, j):
            return sum([D[cl_i][cl_j] for cl_i in Clusters[i] for cl_j in Clusters[j]]) / (
                        len(Clusters[i]) * len(Clusters[j])) \
                if i in Clusters and j in Clusters \
                else float('nan')
        finded_i,finded_j,dist_ij = closest_clusters()
        node=T.next_node()
        T.link(node,finded_i)
        T.link(node,finded_j)

        Clusters[node] = Clusters[finded_j]+Clusters[finded_i]
        Age[node] = D[finded_i][finded_j]/2

        del Clusters[finded_i]
        del Clusters[finded_j]

        row = [d(i,node) for i in range(len(D))] + [0.0]
        for k in range(len(D)):
            D[k].append(row[k])
        D.append(row)

    for node in T.nodes:
        T.edges[node] = [(e, abs(Age[node] - Age[e])) for e, W in T.edges[node]]
    return T


def main():
    n = 4
    D = """0   20  17  11
20  0   20  13
17  20  0   10
11  13  10  0
"""
    SplitedD = D.split("\n")
    NumericalD = [[0]*n for i in range(n)]
    for i in range(n):
        NumericalD[i] = list(map(int,SplitedD[i].split()))

    myTree = UPGMA(NumericalD,n)

    for node in myTree.nodes:
        if node in myTree.edges:
            for edge in myTree.edges[node]:
                end,weight=edge
                print ('{0}->{1}:{2:{prec}f}'.format(node,end,weight,prec='.3'))
main()