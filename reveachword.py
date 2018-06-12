s=input()
n=len(s)
l=s.split(" ")
List=[]
for i in l:
	List.append(i[::-1])
s=" ".join(List)
print(s)
