import Matrix as mt
lookup = mt.Matrix("BLOSUM62.txt")

#initializers for matrices
def _init_x(i, j):
    if i > 0 and j == 0:
        return 0
    else:
        if j > 0:
            return -11 + (-1 * j)
        else:
            return 0

def _init_y(i, j):
    if j > 0 and i == 0:
        return 0
    else:
        if i > 0:
            return -11 + (-1 * i)
        else:
            return 0

def _init_m(i, j):
    if j == 0 and i == 0:
        return 0
    else:
        if j == 0 or i == 0:
            return 0
        else:
            return 0

def _format_tuple(inlist, i, j):
    return 0

def distance_matrix(s, t):
    dim_i = len(t) + 1
    dim_j = len(s) + 1
    #abuse list comprehensions to create matrices
    X = [[_init_x(i, j) for j in range(0, dim_j)] for i in range(0, dim_i)]
    Y = [[_init_y(i, j) for j in range(0, dim_j)] for i in range(0, dim_i)]
    M = [[_init_m(i, j) for j in range(0, dim_j)] for i in range(0, dim_i)]

    for j in range(1, dim_j):
        for i in range(1, dim_i):
            X[i][j] = max((-11+ M[i][j-1]), (-1+X[i][j-1]), (-11+ Y[i][j-1]))
            Y[i][j] = max((-11+ M[i-1][j]), (-11+X[i-1][j]), (-1+Y[i-1][j]))
            M[i][j] = max(int(lookup.lookup_score(s[j-1], t[i-1])) + M[i-1][j-1], X[i][j], Y[i][j])
    print(X)
    print(Y)
    print(M)

    return [X, Y, M]
def convert(s):
    # initialization of string to ""
    new = ""

    # traverse in the string
    for x in s:
        new += x

        # return string
    return new
def backtrace(s, t):
    [X, Y, M] = distance_matrix(s,t)
    sequ1 = ''
    sequ2 = ''
    score = max(X[-1][-1],Y[-1][-1],M[-1][-1])
    i = len(t)
    j = len(s)
    while (i>0 or j>0):
        if (i>0 and j>0 and M[i][j] == M[i-1][j-1] + int(lookup.lookup_score(s[j-1], t[i-1]))):
            sequ1 += s[j-1]
            sequ2 += t[i-1]
            i -= 1; j -= 1
        elif (i>0 and M[i][j] == Y[i][j]):
            sequ1 += '-'
            sequ2 += t[i-1]
            i -= 1
        elif (j>0 and M[i][j] == X[i][j]):
            sequ1 += s[j-1]
            sequ2 += '-'
            j -= 1
    sequ1r = ''.join([sequ1[j] for j in range(-1, -(len(sequ1)+1), -1)])
    sequ2r = ''.join([sequ2[j] for j in range(-1, -(len(sequ2)+1), -1)])
    print(convert(sequ1r))
    print(convert(sequ2r))
    return [score,sequ1r, sequ2r]

X = "YHFDVPDCWAHRYWVENPQAIAQMEQICFNWFPSMMMKQPHVFKVDHHMSCRWLPIRGKKCSSCCTRMRVRTVWE"
Y = "YHEDVAHEDAIAQMVNTFGFVWQICLNQFPSMMMKIYWIAVLSAHVADRKTWSKHMSCRWLPIISATCARMRVRTVWE"
print(backtrace(X,Y))