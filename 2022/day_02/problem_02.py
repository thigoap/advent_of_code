'''
--- Part Two ---
The Elf finishes helping with the tent and sneaks back over to you. "Anyway, the second column says how the round needs to end: X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win. Good luck!"

The total score is still calculated in the same way, but now you need to figure out what shape to choose so the round ends as indicated. The example above now goes like this:

In the first round, your opponent will choose Rock (A), and you need the round to end in a draw (Y), so you also choose Rock. This gives you a score of 1 + 3 = 4.
In the second round, your opponent will choose Paper (B), and you choose Rock so you lose (X) with a score of 1 + 0 = 1.
In the third round, you will defeat your opponent's Scissors with Rock for a score of 1 + 6 = 7.
Now that you're correctly decrypting the ultra top secret strategy guide, you would get a total score of 12.

Following the Elf's instructions for the second column, what would your total score be if everything goes exactly according to your strategy guide?

A for Rock, B for Paper, and C for Scissors
X for Rock, Y for Paper, and Z for Scissors

X beats C - +1
Y beats A - +2
Z beats B - +3

win - +6
draw - +3
lose - +0
'''


game_dict = {
    "X": [["A",3],["B",1],["C",2]],  # lose
    "Y": [["A",4],["B",5],["C",6]],  # draw
    "Z": [["A",8],["B",9],["C",7]]  # win
}

total = 0
with open('./input.txt') as f:
    for line in f:
        opponent = line.split()[0]
        me = line.split()[1]
        choice = game_dict[me]
        for opponent_choice in choice:
            if opponent == opponent_choice[0]:
                total += opponent_choice[1]
                break
print(total)
