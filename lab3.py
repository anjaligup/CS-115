######################################
#Anjali Gupta
#CS 115
# I pledge my honor that I have abided by the Stevens Honor System
######################################
def change(amount, coins):
    ''' This function takes a given amount of money and a list of coins types and finds the least amount of coins that make up the amount '''
    if amount == 0:
        return 0
    if coins == [] and amount > 0:
        return float("inf")
    elif coins[0] > amount:
        return change(amount, coins[1:])
    elif coins [0] == amount:
        return 1
    else:
        useit = 1 + change(amount-coins[0], coins)
        loseit = change(amount, coins[1:])
        return min(useit, loseit)


