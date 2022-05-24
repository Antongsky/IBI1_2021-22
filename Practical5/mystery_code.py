# What does this piece of code do?
# Answer: There is a loop adding progress from 1-10. Each time a random number n is generated. As progress turned to 10, the number is printed.

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

progress=0
while progress<10:
	progress+=1
	print(progress)
	n = randint(1,100)
print(n)
