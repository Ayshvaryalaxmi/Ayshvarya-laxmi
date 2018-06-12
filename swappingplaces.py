s=input()
List=list(s)
n=len(List)
for i in range(0,n-1,2):
	List[i],List[i+1]=List[i+1]+List[i]
string="".join(List)
print(string)
