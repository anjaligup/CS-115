'''
Created on 9 October 2023
@author:   Anjali Gupta
Pledge:    I pledge my honor that I have abided by the Stevens Honor System

CS115 - Hw 3
'''
# Be sure to submit hw3.py.  Remove the '_template' from the file name.

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 0
' Implement the function giveChange() here:
' See the PDF in Canvas for more details.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def giveChange(amount, coins):
    '''returns a list in the form [amount of coins used, [list of all coins used]] to make the amount number'''
    if amount == 0:
        return [0, []]
    if coins == []:
        return [float('inf'), []]
    elif amount == coins[0]:
        return [1, [coins[0]]]
    elif amount < coins[0]:
        return giveChange(amount, coins[1:])
    else:
        useit = giveChange(amount-coins[0], coins)
        loseit = giveChange(amount, coins[1:])
        useit_2 = (useit[0] + 1 , [coins[0]]+useit[1])
    if useit_2[0]<loseit[0]:
        return useit_2
    else:
        return loseit



# Here's the list of letter values and a small dictionary to use.
# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 1
' Implement wordsWithScore() which is specified below.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def wordsWithScore(dct, scores):
    '''List of words in dct, with their Scrabble score.

    Assume dct is a list of words and scores is a list of [letter,number]
    pairs. Return the dictionary annotated so each word is paired with its
    value. For example, wordsWithScore(Dictionary, scrabbleScores) should
    return [['a', 1], ['am', 4], ['at', 2] ...etc... ]
    '''
    def letterScore(letter, scores):
        '''returns the input, a letter, and its cooresponding scrabbleScore'''
        if letter == '':
            return 0
        elif letter == scores[0][0]:
            return scores[0][1]
        else:
            return letterScore(letter, scores[1:])
                    
    def wordScore(S, scoreList):
        '''returns a string with its corresponding score'''
        if S == '':
            return 0
        else:
            return letterScore(S[0], scoreList) + wordScore(S[1:], scoreList)
    if dct == []:
        return []
                
    else:
        return [[dct[0], wordScore(dct[0], scores)]] + wordsWithScore(dct[1:], scores)


#print(wordsWithScore(["cats", "are", "cool"], scrabbleScores))
        

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 2
' For the sake of an exercise, we will implement a function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
' (Notice that you cannot assume anything about the length of the list.)
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def take(n, L):
    '''Returns the list L[0:n], assuming L is a list and n is at least 0.'''
    if n == 0:
        return []
    if L == []:
        return []
    else:
        return [L[0]] + take(n-1, L[1:])# your code goes here



'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 3
' Similar to problem 2, will implement another function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def drop(n, L):
    '''Returns the list L[n:], assuming L is a list and n is at least 0.'''
    if n == 0:
        return L
    if L == []:
        return []
    else:
        return drop(n-1, L[1:])# your code goes here


