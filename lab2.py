########################################
#Name: Anjali Gupta
#CS 115
# I pledge my honor that I have abided by the Stevens Honor System
########################################
def length(L):
    '''Returns the length of a given list'''
    if L == []:
        return 0
    else:
        return 1 + length(L[1:])


def dot(L, K):
    '''This function computes the dot product of an input of two lists'''
    if L == [] and K == []:
        return 0.0
    else:
        return L[0]*K[0] + dot(L[1:],K[1:])


def explode(S):
    '''This function takes a string and returns a list of the characters'''
    if S == "":
        return []
    else:
        return list(S[0]) + list(explode(S[1:]))


def ind(e, L):
    '''This function returns the the index at which an element e is found in a list. If e is not in the list, the function will return an integer that equals the length of the list '''
    if L == [] or L == "":
        return 0
    if e == L[0]:
        return 0
    else:
        return 1 + ind(e, L[1:])
    

def removeAll(e, L):
    '''This function will return a list identical to L but all elements identical to e will be removed '''
    if L == []:
        return []
    elif e == L[0]:
        return removeAll(e, L[1:])
    else:
        return [L[0]] + removeAll(e, L[1:])
    
  
def myFilter(f, L):
    '''This function takes two inputs and returns a new list that contains all the elements in list L for which the function f evaluates to True'''
    if L == []:
        return []
    elif f(L[0]) == True:
        return [L[0]] + myFilter(f, L[1:])
    else:
        return myFilter(f, L[1:])
    
'''
def deepReverse(L):
    if L == []:
        return []
    if isinstance(x, list):
        return deepReverse(list) + deepReverse(L[0:])
    else:

'''
    

