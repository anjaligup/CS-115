
try:
    x = 23
    print(list(map(lambda y : y+1, x)))
except ZeroDivisionError:
    print('This is an IO error')
except TypeError:
    print('This is a Type Error')
else:
    print('Hello')
finally:
    print('Finally')
print('Done Here')


try:
    n = 5
    d = 5
    print(n/d)
except ValueError:
    print('This is a value error')
except ZeroDivisionError:
    print('This is a zerodivisionerror')
else:
    print('we are all good to go')
finally:
    print('Done deal!')
print("Done done deal!")


#Example 3: Some exception examples
a = int('rest') # ValueError
x = 23
map(lambda y: y+1, x) #Type Error 
l = [1,2,3] 
print(l[5]) # Index Error
dic = {'5':'here', '6':'there'}
print(dic['8']) #Key Error



