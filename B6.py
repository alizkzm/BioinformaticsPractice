def lcs3(a, b, c):
    m = len(a)
    l = len(b)
    n = len(c)
    subs = [[[0 for k in range(n+1)] for j in range(l+1)] for i in range(m+1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            for k, z in enumerate(c):
                if x == y and y == z:
                    subs[i+1][j+1][k+1] = subs[i][j][k] + 1
                else:
                    subs[i+1][j+1][k+1] = max(subs[i+1][j+1][k],
                                              subs[i][j+1][k+1],
                                              subs[i+1][j][k+1])
    lcs1 = ""
    lcs2 = ""
    lcs3 = ""
    print(subs[-1][-1][-1])
    while (m+l+n)!=0:
        if m==0 and l==0 and n!=0:
            lcs1 += str("-")
            lcs2 += str("-")
            lcs3 += str(c[n - 1])
            n-=1
            continue
        if m==0 and l!=0 and n==0:
            lcs1 += str("-")
            lcs2 += str(b[l-1])
            lcs3 += str("-")
            l-=1
            continue
        if m!=0 and l==0 and n==0:
            lcs1 += str(a[m-1])
            lcs2 += str("-")
            lcs3 += str("-")
            m-=1
            continue
        if m==0 and l!=0 and n!=0:
            lcs1 += str("-")
            lcs2 += str(b[l - 1])
            lcs3 += str(c[n - 1])
            l-=1
            n-=1
            continue
        if m!=0 and l==0 and n!=0:
            lcs1 += str(a[m - 1])
            lcs2 += str("-")
            lcs3 += str(c[n - 1])
            m-=1
            n-=1
            continue
        if m!=0 and l!=0 and n==0:
            lcs1 += str(a[m - 1])
            lcs2 += str(b[l - 1])
            lcs3 += str("-")
            m-=1
            l-=1
            continue
        step = subs[m][l][n]
        if step-subs[m-1][l-1][n-1]==1 and a[m-1]==b[l-1] and a[m-1]==c[n-1]:
            lcs1 += str(a[m-1])
            lcs2 += str(b[l - 1])
            lcs3 += str(c[n - 1])
            m -= 1
            l -= 1
            n -= 1
        elif step-subs[m-1][l-1][n]==0 and a[m-1]==b[l-1] and a[m-1]!=c[n-1] :
            lcs1 += str(a[m - 1])
            lcs2 += str(b[l - 1])
            lcs3 += str("-")
            m -= 1
            l -= 1
        elif step-subs[m-1][l][n-1]==0 and a[m-1]!=b[l-1] and a[m-1]==c[n-1] :
            lcs1 += str(a[m - 1])
            lcs2 += str("-")
            lcs3 += str(c[n-1])
            m -= 1
            n -= 1
        elif step - subs[m][l-1][n - 1] == 0 and a[m - 1] != b[l - 1] and b[l - 1] == c[n - 1]:
            lcs1 += str("-")
            lcs2 += str(b[l-1])
            lcs3 += str(c[n - 1])
            l -= 1
            n -= 1
        elif step - subs[m-1][l][n] == 0 and a[m - 1] != b[l - 1] and a[m - 1] != c[n - 1]:
            lcs1 += str(a[m-1])
            lcs2 += str("-")
            lcs3 += str("-")
            m -= 1
        elif step - subs[m][l-1][n] == 0 and b[l - 1] != a[m - 1] and b[l - 1] != c[n - 1]:
            lcs1 += str("-")
            lcs2 += str(b[l-1])
            lcs3 += str("-")
            l -= 1
        elif step - subs[m][l][n-1] == 0 and c[n- 1] != a[m - 1] and c[n- 1] != b[l - 1]:
            lcs1 += str("-")
            lcs2 += str("-")
            lcs3 += str(c[n-1])
            n -= 1
    print(lcs1[::-1])
    print(lcs2[::-1])
    print(lcs3[::-1])
    return [lcs1[::-1],lcs2[::-1],lcs3[::-1]]

X = "ATAAGTAAGGTGGCTAGCACGCAGCGGTGGCTGGTTATTCATTTTTGCCCTCCCCCCCCCTTTTTTTTTTCGCAGCATATCGATAACAGGGTTATTCCGC"
Y = "CTAGCTGTTCGGGTTATTCATATGGTCGCGGTGGCTGGTTATTCTTTTTTTTTTTTTTTTTTTCGTATATCGCAGCATATCGATAACAGGGTTATTCCGC"
Z = "GAACGGGCCGCAGCATATCGATAACAGGGTTATTCCGCAGCATAACTGTAGTGGGCGGCGGTGGCTGGTTATTCTTTTTTTTTTT"
print(lcs3(X,Y,Z))
