l=[]
S=input()
s=S.split(" ")
R=int(s[0])
B=int(s[1])
G=int(s[2])
N=int(input())
total=R+B+G
pairs=0
if N==1:
	print("4")
else:
	R-=1
	B-=1
	G-=1
	l.append("R")
	l.append("B")
	l.append("G")
	while len(l)<total:
		for i in range(2):
			if R>0 and pairs!=N:
				R-=1
				l.append("R")
				if(R%2==0):
					pairs+=1
		if pairs==(N):
			break
		for i in range(2):
			if B>0 and pairs!=N:
				B-=1
				l.append("B")
				if(B%2==0):
					pairs+=1
		if pairs==(N):
			break
		for i in range(2):
			if G>0 and pairs!=N:
				G-=1
				l.append("G")
				if(G%2==0):
					pairs+=1
		if pairs==(N):
			break
	draws=len(l)
	print(draws)
