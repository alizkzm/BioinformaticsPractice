import math
X = "zxxxxyzzxyxyxyzxzzxzzzyzzxxxzxxyyyzxyxzyxyxyzyyyyzzyyyyzzxzxzyzzzzyxzxxxyxxxxyyzyyzyyyxzzzzyzxyzzyyy"
States = "A   B"
Emission = """0.532	0.226	0.241	
0.457	0.192	0.351"""
Transition = """0.634	0.366	
0.387	0.613"""


States = States.split()
NumericalStates = {}
for i in range(len(States)):
    NumericalStates[States[i]] = i

alphabet = sorted(set(X))
NumericalAlphabet = {}
for i in range(len(alphabet)):
    NumericalAlphabet[alphabet[i]] = i


Emission = Emission.split("\n")
for i in range(len(Emission)):
    Emission[i] = (Emission[i].split())
NumericalEmission = [[] for i in range(len(Emission))]
for i in range(len(Emission)):
    for j in range(len(Emission[0])):
        NumericalEmission[i].append(float(Emission[i][j]))

Transition = Transition.split("\n")
for i in range(len(Transition)):
    Transition[i] = (Transition[i].split())
NumericalTransition = [[] for i in range(len(Transition))]
for i in range(len(Transition)):
    for j in range(len(Transition[0])):
        NumericalTransition[i].append(float(Transition[i][j]))

Nstates = len(States)
s = [[0]*len(X) for i in range(Nstates)]
for i in range(Nstates):
    s[i][0] = math.log10(NumericalEmission[NumericalStates[States[i]]][NumericalAlphabet[X[0]]]/Nstates)
FinalPath = []
for j in range(1,len(X)):
    LastState = []
    for i in range(Nstates):
        ski = []

        for k in range(Nstates):
            ski.append(s[k][j-1] + math.log10(NumericalEmission[NumericalStates[States[i]]][NumericalAlphabet[X[j]]])  + math.log10(NumericalTransition[NumericalStates[States[k]]][NumericalStates[States[i]]]) )

        s[i][j] = max(ski)
        LastState.append( States[ski.index(s[i][j])] )

    maxS = s[0][j]
    IndexMaxS = 0
    for ii in range(1,Nstates):
        if s[ii][j] > maxS:
            maxS = s[ii][j]
            IndexMaxS = ii
    FinalPath.append(LastState[IndexMaxS])

maxAkharinState = s[0][len(X)-1]
lastLetter = States[0]
for i in range(1,Nstates):
    if s[i][len(X)-1] > maxAkharinState:
        maxAkharinState = s[i][len(X)-1]
        lastLetter = States[i]
FinalPath.append(lastLetter)
FinalPath = "".join(FinalPath)
print(FinalPath)