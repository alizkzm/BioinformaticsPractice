def compareMismatch(word1,word2,d):
    error = 0
    list = word2.split(" ")
    for ind, letter in enumerate(word1):
        #print(letter,word2[ind])
        if letter!=word2[ind]:
            error +=1
    if (error<d+1):
        #if (error!=0):
            #print('yes')
        return 1
    #print('no')
    return 0

#input
seq = "CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAATGCCTAGCGGCTTGTGGTTTCTCCTACGCTCC"
pattern = "ATTCTGGA"
k = len(pattern)
n = len(seq)
d = 3

for j in range(n-k+1):
    if(compareMismatch(pattern,seq[j:j+k],d)==1):
        print(j)

