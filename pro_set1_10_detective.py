N=int(input())
s=input()
l=s.split(" ")
sum=0
for i in range(N):
	for j in range(int(l[i])):
		#print(l[:i])
		#print(j)
		m=str(j)
		if m in l[:i]:
			sum=sum+j
print(sum)
