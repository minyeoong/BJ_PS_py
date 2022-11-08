import itertools
nanjaeng=[]
for i in range(9):
    nanjaeng.append(int(input()))
nC7=list(itertools.combinations(nanjaeng,7))
print(nC7[0])
for i in range(len(nC7)):
    if(sum(nC7[i])==100):
        nanlist = list(nC7[i])
nanlist.sort()
for i in nanlist:
    print(i)
    