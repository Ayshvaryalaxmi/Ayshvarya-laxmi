str=input()
if str.isdigit():
	num=int(str)
	n=0
	temp=0
	while num>0:
		temp=num%10
		n=n*10+temp
		num=int(num/10)
	print(n)
else:
	print("Invalid input")
