string=input()
List=string.split(" ")
n=len(List[0])
m=len(List[1])
if n==m:
	for i in range(0,n):
		if List[0][i]!=List[1][i]:
			List[0]=List[0].replace(List[0][i],List[1][i])
	if List[0]==List[1]:
		print("yes")
	else:
		print("no")
else:
	print("no")
