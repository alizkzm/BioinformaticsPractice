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


def NeighbourJoining(D,n,Node_List=None):
    def my_remove(i, D):
        D_new = []
        for j in range(len(D)):
            if j != i:
                D_new.append([D[j][k] for k in range(len(D[j])) if k != i])
        return D_new


    def Find_ij(D):
        i = -1
        j = -1
        minD = float('inf')
        for ii in range(n):
            for jj in range(ii, n):
                if D[ii][jj] < minD:
                    i = ii
                    j = jj
                    minD = D[i][j]
        return (i, j, minD)


    if Node_List==None:
        Node_List = list(range(n))
    if n == 2:
        T = Tree(2)

        T.link(Node_List[0],Node_List[1],D[0][1])
        return T
    else:
        Total_distance = [sum(row) for row in D]

        D_star = [[0]*n for i in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                D_star[i][j] = (n - 2) * D[i][j] - Total_distance[i] - Total_distance[j]
                D_star[j][i] = D_star[i][j]

        finded_i,finded_j,min_distance = Find_ij(D_star)

        delta = [[0] * n for i in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                delta[i][j] = (Total_distance[i] - Total_distance[j]) / (n - 2)
                delta[j][i] = delta[i][j]

        LimbI = (D[finded_i][finded_j] + delta[finded_i][finded_j])/2
        LimbJ = (D[finded_i][finded_j] - delta[finded_i][finded_j])/2

        D.append([])
        for k in range(n):
            D[-1].append((D[k][finded_i]+D[k][finded_j]-D[finded_i][finded_j])/2)
            D[k].append((D[k][finded_i] + D[k][finded_j] - D[finded_i][finded_j]) / 2)
        D[-1].append(0)

        m = Node_List[-1]+1
        Node_List.append(m)
        D = my_remove(max(finded_i, finded_j), D)
        D = my_remove(min(finded_i, finded_j), D)
        node_i = Node_List[finded_i]
        node_j = Node_List[finded_j]
        Node_List.remove(node_i)
        Node_List.remove(node_j)
        T = NeighbourJoining(D,n-1,Node_List)
        T.link(node_i,m,LimbI)
        T.link(node_j,m,LimbJ)
        return T




def main():
    n = 4
    D = """0   23  27  20
            23  0   30  28
            27  30  0   30
            20  28  30  0
        """
    SplitedD = D.split("\n")
    NumericalD = [[0]*n for i in range(n)]
    for i in range(n):
        NumericalD[i] = list(map(int,SplitedD[i].split()))

    myTree = NeighbourJoining(NumericalD,n)

    for node in myTree.nodes:
        if node in myTree.edges:
            for edge in myTree.edges[node]:
                end,weight=edge
                print('{0}->{1}:{2:{prec}f}'.format(node, end, weight, prec='.3'))
main()