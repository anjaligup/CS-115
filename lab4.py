#Anjali Gupta
#CS 115
# I pledge my honor that I have abided by the Stevens Honor System

def knapsack(capacity, itemList):
    '''this function takes an integer for its capacity and a list filled with items weight and their value. It will return the greatest weight that can be made with the items without going over the capacity'''
    if itemList == [] or capacity == 0:
        return [0,[]]
    elif itemList[0][0] > capacity:
        return knapsack(capacity, itemList[1:])
    else:
        use_it = knapsack(capacity-itemList[0][0], itemList[1:])
        print(use_it)
        lose_it = knapsack(capacity, itemList[1:])
        print(lose_it)
        use_it= [use_it[0]+itemList[0][1], [itemList[0]] + use_it[1]] 
    if use_it[0] > lose_it[0]:
        return use_it
    else:
        return lose_it
    

