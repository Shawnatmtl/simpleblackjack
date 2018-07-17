import random
import time

deck = list('234567890JQKA'*4)
random.shuffle(deck)
value = { '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, 
			'9':9, '0':10, 'J':10, 'Q':10, 'K':10, 'A':1}
player = [deck.pop() for _ in range(2)]
cpu = [deck.pop() for _ in range(2)]

def check(who, hand):
	subtotal = sum(map(value.get, hand))
	if subtotal > 21:
		return print('{} loses'.format(who), *hand)
	if len(hand)>4:
		return print('{} wins'.format(who))
	total =[item for item in  
			[subtotal] + list(range(subtotal, subtotal +10*hand.count('A')+1,10))
			if item <=21]
	if 21 == total[-1]:
		return print('{} wins.'.format(who), *hand)	
	
	return total
	


while 1:
	pl, cp = check('Player',player) , check('DEALER',cpu)
	if not pl or not cp:
		break
	print(*player)
	p = input('Enter to stay. ')
	if p:
		player.append(deck.pop())
	ai =  sum(map(value.get, cpu))<15
	if ai:
		cpu.append(deck.pop())
	if not p and not ai:
		if pl[-1]>cp[-1]:
			print('player wins.')
		elif pl[-1] <cp[-1]:
			print('DEALER wins.')
		else: 
			print('Tie')
		print('Player:', *player)
		print('DEALER:', *cpu)
		break



