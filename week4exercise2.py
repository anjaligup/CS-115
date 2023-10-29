
def mySum(l):
    '''returns sum of a given list'''
    if l == []:
        return 0
    else:
        return l[0] + mySum(l[1:])

    
print (mySum([1, 2, 3, 4]))

def reverseString(string):
    '''returns the reverse of a string'''
    if string == "":
        return ""
    else:
        #return reverseString(string[1:]) + string[0]
        return string[-1] + reverseString(string[:-1])

print(reverseString("start"))

M = ['what', 'does', 'map', 'really']
L = 2*['do'] + M
print(L)
N = [ 'map', L[3], M[2] ]  


