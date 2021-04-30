import random

coin = random.randint(1, 2)

def game():

	if coin == 1:
		return 'yes'
	else:
		return 'no'

print(game())