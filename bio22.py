def profile_most_probable_kmer(dna, k, profile):
    '''Returns the profile most probable k-mer for the given input data.'''
    # A dictionary relating nucleotides to their position within the profile.
    nuc_loc = {nucleotide:index for index,nucleotide in enumerate('ACGT')}

    # Initialize the maximum probabily.
    max_probability = -1

    # Compute the probability of the each k-mer, store it if it's currently a maximum.
    for i in range(len(dna)-k+1):
        # Get the current probability.
        current_probability = 1
        for j, nucleotide in enumerate(dna[i:i+k]):
            current_probability *= profile[j][nuc_loc[nucleotide]]

        # Check for a maximum.
        if current_probability > max_probability:
            max_probability = current_probability
            most_probable = dna[i:i+k]

    return most_probable

def MakeProfile(Strings,t):

    Profile = {"A":[1]*len(Strings[0]),"C":[1]*len(Strings[0]),"G":[1]*len(Strings[0]),"T":[1]*len(Strings[0])}
    for j in range(len(Strings[0])):
        for i in range(t):
            if Strings[i][j] == "A":
                Profile["A"][j] += 1
            if Strings[i][j] == "C":
                Profile["C"][j] +=1
            if Strings[i][j] == "G":
                Profile["G"][j] += 1
            if Strings[i][j] == "T":
                Profile["T"][j] +=1
    return Profile

def StrProb(Pattern , Profile):
    prob = 1
    for i in range(len(Pattern)):

        prob = prob* Profile[Pattern[i]][i]
    return prob

def MakeMotifs(Profile,DNA,t,k):
    Motifs = ["" for l in range(t)]
    n = len(DNA[0])
    counter = 0
    for s in DNA:
        Probability = 0
        for j in range(n-k+1):
            CandidPattern = s[j:j+k]
            if StrProb(CandidPattern,Profile) > Probability:
                Probability = StrProb(CandidPattern,Profile)
                Motifs[counter] = CandidPattern
        counter += 1
    return Motifs

def Score(Motifs,t):
    profile = MakeProfile(Motifs,t)
    profileZiped = list(zip(profile["A"],profile["C"],profile["G"],profile["T"]))
    Sum = 0
    for i in range(len(Motifs[0])):
        Sum = Sum + sum(profileZiped[i]) - max(profileZiped[i])
    return Sum

import random

k = 12
t = 25
dna = """GATGGACCGGGCCATACATGGTGACACGCATCAGAAAGCTGTCCCCGTGCCTTATGCGCTGTCTGTTAGTACATCTCTCTCAATGGCCGTATTTTCAGAACAAGTATCACTTGGATCATCATCTACTCGACGGAGGGCGCGCAAGTGGGTATCTCG
TAAAAAGGTATAAGGGAGTCATATCCGCAGTCCTAGTGACCTTTCCCGGCCCTAGCAGTGCTCCGATAGCCCATGGATGAGACGTAACTCGGCTACTGTTTGTGACTCAAGATAGTTGCCGTCGATATCTCGGATTCTGCTTATCGTGTTACGAGC
AACCACGAGTACCTCTGTCGTGGTCCTTCACCAGGACTCGAAATTTGGCTCACGCCCAACGCCAAGATTACGTCGATCGTTCCTGTTGATATCTCGCCGCATATCAGGTTTATACTGATCGGCTCAGTGATTGTTAATCATCGGCGCGGGTTGTCA
TGTCATGTGCGGATACAGTGGTGACACCAGGTCACCTCCGACCTAAAAGCGTTCAAGGTATGGCCCGAAGAGGTAGGTATCTCTTGTGCCCGCTGCTGCTATCACTCCCTGTGAGCCCCGACACGAATGTTAAACCAGTTTATATTCGCTCGTCAT
AACCTAAACCCTTGCTTCCCACCATCCCTGCGAAGCAACCTTATCCGTAGTTCAGTCGCGCTGAACTCGGAAAGTGCGCTCACGAGATTCTAACTTACACTTGTTTAAGTACCACGTCCGGTGGATATCGCTGGCGTTGAAGGATAGTTCTGGTTA
GTGCCCGATATGCCCGTCAGGGTTGAAGTCTGGGAAGTCGTTATCCCAAACGAAATACCCCGTTCGCAGGCGTGATGTATATCCTGATTAGTACCGCGTATAATATTAGTTTCGCACAGGAGCGTGCTTGTTTTGGGTCATGGATTGGGTACAGCA
TAGTCTTCGAGGCATCTACCTGCGACCGAGCTTGCGATCCAAAAGCATACCCATGAAGTTTGCAAATCTTTCTTAGAGCTACAGGTAGATATCCCTGGGCCGGTAACTAGTAATATGTACAGTTTAGTTGTCCTGTACAATACTGATTGGAGTCAG
AGGAGACGTGTTTGGTAGGCGCTCGACCCTTACCCCCCTATCTCGACTGGCATTGGACGTCCTCAGACTGGTGGATTTGACCTAGTGGTTATCACGCACATGGGAGAACCCGGTCAGAATACATCCTGTTACAGTCAGACGCCGGGTCATTCGCAA
TGTGGGGATCGTCTGATTCATCGACGTCATGGAAACGGGGACGGGCCAGTGGTTATCCCATGCTGCCTTTTAGGAATTCTAGGAGGCGTTCCTAAATAGCTCGCCCGACGATATCCTACTTGATTGTGGCGGTATACCTTGCTGAACCTCGCAGTA
CGCAGTGCACTAGTGGCTATCGCCTTTCTATCCCTGAGGCGTTTGCGTTATAAGATCACTCTGTCGGTGTGAAACCACTGAGTCACACTGACCGGTCGACTGGCCCGTCATATGCAAGTTGAAACGCTTACTGCCGGGTATCGCTCTAAGCTCGAC
TACTCGTAACTTCAAAATCTCGTAGGGTCTGCAGAGTAAGAATCCCGGATACTTCAACATTATCGATTCGTCAAGACGTGCGGAGTGGATATCCCTTATTCCTATACGTCACAAGCCGCGGTCAAGTCGCTTACGCACGGTAGAGCGGGAAACCCT
GCTCTAGTACGCCACAGTGCCAGTACATGACCTCACGAGCCGCCACTTACGTTGATATGTTATAAATCACTAGTTTCGTTGGTACAAACAATAAGTGAGAAGCAATGAGCAACTTATCTCATAAAAAGTGTGGTCGTTATCACACATGACATAAAC
GAGACGGTCGTAGAAATTTGCGCTTGCTCGTATCTCAGTATCCTTCAAAGATTGAACCGGATCGCGGCGGCTAATATTGAAATCCTTAGACTTAACGTTGGTATCACTTTAGAATTTCTGACTTGAGGGTAGTGACTAGACAATCATGATGGAAGA
GATCGGTGGCAGTTGAATTAAGACTAGTTATCCCCTGCTTACACTTTTTCCGCCCGGACACGTGTGACGGTAGTTGATATCTCTCAAGTATCCCGACTTCACGTACGATGCCACCCATCTCCGGCAAACACACTTCTATAATATCGTGGAGCCGAA
GTAGGTATCACCAGAGTTCTCTCGGTATGTGGCGCTAAAACCTCTTAGAGTATGAAGGGTGAAGACCAAGCTCATACCACCCCTATATAGGGCTAATTAATTCCACATCCAGGCAAGATGTCACCCTACAGGTCGCTCACTTGTGGAGAACATCAC
GTGGCTATCGCTGTGATCCGTCACACAAAATCAACTTTGTAGTATTTTGGGTAGTCGGGATAACGCGTGGTCTAAGGTGAGCTGCCTTTGATCCGTTGGGTGGCTACCTTGCAAGTTACCGGCTTGTCACTAGATATAACCGGAAGTCTCTGCAAA
TGAGCAGACCCGACAAAGGCCATGACTTCAAAACCGGTTGTGCAGCGACAGGTACTTTAAGTACGGCACCATTAATATCGCTATACTTACGAGTTAGTGGGTATCTCATGCAAACAAACTGCTACTAGGAACTTAGACGAACTTACCAGGAGGATT
AGTGATCTGAGCATAGTATACTGAGAACGTGTGTGTGACCCCTCCAGCGTCCCCGGCTACTGTTCCAGATCCTAACTAATTACTGCTAGCGATCTGGTCGATATCGCTACGGAACGAAGCCGTACAATCGCCCAGAAGCGGTTAGTCAAGGGCGTT
CAAAATGGGAGTACTTCTCGTAGAATAATTCGTCTGTAATTCCTAGGTTCCATAGATAGGCCTCGATAGTGAAATTCCTTCATGCCCCGAGGTGGCGTTGATATCTCCTTTCTAAGCGGTACCCTTAAGAGTACTCGCGATGGGCTTATCCTCCTC
GTTGGTATCACCCCCAATCCTCTTAGTTTACACTGTAAGATTAACGTCAGGGTGTTGTGGATGGCTTTTCTAATTTAGGTCCTCGGGATGCTCAGGTGTTACTATCGGACTGAGTGAATGTAAGTCCGGGTATCAGCCATGAAACCACTGGAGATC
CCTCGGAAAACGTCGTAAGTGGTATCACAATCCACTAGTCACGGAGGGCGGTGAGTGTCTCGATGCTCAACCCCCAACCCTCAGATGAGGCTATCTGTAGGTATCACTTACGTCACTACGGGGAACAGCTCGCCTTAAGTGTAGGCTAGGTATATG
GGCGGCTCCATCCGATGTGACGGATTTCATGAGGCACAAGCGCTTCACTCCCTATTTGGCTCGTGACAAAGTTCAACGGCTTTGCAGATATCCATGGTCGTTATCCCGGTGGTGAACCTACCGTCAAGTCTCTACAGTGCGCGAAGTGTCCCGGGC
TACTAGTATAAGTTCCGAGCCAAATGGATGGCCCAGGCGCACTAGTGTTAGAAGGATTCGGGCTGTAGGTACATCAAGCTCGAATTTGTCCCACGTCATTCTGGGCCACCCGGACCACAGAAGACCTCTCTCTGTGCCGACGGTGTGGTTATCACG
GTGGTTATCACCGGGATCGAATACAGATACGTCTGGTACATGCCTTGTCATTATTCATACGCCCCCTGGGCCAACAATCCTTTGTCAACCGCGGTCAAAAAGGTAACTAGGATCGGCTTGATCTCTAATTCCGGACTGTTCACCACGGGTCGACCG
CATCACGCAATGCGAACGACTGAAGAAGGCAAGGACAGTTACGCAACCTATCATGCGTAGATCAAGGTAATCGGGACCGGTCTGGAATTTAGGAGTGTTGTTATCGCAACCTGCGATCATAACATCCTCTTATTGCCTATAAACCGACCCTGACCG"""
dna = dna.split("\n")
Motifs = ["" for i in range(t)]
def SymbolToNumber(Symbol):
    if Symbol == "A":
        return 0
    elif Symbol == "C":
        return 1
    elif Symbol == "G":
        return 2
    elif Symbol == "T":
        return 3

def NumberToSymbol(index):
    if index == 0:
        return str("A")
    elif index == 1:
        return str("C")
    elif index == 2:
        return str("G")
    elif index == 3:
        return str("T")
def window(s, k):
    for i in range(1 + len(s) - k):
        yield s[i:i+k]
def ProfileMostProbable(Text, k, Profile):

    letter = [[] for key in range(k)]
    probable = ""
    hamdict = {}
    index = 1
    for a in range(k):
        for j in "ACGT":
            letter[a].append(Profile[j][a])
    for b in range(len(letter)):
        number = max(letter[b])
        probable += str(NumberToSymbol(letter[b].index(number)))
    for c in window(Text, k):
        for x in range(len(c)):
            y = SymbolToNumber(c[x])
            index *= float(letter[x][y])
        hamdict[c] = index
        index = 1
    for pat, ham in hamdict.items():
        if ham == max(hamdict.values()):
            final = pat
            break
    return final
def main():
    Motifs = ["" for i in range(t)]
    for i in range(t):
        Motifs[i] = dna[i][:k]
    BestMotifs = Motifs
    for indx in range(len(dna[0])-k+1):
        Motifs[0] = dna[0][indx:indx+k]
        for i in range(t-1):
            Profile = MakeProfile(Motifs[i+1][:], t)
            Motifs[i+1] = ProfileMostProbable(dna[i+1], k, Profile)
        if Score(Motifs,t) < Score(BestMotifs,t):
            BestMotifs = Motifs
    return BestMotifs

xMotif = main()
print(xMotif)

