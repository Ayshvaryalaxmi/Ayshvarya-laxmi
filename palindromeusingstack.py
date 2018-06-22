s=input()
stack=list(s)
l=stack[:]
L=[]
for i in s:
	L.append(stack.pop())
if L==l:
	print("YES")
else:
	print("NO")
