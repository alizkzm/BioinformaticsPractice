import numpy as np
import Matrix as mt

def _init_x(i,j):
    if j > 0 and i == 0:
        return 0
    else:
        if i > 0:
            return -11 + (-1 * i)
        else:
            return 0

def _init_y(i,j):
    if i > 0 and j == 0:
        return 0
    else:
        if j > 0:
            return -11 + (-1 * j)
        else:
            return 0

def lengthOfLcs(str1, str2):
    lookup = mt.Matrix("BLOSUM62.txt")
    m = len(str1)
    n = len(str2)
    '''
    matrix1 = [[0] * (n + 1) for i in range(m + 1)]
    matrix1[0][0] = 0
    matrix1[1][0] = 0
    for i in range(m):
        matrix1[i+1][0] = -11-1*i
    for i in range(n+1):
        matrix1[0][i] = 0

    matrix2 = [[0] * (n + 1) for i in range(m + 1)]
    matrix2[0][0] = 0

    matrix3= [[0] * (n + 1) for i in range(m + 1)]
    matrix3[0][0] = 0
    matrix3[0][1] = 0
    for i in range(m+1):
        matrix3[i][0] -= 0
    for i in range(n):
        matrix3[0][i+1] = -11-1*i
    '''
    dim_i = len(str1) + 1
    m = dim_i
    dim_j = len(str2) + 1
    n = dim_j
    # abuse list comprehensions to create matrices
    matrix1 = [[-_init_x(i,j) for i in range(0, dim_i)] for j in range(0, dim_j)]
    matrix3 = [[-_init_y(i,j) for i in range(0, dim_i)] for j in range(0, dim_j)]
    matrix2 = [[0 for i in range(0, dim_i)] for j in range(0, dim_j)]
    print(matrix1)
    print(matrix2)
    print(matrix3)

    for i in range(m):
        for j in range(n):
            if i!=0 and j!=0:
                print(i,j)
                matrix1[i][j] = max(matrix1[i-1][j]-1,
                                       matrix2[i-1][j]-11)
                matrix2[i][j] = max(matrix1[i][j],
                                    matrix2[i-1][j-1]+ int(lookup.lookup_score(str1[i - 1], str2[j - 1])),
                                    matrix3[i][j])
                matrix3[i][j] = max(matrix3[i][j-1] - 1,
                                    matrix2[i][j-1] - 11)
    score = max([matrix1[i][j],matrix2[i][j],matrix3[i][j]])
    print(score)
    return matrix1,matrix2,matrix3

def convert(s):
    # initialization of string to ""
    s = s[::-1]
    new = ""

    # traverse in the string
    for x in s:
        new += x

        # return string
    return new

def printLcs(str1,str2):
    lookup = mt.Matrix("BLOSUM62.txt")
    string1 = [""]
    string2 = [""]
    matrix = lengthOfLcs(str1,str2)
    matrix = np.array(matrix)
    m = matrix.shape[0]
    n = matrix.shape[1]
    i = m-1
    j = n-1
    score = matrix[i][j]
    while(i+j!=0):
        #print(int(lookup.lookup_score(str1[i-1],str2[j-1])),[str1[i-1],str2[j-1]])
        a = matrix[i][j]-matrix[i][j-1]
        b = matrix[i][j]-matrix[i-1][j]
        c = matrix[i][j]-matrix[i-1][j-1]
        d = int(lookup.lookup_score(str1[i-1],str2[j-1]))
        e = -5
        if (d==c):
            string1.append(str1[i - 1])
            string2.append(str2[j - 1])
            i -= 1
            j -= 1
            continue
        if (b==e):
            string1.append(str1[i - 1])
            string2.append("-")
            i -= 1
            continue
        if (a==e):
            string2.append(str2[j - 1])
            string1.append("-")
            j -= 1
            continue
    print(convert(string1))
    print(convert(string2))

    return [score,convert(string1),convert(string2)]

X = "PRTEINS"
Y = "PRTWPSEIN"
matrix1,matrix2,matrix3 = lengthOfLcs(X, Y)
print(matrix1)
print(matrix2)
print(matrix3)

a = mt.Matrix("BLOSUM62.txt").lookup_score("N","N")
print(a)
