import math


def Hamm(PatternA,PatternB):
    Hamm = 0
    for i in range(len(PatternB)):
        if PatternA[i] != PatternB[i]:
            Hamm += 1
    return Hamm


def HammDistPattAndText(Pattern,Text):
    distance = math.inf
    for i in range(0,len(Text)-len(Pattern)+1):
        HammDisA_B = Hamm(Pattern,Text[i:i+len(Pattern)])
        if HammDisA_B < distance:
            distance = HammDisA_B
    return distance


def HammDNAandPattern(DNA,Pattern):
    Sum = 0
    for i in range(len(DNA)):
        Sum += HammDistPattAndText(Pattern,DNA[i])
    return Sum

def NumberToSymbol(number):
    if number == 0:
        return "A"
    if number == 1:
        return "C"
    if number == 2:
        return "G"
    if number == 3:
        return "T"


def NumberToPattern(number,k):
    if k == 1:
        return NumberToSymbol(number)
    preIndex = number // 4
    r = number%4
    symbol = NumberToSymbol(r)
    PrefixPattern = NumberToPattern(preIndex,k-1)
    return symbol + PrefixPattern

k = 6

DNA = """CTATGAAGGGTAACCGTGATTAGCGAATATACTATGGGCGAC
ATCGTAAGAATGAAAATGCTTCCTGGTATCACAATGCGACTT
GTACCTAGTTTTAATAAGACAATGGCGGCCGCAGACTGATTG
CTTTCAAATATTGCCGCTGATGCACTATAGACGATGTTGTTA
TCATCGTCATGGGCCAGTGTTCAAACAATGTAATTGATTGCG
CCTGGACCCGCGAACCGCACAATGCTCTATTATGACTTGTGA
GGGCCCCAGGATCCACCTGTGTTACTTTGCACGATGTTACAC
GGGCCAGTGTCTACTATGTTGGCGAGGGAACGCACACAATTC
TTTGAGTGCTGGACTATGCAATTACCTACAGGGCGCAGCCGG
ACCATGTTGTGATTTCTTGCTACAACTGGTTGGCCCTAGTAG"""

DNA = DNA.split("\n")
dist = math.inf
for i in range((4**k) - 1):
    CandidPattern = NumberToPattern(i,k)
    HammAandB = HammDNAandPattern(DNA, CandidPattern)
    if HammAandB < dist:
        dist = HammAandB
        Median = CandidPattern

print(Median)