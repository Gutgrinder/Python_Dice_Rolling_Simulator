import random
abfrage = 'j'
while abfrage != 'n':
	
	MaxZahl = input('Wie viele Seiten hat der Wuerfel? ')
	print('Der Wuerfel zeigt die Zahl: ', random.randint(1, int(MaxZahl)))
	abfrage = input ('Willst du noch einmal Wuerflen? (j/n): ')

