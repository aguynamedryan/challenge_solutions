# -*- coding: utf-8 -*-
"""
Question:
A complement of a number is defined as inversion (if the bit value = 0, change it to 1 and vice-versa) of all bits of the number starting from the leftmost bit that is set to 1.
For example, if N = 5, N is 101 in binary. The complement of N is 010, which is 2 in decimal. Similarly if N = 50, then complement of N is 13
Complete the function getIntegerComplement(). This function takes N as it's parameter. The function should return the complement of N.

Constraints :
0 ≤ N ≤ 100000.
Sample Test Cases:

Input #00:
50

Output #00:
13

Explanation:
50 in decimal form equals: 110010.
Inverting the bit sequence: 001101. This is 13 in decimal
Input #01:
100

Output #01:
27

Explanation:
The bit sequence for 100 equals 1100100.
Inverting the sequence we get 0011011 which is 27 in decimal


"""

"""
Solution

Wrote this one to show off my one-liner skills.
"""
import re
def getIntegerComplement(n):
  return int(re.sub(r'!', '0', re.sub(r'0', '1', re.sub(r'1', '!', bin(n)[2:9999]))), 2)

if __name__ == "__main__":
    print getIntegerComplement(50)
