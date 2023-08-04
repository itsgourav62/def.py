# Python program to iterate
# over 3 lists using zip function

import itertools

num = [1, 2, 3]
color = ['yellow', 'orange', 'black']
value = [55, 56,57]

for (a, b, c) in zip(num, color, value):
	print (a, b, c)
