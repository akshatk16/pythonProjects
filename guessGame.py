import random

secret = random.randint(1, 9)
result = False
count = 0

while count < 3:
	guess = int(input('Guess: '))
	if guess == secret:
		print("Correct!")
		result = True
		break
	count = count+1
if result == False:
	print(f'Failed! It was {secret}')
input()
