#input
string="GATATATGCATATACTT"
seq="ATAT"

n=len(string)
k=len(seq)
for i in range(n-k+1):
    if string[i:i+k]==seq:
        print(i)
