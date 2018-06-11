character=str(input())
l=['a','e','i','o','u']
if character.isalpha():
	if(character in l):
		print("vowel")
	else:
		print("consonant")
else:
	print("Invalid input"
