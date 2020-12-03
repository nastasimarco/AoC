"""Solution attempt of AoC 2020 puzzle 01.

--- Day 1: Report Repair ---
After saving Christmas five years in a row, you've decided to take a vacation at a nice resort on a tropical island. Surely, Christmas will go on without you.

The tropical island has its own currency and is entirely cash-only. The gold coins used there have a little picture of a starfish; the locals just call them stars. None of the currency exchanges seem to have heard of them, but somehow, you'll need to find fifty of these coins by the time you arrive so you can pay the deposit on your room.

To save your vacation, you need to get all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

Before you leave, the Elves in accounting just need you to fix your expense report (your puzzle input); apparently, something isn't quite adding up.

Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.

For example, suppose your expense report contained the following:

1721
979
366
299
675
1456
In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.

Of course, your expense report is much larger. Find the two entries that sum to 2020; what do you get if you multiply them together?

--- Part Two ---
The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left over from a past vacation. They offer you a second one if you can find three numbers in your expense report that meet the same criteria.

Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. Multiplying them together produces the answer, 241861950.

In your expense report, what is the product of the three entries that sum to 2020?
"""

import numpy as np

report = np.loadtxt('input.txt', dtype=int)

# custom input
# report = np.array([1721, 979, 366, 299, 675, 1456])

report.sort()
# print('sorted report:', report)

def search_n1n2(report, mysum, n1_idx=0, n2_idx=1):
    """
    recursive function to find the two numbers in input array with given sum.
    """
    n1 = report[n1_idx]
    n2 = report[n2_idx]

    if n1 + n2 == mysum:
        return n1, n2
    elif (n1 + n2 < mysum) and (n2_idx + 1 < report.size):
        return search_n1n2(report, mysum, n1_idx, n2_idx + 1)
    elif (n1_idx +2 < report.size):
        return search_n1n2(report, mysum, n1_idx + 1 , n1_idx + 2)
    else:
        return 0, 0

n1, n2 = search_n1n2(report, 2020)
print('--- Part One ---')
print(f'The two numbers with sum 2020 are: {n1} and {n2}.')
print(f'Their product is: {n1*n2}.')

def search_n1n2n3(report):
    for num in report:
        n1, n2 = search_n1n2(report, 2020 - num)
        if num + n1 + n2 == 2020:
            return num, n1, n2
        else:
            pass

n1, n2, n3 = search_n1n2n3(report)
print('--- Part Two ---')
print(f'The three numbers with sum 2020 are: {n1}, {n2} and {n3}.')
print(f'Their product is: {n1*n2*n3}.')