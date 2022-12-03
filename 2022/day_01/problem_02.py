'''
--- Part Two ---
By the time you calculate the answer to the Elves' question, they've already realized that the Elf carrying
the most Calories of food might eventually run out of snacks.

To avoid this unacceptable situation, the Elves would instead like to know the total Calories carried by the top
three Elves carrying the most Calories. That way, even if one of those Elves runs out of snacks, they still have
two backups.

In the example above, the top three Elves are the fourth Elf (with 24000 Calories), then the third Elf
(with 11000 Calories), then the fifth Elf (with 10000 Calories). The sum of the Calories carried by these three
elves is 45000.

Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?
'''


lst = []
total = 0
with open('./input.txt') as f:
    for line in f:
        if line.strip():
            total += int(line)           
        else:
            lst.append(total)
            total = 0
    else:  # eof
        lst.append(total)
        total = 0  

lst.sort(reverse=True)
top_3_sum = sum(lst[:3])

print(top_3_sum)
