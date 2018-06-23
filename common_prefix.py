N=int(input())
l=[]
temp=0
flag=0
for i in N:
	s=input()
	n=len(s)
	List=list(s)
	l.append(List)
	if n>temp:
		temp=n
for i in range(temp):
	for j in range(N):
		if(l[0][i]!=l[j][i]):
			flag=1
			break
	if flag==1:
		print(l[0][:i])
		break
