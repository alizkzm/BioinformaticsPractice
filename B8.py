import Matrix as mt
lookup = mt.Matrix("BLOSUM62.txt")

def x(i, j):
    if i > 0 and j == 0:
        return 0
    else:
        if j > 0:
            return -11 + (-1 * j)
        else:
            return 0
def y(i, j):
    if j > 0 and i == 0:
        return 0
    else:
        if i > 0:
            return -11 + (-1 * i)
        else:
            return 0

def lengthMatrix(str1, str2):
    n = len(str2) + 1
    m = len(str1) + 1
    lower = [[x(j,i) for i in range(0, m)] for j in range(0, n)]
    upper = [[y(j,i) for i in range(0, m)] for j in range(0, n)]
    middle = [[0 for i in range(0, m)] for j in range(0, n)]

    for j in range(1, m):
        for i in range(1, n):
            lower[i][j] = max((-11 + middle[i][j - 1]), (-1 + lower[i][j - 1]))
            upper[i][j] = max((-11 + middle[i - 1][j]), (-1 + upper[i - 1][j]))
            middle[i][j] = max(int(lookup.lookup_score(str1[j - 1], str2[i - 1])) + middle[i - 1][j - 1], lower[i][j],
                               upper[i][j])
    print(lower)
    print(upper)
    print(middle)

    return [lower, upper, middle]


def convert(s):
    new = ""
    s = s[::-1]
    for x in s:
        new += x
    return new


def printPath(s, t):
    [lower, upper, middle] = lengthMatrix(s, t)
    string1 = ''
    string2 = ''
    score = max(lower[-1][-1], upper[-1][-1], middle[-1][-1])
    i = len(t)
    j = len(s)
    while (i > 0 or j > 0):
        if (i > 0 and j > 0 and middle[i][j] == middle[i - 1][j - 1] + int(lookup.lookup_score(s[j - 1], t[i - 1]))):
            string1 += s[j - 1]
            string2 += t[i - 1]
            i -= 1
            j -= 1
        elif (i > 0 and middle[i][j] == upper[i][j]):
            string1 += '-'
            string2 += t[i - 1]
            i -= 1
        elif (j > 0 and middle[i][j] == lower[i][j]):
            string1 += s[j - 1]
            string2 += '-'
            j -= 1
    print(score)
    print(convert(string1))
    print(convert(string2))
    return [score, string1, string2]

X = "FYACKRPNDLRLSDHILKMNGEHWDMGVVLYFLFMSPYNKQEHPETMCLPPWRAQRIVWLIQCSELGPVTIWYMQGTSGIICVKPDEMWL"
Y = "FYYCKRPNDLRLSCHILKGNGEHWDMGVVLYFLFMSPYNKQEGPEWLWTWMWNLQRQCSELGPVTIWYTKQGHSGIMCVKPAEMWL"
print(printPath(X, Y))