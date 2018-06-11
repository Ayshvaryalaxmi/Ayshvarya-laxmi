character=str(input())
l=['a','e','i','o','u']
if character.isalpha():
	if(character in l):
		print("Vowel")
	else:
		print("Consonant")
else:
	print("Invalid input")
