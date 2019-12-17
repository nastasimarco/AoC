"""--- Day 4: Secure Container ---
You arrive at the Venus fuel depot only to discover it's protected by a password. The Elves had written the password on a sticky note, but someone threw it out.

However, they do remember a few key facts about the password:

It is a six-digit number.
The value is within the range given in your puzzle input.
Two adjacent digits are the same (like 22 in 122345).
Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
Other than the range rule, the following are true:

111111 meets these criteria (double 11, never decreases).
223450 does not meet these criteria (decreasing pair of digits 50).
123789 does not meet these criteria (no double).
How many different passwords within the range given in your puzzle input meet these criteria?

Your puzzle input is 284639-748759.

--- Part Two ---
An Elf just remembered one more important detail: the two adjacent matching digits are not part of a larger group of matching digits.

Given this additional criterion, but still ignoring the range rule, the following are now true:

112233 meets these criteria because the digits never decrease and all repeated digits are exactly two digits long.
123444 no longer meets the criteria (the repeated 44 is part of a larger group of 444).
111122 meets the criteria (even though 1 is repeated more than twice, it still contains a double 22).
How many different passwords within the range given in your puzzle input meet all of the criteria?

Your puzzle input is still 284639-748759.
"""
import numpy as np

# custom input
# 111111
# 223450
# 123789

bottom = 284639
top = 748759

def meets_requirement(password):
    digits = [int(digit) for digit in str(password)]
    if len(digits)==6:
        if (sorted(digits) == digits): # check non decreasing
            if (len(set(digits)) == 6): # check if has a double
                return False
            else:
                for i in range(6 - 1):
                    if (digits[i] == digits[i+1]):
                        return True
    else:
        return False

def second_criteria(password):
    digits = [int(digit) for digit in str(password)]
    if (2 in [digits.count(digit) for digit in set(digits)]):
        return True
    else:
        return False

passwords = []
for i in range(bottom, top + 1):
    if meets_requirement(i):
        passwords += [i]

second_passwords = []
for password in passwords:
    if second_criteria(password):
        second_passwords += [password]

# print(passwords[:10], passwords[-10:])
print('Part I')
print('The number of passwords within the range given meeting the criteria is:',
      f'{len(passwords)}')

print('Part II')
print('The number of passwords within the range given meeting the criteria is:',
      f'{len(second_passwords)}')