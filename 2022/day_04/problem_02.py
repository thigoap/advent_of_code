'''
--- Part Two ---
It seems like there is still quite a bit of duplicate work planned. Instead, the Elves would like to know the number of pairs that overlap at all.

In the above example, the first two pairs (2-4,6-8 and 2-3,4-5) don't overlap, while the remaining four pairs (5-7,7-9, 2-8,3-7, 6-6,4-6, and 2-6,4-8) do overlap:

5-7,7-9 overlaps in a single section, 7.
2-8,3-7 overlaps all of the sections 3 through 7.
6-6,4-6 overlaps in a single section, 6.
2-6,4-8 overlaps in sections 4, 5, and 6.
So, in this example, the number of overlapping assignment pairs is 4.

In how many assignment pairs do the ranges overlap?
'''

partial = 0
with open('./input.txt') as f:
    lst = f.read().splitlines()
    for item in lst:
        item_01 = item.split(',')[0]
        item_01_01 = item_01.split('-')[0]
        item_01_02 = item_01.split('-')[1]
        item_01_lst = [x for x in range(int(item_01_01), int(item_01_02) + 1)]
        item_02 = item.split(',')[1]
        item_02_01 = item_02.split('-')[0]
        item_02_02 = item_02.split('-')[1]
        item_02_lst = [x for x in range(int(item_02_01), int(item_02_02) + 1)]
        check_01 =  any(item in item_01_lst for item in item_02_lst)
        check_02 =  any(item in item_02_lst for item in item_01_lst)
        if check_01 or check_02: 
            partial += 1

print(partial)