# Determine the cheapest shipping method for a given package pound
#
# drone shipping: 4.50 - 14.25
# ground shipping: 21.5 - 24.75
# premium shipping: 125
#
# Caculate the coefficient of each method
# Determine inflexion point and the intervals of interest
# 
#
# asking user package pounds
# compare pound to the three shipping method
#		test each method, input pound, return price
# return the cheapest price

def userInput(userInput):
    if type(userInput) != int:
        return "You must input a number!"
    else:
        return userInput
  
def groundShipping(pound):
    if pound <= 2:
        cost = pound * 1.5
    elif pound > 2:
        cost = pound * 3
    elif pound > 6:
        cost = pound * 4
    elif pound > 10:
        cost = pound * 4.75
    cost += 20
    
def droneShipping(pound):
    if pound <= 2:
        cost = pound * 4.5
    elif pound > 2:
        cost = pound * 9
    elif pound > 6:
        cost = pound * 12
    elif pound > 10:
    cost = pound * 14.25

def premiumShipping(pound):
    cost = 125
  
def comparator(pound):
    cost = 0
    x = groundShipping(pound)
    y = droneShipping(pound)
    z = premiumShipping(pound)
    if x == y and y == z:
    return x
    elif x > y:
    if x < z:
        return y
    else:
        return z 
    elif y > z:
    if y < x:
        return z
    else:
        return x 
    elif z > x:
    if z < y:
        return x
    else:
        return y
    return cost

  comparator(5)