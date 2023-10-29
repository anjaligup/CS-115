def fib(n, a = 0, b = 1):
    if n == 0:
        return a
    if n == 1:
        return b
    else:
        return fib(n-1, b, a+b) #a gets assigned the value of b and then b gets assigned the value of a+b

print(fib(7))

def isPalindrome(word): #word can be read backwards and forwards the same way ex) madam, racecar
    if len(word) == 0 or len(word) == 1:
        return True
    if word[0] == word[-1]:
        return isPalindrome(word[1:-1])
    else:
        return False

    
