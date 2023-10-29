############################################################
# Name:Anjali Gupta
# Pledge:I pledge my honor that I have abided by the Stevens Honor System
# CS115 Lab 1
#
############################################################
from math import factorial
from functools import reduce
def inverse(x):
    '''this function returns the inverse value of a number n'''
    return 1/float(x)

def add(a, b):
    '''will add two integers a and b, will be called in e(n) function'''
    return a + b


def e(n):
    '''this function approximated e by adding up the first n terms of this sequence'''
    listA = list(map(factorial,range(n+1)))
    listB = list(map(inverse, listA))
    return reduce(add, listB)
    
    
    
