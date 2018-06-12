s=input()
n=len(s)
if n<=100000 and n>=1:
	l=s.split(" ")
	List=[]
	for i in l:
		List.append(i[::-1])
	s=" ".join(List)
	print(s)
