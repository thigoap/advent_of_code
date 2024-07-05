'''
--- Part Two ---
Now, given the same instructions, find the position of the first character that causes him to enter the basement (floor -1). The first character in the instructions has position 1, the second character has position 2, and so on.

For example:

) causes him to enter the basement at character position 1.
()()) causes him to enter the basement at character position 5.
What is the position of the character that causes Santa to first enter the basement?
'''


file = open('./input.txt', mode='r')
floor = 0

all = file.read()
for index, char in enumerate(all):
	if '(' in char:
		floor += 1
		if floor == -1:
			print(index + 1)
			break	
	else:
		floor -= 1
		if floor == -1:
			print(index + 1)
			break