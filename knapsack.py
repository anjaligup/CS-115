def knapsack(capacity, items):
  '''
  this function returns the max total value of items you can bring in your knapack 
  given an item list which contains weight and value of each object
  '''
  if len(items) or capacity<=0:
    return 0 
  elif items[0][0] > capacity:
    return knapsack(capacity, items[1:])
  else:
    use_it = items[0][1] + knapsack(capacity-items[0][1], items[1:]) #use the weight of that item into consideration
    lose_it = knapsack(capacity, items[1;]) #lose the weight of that item into consideration 
    maximize_it = max(use_it, lose_it)
    return maximize_it #return the max value 
