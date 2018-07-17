s=input().split(" ")
changes=abs(len(s[1])-len(s[0]))
n=len(s[0])
if n>len(s[1]):
	n=len(s[1])
for num in range(n):
	if s[0][num]!=s[1][num]:
		changes+=1
print(changes)
