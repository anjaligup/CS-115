'''
Created on 19 October 2023
@author:   Anjali Gupta
Pledge:    I pledge my honor that I have abided by the Stevens Honor System

CS115 - Lab 6
'''
def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    if n %2 == 0:
        return False
    else:
        return True

'''
Answers to Questions:
42 base 10 into base 2 --> 101010

If I am given an odd base 10 number, the least-signficant bit would be 1 and
for a even base 10 number, the least-significant bit would be 0

if you remove the rightmost digit from a base 2 number, the value of the original number will be divided by 2 

if N is odd, you would add a 1 to the rightmost base 2 digit
if N is even, you would add a 0 to the rightmost base 2 digit

2012 is the ternary conversion of 59 
'''

def numToBinary(n): #returns string
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n == 0:
        return ''
    elif n % 2 == 0:
        return numToBinary(n//2) + '0'
    else:
        return numToBinary(n//2) + '1'
        

def binaryToNum(s): #returns integer value 
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if s == '':
        return 0
    elif s[-1] == '1':
        return 2*binaryToNum(s[:-1]) + 1
    else:
        return 2*binaryToNum(s[:-1]) 
        

def increment(s):
    '''Precondition: s is a string of 8 bits.
    Returns the binary representation of binaryToNum(s) + 1.'''
    if s == '11111111':
        return '00000000'
    else:
        x = numToBinary(binaryToNum(s) + 1)
        return '0' * (8-len(x)) + x
    
    

def count(s, n):
    '''Precondition: s is an 8-bit string and n >= 0.
    Prints s and its n successors.'''
    if n > 0:
        print(s)
        return count(increment(s), n-1)
    else:
        return print(s)


def numToTernary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the ternary representation of non-negative integer
    n. If n is 0, the empty string is returned.'''
    if n == 0:
        return ''
    else:
        return str(numToTernary(n//3)) + str(n%3)
    

def ternaryToNum(s):
    '''Precondition: s is a string of 0s, 1s, and 2s.
    Returns the integer corresponding to the ternary representation in s.
    Note: the empty string represents 0.'''
    if s == '':
        return 0
    elif s[-1] == '2':
        return 3*ternaryToNum(s[:-1]) + 2
    elif s[-1] == '1':
        return 3*ternaryToNum(s[:-1]) + 1
    else:
        return 3*ternaryToNum(s[:-1]) 
    

