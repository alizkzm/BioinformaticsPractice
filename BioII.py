


k = 3
t = 5
dna = """GGCGTTCAGGCA
AAGAATCAGTCA
CAAGGAGTTCGC
CACGTCAATCAC
CAATAATATTCG"""
dna = dna.split("\n")


print(dna[0])
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
def MakeMotifs(Profile,dna,t,k):
    Motifs = ["" for l in range(t)]
    n = len(dna[0])
    counter = 0
    for s in dna:
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
def profile_most_probable_kmer(dna, k, profile):
    nuc_loc = {nucleotide:index for index,nucleotide in enumerate('ACGT')}
    max_probability = -1
    for i in range(len(dna)-k+1):
        current_probability = 1
        for j, nucleotide in enumerate(dna[i:i+k]):
            current_probability *= profile[j][nuc_loc[nucleotide]]

        if current_probability > max_probability:
            max_probability = current_probability
            most_probable = dna[i:i+k]
    return most_probable

def main():
    Motifs = ["" for i in range(t)]
    for i in range(t):
        Motifs[i] = dna[i][:k]
    BestMotifs = Motifs
    for indx in range(len(dna[0])-k+1):
        Motifs[0] = dna[0][indx:indx+k]
        for i in range(t-1):
            m = []
            for l in range(i+1):
                m.append(Motifs[l])
            print(m)
            Profile = MakeProfile(dna, t)
            print(Motifs[2])
            print(Profile)
            Motifs[i+1] = profile_most_probable_kmer(dna[i+1], k, Profile)
        if Score(Motifs,t) < Score(BestMotifs,t):
            BestMotifs = Motifs
    return BestMotifs

xMotif = main()
for j in range(t):
    print(xMotif[j])