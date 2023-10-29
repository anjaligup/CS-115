#Anjali Gupta
#CS 115
#I pledge my honor that I have abided by the Stevens Honor System [AG]


def helper_function(L):
    '''creates a new list of sums of adjacent terms in the original list'''
    if len(L) == 1:
        return []
    else:
        return [L[0] + L[1]] + helper_function(L[1:])


def pascal_row(n):
    '''outputs a list of elements found in a certain row of Pascal's triangle'''
    if n == 0:
        return [1]
    else:
        return [1] + helper_function(pascal_row(n-1)) + [1]


def pascal_triangle(n):
    '''outputs a list of lists containing values of all the rows up to and including row n'''
    if n == 0:
        return [[1]]
    else:
        last_pascal_row = pascal_row(n)
        return pascal_triangle(n-1) + [last_pascal_row] 


def test_pascal_row():
    '''uses assert statements to test pascal_row'''
    assert pascal_row(0) == [1]
    assert pascal_row(1) == [1, 1]
    assert pascal_row(3) == [1, 3, 3, 1]
    assert pascal_row(5) == [1, 5, 10, 10, 5, 1]


def test_pascal_triangle():
    '''uses assert statements to test pascal_triangle'''
    assert pascal_triangle(1) == [[1], [1, 1]]
    assert pascal_triangle(2) == [[1], [1, 1], [1, 2, 1]]
    assert pascal_triangle(4) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    assert pascal_triangle(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
    
