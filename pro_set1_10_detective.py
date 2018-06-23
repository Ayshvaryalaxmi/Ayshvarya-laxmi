N=int(input())
s=input()
l=s.split(" ")
sum=0
for i in l:
	for j in range(int(i)):
		sum+=j
print(sum)
