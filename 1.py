from collections import defaultdict
def patternList(k):
    list =  [''] * (pow(4,k))
    for i in range(k):
        for j in range(pow(4,k)):
            if ((j // (pow(4,i))) % 4)==1:
                word='A'
            elif ((j // (pow(4,i))) % 4)==2:
                word='G'
            elif ((j // (pow(4,i))) % 4)==3:
                word='C'
            elif ((j // (pow(4,i))) % 4)==0:
                word='T'
            list[j]+=word
    return list

def inversComplement(input):
    output = ''
    for letter in input:
        #print(letter)
        if letter == 'A':
            output += 'T'
        elif letter == 'T':
            output += 'A'
        elif letter == 'G':
            output += 'C'
        else:
            output += 'G'
        #print(output)
    return (output[::-1])

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
seq = "ACGTCACGTACGTGTACGCATGATGCATGCTTCAGAGCT"
k = 4
d = 0
patterns = patternList(k)
kmer_freq = defaultdict(int)
for word in patterns:
    for j in range(len(seq)-k+1):
        if(compareMismatch(word,seq[j:j+k],d)==1):
            kmer_freq[word]+=1
        if(compareMismatch(inversComplement(word),seq[j:j+k],d)==1):
            kmer_freq[word]+=1

#print(kmer_freq)

counts = list(kmer_freq.values())
max = max(kmer_freq.values())
for ind,item in enumerate(kmer_freq):
    if counts[ind]==max:
        print(item)

print(len("CATCGACATGCACATGCACATGCAACGTCACGTACGTGTACGCATGATGCATGCTTCAGAGCTACGCATGATGCATGCTTCGCATGATGCATGCTTCAGAGCTACGCATGATGCA"))