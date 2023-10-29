'''
Created on 26 September 2023
@author:   Anjali Gupta
Pledge:    I pledge my honor that I have abided by the Stevens Honor System
CS115 - Hw 2
'''
import sys, unittest, operator, hw2, functools

Dictionary = ["a", "am", "at", "apple", "bat", "bar", "babble", "can", "foo",
"spam", "spammy", "zzyzva"]

# Allows up to 10000 recursive calls.
# The maximum permitted limit varies from system to system.
sys.setrecursionlimit(10000)

# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a','am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

# Implement your functions here.
def letterScore(letter, scrabbleScores):
    '''this function takes an input as a single letter and returns a single number associated with the given letter'''
    if letter == '':
        return 0
    elif letter == scrabbleScores[0][0]:
        return scrabbleScores[0][1]
    else:
        return letterScore(letter, scrabbleScores[1:])

###################################
    
def wordScore(S, scoreList):
    '''this function takes in an input as a string and returns an ouput as the scrabble score of that string'''
    if S == '':
        return 0
    else:
        return letterScore(S[0], scoreList) + wordScore(S[1:], scoreList)

##################################
    
def whetherString(S, Rack):
    '''function checks if a given word in dictionary can be formed with the Rack list'''
    if S == '':
        return True
    elif S[0] in Rack:
        Rack.remove(S[0])
        return whetherString(S[1:], Rack)
    else:
        return False
 
###################################
    
def scoreList(Rack):
    '''this function returns a list of words that can be made by Rack and its corresponding score'''
    x = list(filter(lambda wrd: whetherString(wrd, Rack[:]) , Dictionary)) #returns list of words
    new = list(map(lambda wrd: [wrd, wordScore(wrd, scrabbleScores)], x))
    return new

###################################

def compare_scores(x,y):
    '''takes two inputs, each with the format ["string", number] and returns whichever number and string is greater'''
    if x[1] > y[1]:
        return x
    else:
        return y

def bestWord(Rack):
    '''This function returns the highest scoring word and its score that can be made given the rack'''
    new_score_list = scoreList(Rack)
    if new_score_list == []:
        return ["", 0]
    else:
        highest_score = functools.reduce(compare_scores, new_score_list)
        return highest_score
    
    
    
    

