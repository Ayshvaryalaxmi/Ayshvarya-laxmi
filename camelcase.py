#print(input().title())
n=input()
Lis=[]
List=n.split(" ")
for word in List:
	word=word[0].upper()+word[1:].lower()
	Lis.append(word)
string=" ".join(Lis)
print(string)
