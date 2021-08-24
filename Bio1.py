Text = "AAGATTCTCTAC"
k = 4
myDict = {}

for i in range(0,len(Text)-k+1):

    kmer = Text[i:i+k]
    Prefix = kmer[0:len(kmer)-1]
    Suffix = kmer[1:len(kmer)]
    if Prefix in myDict:
        LastElement = myDict.pop(Prefix)
        LastElement.append(Suffix)
        myDict[Prefix] = LastElement
    else:
        myDict[Prefix] = [Suffix]


allKeys = sorted(list(myDict.keys()))
for key in allKeys:
    Value = myDict[key]
    if len(Value) == 1:
        print(key + " -> " + Value[0])
    else:
        Value = sorted(Value)
        for j in range(0,len(Value)-1):
            ValueString = Value[j]+","
        print(key + " -> " + ValueString+Value[-1])


