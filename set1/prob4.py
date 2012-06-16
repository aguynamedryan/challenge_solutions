# -*- coding: utf-8 -*-
"""
Question:
Complete the function getEqualSumSubstring, which takes a single argument. The single argument is a string s, which contains only non-zero digits.  This function should print the length of longest contiguous substring of s, such that the length of the substring is2*N digits and the sum of the leftmost N digits is equal to the sum of the rightmost N digits.If there is no such string, your function should print 0.

Sample Test Cases:   Input #00: 123231  Output #00: 6  Explanation: 1 + 2 + 3 = 2 + 3 + 1.  The length of the longest substring = 6 where the sum of 1st half = 2nd half

Input #01: 986561517416921217551395112859219257312  Output #01: 36
"""

""" Solution """
def firstHalfOfString(s):
  return s[0:len(s) / 2]

def secondHalfOfString(s):
  return s[len(s) / 2:len(s)]

def sumString(string):
  someSum = 0

  for num in string:
    someSum += int(num)

  return someSum

def isEqualSumSubstring(string):
  if (len(string) % 2 == 1):
    return 0

  if (sumString(firstHalfOfString(string)) == sumString(secondHalfOfString(string))):
    return 1

  return 0

def getEqualSumSubstring(string):
  from collections import deque
  # The queue will store all the strings we need to check
  # We start by checking the entire string
  queue = deque([string])

  while len(queue) != 0:
    s = queue.popleft();

    # The first string that matches our criteria is,
    # by design, the longest so we're done.
    # Return the length!
    if (isEqualSumSubstring(s)):
      return len(s)

    # If the current string isn't our winner we'll add
    # to the queue two new substrings of the current string
    # We trim a character off either end of the current string
    # and feed it into the queue
    #
    # In this way, the queue will get filled
    # with all possible substrings of the initial string
    # until either a string matches our criteria,
    # or the string becomes the empty string, meaning
    # there is no match
    if (len(s) - 1 > 0):
      queue.append(s[0:len(s) - 1])
      queue.append(s[1:len(s)])

  return 0

if __name__ == "__main__":
    print getEqualSumSubstring('986561517416921217551395112859219257312')
