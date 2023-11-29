'''
Created on 10/31/2023
@author: Anjali Gupta & Aishnavi Alalasundram
Pledge: I pledge my honor that I have abided by the Stevens Honor System - AG, AA
CS115 - Hw 6
'''
# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5
# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1 #equals 31
# Do not change the variables above.
# Write your functions here. You may use those variables in your code.

#place helper functions here:
def count0(S):
  '''counts consecutive 0's in binary string'''
  if S == '':
    return 0
  else:
    if S[0] == '0':
      return 1 + count0(S[1:])
    else:
      return 0

def count1(S):
  '''counts consecutive 1's in binary string'''
  if S == '':
    return 0
  else:
    if S[0] == '1':
      return 1 + count1(S[1:])
    else:
      return 0

def pad(S):
  '''pads each 5 bit binary string with zeros if it doesn't already have zeros '''
  numberOfZeros = "0" * (COMPRESSED_BLOCK_SIZE - len(S))
  return numberOfZeros + S


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


#compress function
def compress(S):
  '''this function takes in a 64-bit binary string and returns run-length encoding of the input string'''
  if S == '':
    return ''
  else:
    zeros = count0(S[:MAX_RUN_LENGTH]) #number of zeros found in string
    if S[zeros:] == '':
      return pad(numToBinary(zeros))
    else:
      ones = count1(S[zeros:zeros+MAX_RUN_LENGTH])
      binary1 = numToBinary(ones)
      x = pad(numToBinary(zeros)) + pad(binary1) + compress(S[zeros+ones:])
      return x

'''
  the largest number of bits 
'''

def uncompress(C):
  '''this function uncompresses the compressed binary string'''
  if C == '':
    return ''
  else:
    zeros = binaryToNum(C[:COMPRESSED_BLOCK_SIZE])
    ones = binaryToNum(C[COMPRESSED_BLOCK_SIZE:COMPRESSED_BLOCK_SIZE*2])
    if zeros == 0:
      return '1' * ones + uncompress(C[COMPRESSED_BLOCK_SIZE*2:])
    else:
      return '0' * zeros + '1' * ones + uncompress(C[COMPRESSED_BLOCK_SIZE*2:])


def compression(S):
  '''returns the ratio of the compressed size to the original size for image S'''
  return len(compress(S))/len(S)


#The largest number of bits that the compress algorithm could possibly use
#to encode a 64-bit string/image is 7 because 2**6 is 64, including 2**0.

#In the compression ratios, the ratio decreases when the consecutive
#numbers grow higher. An example of this is 1111 is 11 in binary. Compressions
#with more than the same three consecutive numbers could be smaller than the
#uncompressed base.  

#Lai's algorithm shouldn't exist because rewriting a 64 bit string into a shorter #string doesn't make sense and wouldn't work, therefore it has to be represented by #at least a 64 bit string to keep the bit order going. 
