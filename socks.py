l=[]
R=int(input())-1
B=int(input())-1
G=int(input())-1
N=int(input())
pairs=0
def R_decerement():
	if R>0:
		R-=1
		l.append("R")
def B_decrement():
	if B>0:
		B-=1
		l.append("B")
def G_decrement():
	if G>0:
		G-=1
		l.append("G")
def main():
	if N==1:
		print("4")
	else:
		R-=1
		B-=1
		G-=1
		l.append("R")
		l.append("B")
		l.append("G")
		while(len(l))!=(R+B+G+3)):
			for i in range(2):
				R_decrement()
				if(R%2==0):
					pairs+=1
			for i in range(2):
				B_decrement()
				if(B%2==0):
					pairs+=1
			for i in range(2):
				G_decrement()
				if(G%2==0):
					pairs+=1
			if pairs==(N-3):
				break
		draws=len(l)
		print(draws)
main()
