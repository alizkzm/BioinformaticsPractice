import numpy as np

def lengthOfLcs(str1,str2,str3):
    m = len(str1)
    n = len(str2)
    o = len(str3)
    L = [[[0 for i in range(o + 1)] for j in range(n + 1)]
         for k in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            for k in range(o + 1):
                if (i == 0 or j == 0 or k == 0):
                    L[i][j][k] = 0

                elif (X[i - 1] == Y[j - 1] and
                      X[i - 1] == Z[k - 1]):
                    L[i][j][k] = L[i - 1][j - 1][k - 1] + 1

                else:
                    L[i][j][k] = max(max(L[i - 1][j][k],
                                         L[i][j - 1][k]),
                                     L[i][j][k - 1])
    return L


def convert(s):
    # initialization of string to ""
    s = s[::-1]
    new = ""

    # traverse in the string
    for x in s:
        new += x

        # return string
    return new

def printLcs(str1,str2,str3):
    string1 = [""]
    string2 = [""]
    string3 = [""]

    matrix = lengthOfLcs(str1,str2,str3)
    matrix = np.array(matrix)
    m = matrix.shape[0]
    n = matrix.shape[1]
    o = matrix.shape[2]
    i = m-1
    j = n-1
    k = o-1
    print(len(str1))
    while(i+j+k!=0):
        a111 = matrix[i][j][k]-matrix[i-1][j-1][k-1]
        a110 = matrix[i][j][k]-matrix[i-1][j-1][k]
        a100 = matrix[i][j][k]-matrix[i-1][j][k]
        a011 = matrix[i][j][k]-matrix[i][j-1][k-1]
        a001 = matrix[i][j][k]-matrix[i][j][k-1]
        a010 = matrix[i][j][k]-matrix[i][j-1][k]
        a101 = matrix[i][j][k]-matrix[i-1][j][k-1]
        if a111 and str1[i-1]==str2[j-1] and str1[i-1]==str3[k-1]:
            string1.append(str1[i-1])
            string2.append(str2[j-1])
            string3.append(str3[k-1])
            i-=1
            j-=1
            k-=1
            continue
        if a110==1 and str1[i-1]==str2[j-1] and str1[i-1]!=str3[k-1]:
            string1.append(str1[i-1])
            string2.append(str2[j-1])
            string3.append("-")
            i-=1
            j-=1
            continue
        if a101==0 and str1[i-1]!=str2[j-1] and str1[i-1]==str3[k-1]:
            string1.append(str1[i-1])
            string2.append("-")
            string3.append(str3[k-1])
            i-=1
            k-=1
            continue
        if a100==0 and str2[j-1]!=str3[k-1]:
            string1.append(str1[i-1])
            string2.append("-")
            string3.append("-")
            i-=1
            continue
        if a011==0 and str1[i-1]!=str2[j-1] and str2[j-1]==str3[k-1]:
            string1.append("-")
            string2.append(str2[j-1])
            string3.append(str3[k-1])
            j-=1
            k-=1
            continue
        if a010==0 and str1[i-1]!=str3[k-1]:
            string1.append("-")
            string2.append(str2[j-1])
            string3.append("-")
            j-=1
            print("1")
            continue
        if a001==0 and str1[i-1]!=str2[j-1]:
            string1.append("-")
            string2.append("-")
            string3.append(str3[k-1])
            k -= 1
            continue
    print(convert(string1))
    print(convert(string2))
    print(convert(string3))
    return 0
X = "ATATCCG"
Y = "TCCGA"
Z = "ATGTACTG"
print(printLcs(X, Y,Z))
