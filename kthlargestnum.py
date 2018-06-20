List=[]
s=input()
s=s.split(" ")
n=int(s[0])
k=int(s[1])
l=input()
l=l.split(" ")
for i in l:
	List.append(int(i))
L=sorted(List, reverse=True)
print(L[k-1])
