def BWmatching(F,L,Pattern):
    top = 0
    bottom = len(L)-1
    while top <= bottom:
        if len(Pattern) > 0:
            Symbol = Pattern[-1]
            Pattern = Pattern[:-1]
            print(Pattern)
            if L[top:bottom+1].count(Symbol) > 0 :
                top = F.find(Symbol) + L[0:top].count(Symbol)
                bottom = F.find(Symbol) + L[0:bottom+1].count(Symbol) -1
            else:
                return 0
        else:
            return bottom-top+1

Last = "TCCTCTATGAGATCCTATTCTATGAAACCTTCA$GACCAAAATTCTCCGGC"
First = ''.join(sorted(Last))
Patterns = "CCT CAC GAG CAG ATC"

print(First)

Patterns  = Patterns.split()
answer = list()
for i in range(len(Patterns)):
    answer.append(BWmatching(First,Last,Patterns[i]))

print(*answer , sep=" ")