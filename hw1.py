########################
# Anjali Gupta
# CS 115
# I pledge my honor that I have abided by the Stevens Honor System
########################
from functools import reduce

def mult(x,y):
    '''this function will multiply values together'''
    return x * y 

def factorial(n):
    '''this function will return the factorial of a given number n'''
    return reduce(mult, range(1, n+1))

def add(x, y):
    '''this function will add values together'''
    return x + y

def mean(L):
    '''this function will return the mean of a given list'''
    a1 = reduce(add, L)
    a2 = a1 / (len(L))
    return a2 
            
