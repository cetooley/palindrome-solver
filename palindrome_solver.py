#!/usr/bin/python

# find i and j such that i, j, is a certain number length and their resulting product is the largest palindromic number (e.g. 12233221, 6762676)
# for example, find the largest palindrome p such that i, j are integers of length 4.
# why am I publishing this? I want to know if this is mathematically valid! I don't know how I would go about proving this or not.

import argparse

parser = argparse.ArgumentParser(prog='palindrome_solver.py', description="Small program to find max palindromic numbers given an integer length" )
parser.add_argument( '-l', '--length', type=int, default=3, help='The maximum length of the integer (999 is length 3)' )
args = parser.parse_args()

max_palindrome = 0
count = 0
palin_i = int(pow(10, args.length-1)) #100 for length=3
palin_j = int(pow(10, args.length-1))
from_max = int(pow(10, args.length ) )-1 #999 for length=3

#count down from the highest value for i
for i in range(from_max,palin_i, -1):
    #for j in range(from_max,i,-1): #this seems to do less loops but is actually slower!
    for j in range(i,palin_j,-1):
        count = count+1
        if i*j < max_palindrome:
            #don't bother with any more j
            break
        #easy to check whether it's a palindrome with str
        #just reverse the string and determine whether it's the same as unreversed.
        if max_palindrome < i*j and str(i*j) == str(i*j)[::-1]:
            max_palindrome = i*j
            palin_i = i
            palin_j = j

print "Palindrome:\t\t" + str( max_palindrome)
print "i value:\t\t" + str( palin_i )
print "j value:\t\t" + str( palin_j )
print "Loop Count:\t\t" + str( count )
