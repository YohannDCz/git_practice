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
    cost = 0
    if pound <= 2:
        cost = pound * 1.5
    elif pound <= 6:
        cost = pound * 3
    elif pound <= 10:
        cost = pound * 4
    elif pound > 10:
        cost = pound * 4.75
    cost += 20
    return cost


def droneShipping(pound):
    cost = 0
    if pound <= 2:
        cost = pound * 4.5
    elif pound <= 6:
        cost = pound * 9
    elif pound <= 10:
        cost = pound * 12
    elif pound > 10:
        cost = pound * 14.25
    return cost

def premiumShipping(pound):
    cost = 125
    return cost

def comparator(pound):
    groundShippingg = groundShipping(pound)
    droneShippingg = droneShipping(pound)
    premiumShippingg = premiumShipping(pound)
    if groundShippingg == droneShippingg and droneShippingg == premiumShippingg:
        return "You should use groundShipping. It will cost $" +str(groundShipping(pound))+ "." 
    elif groundShippingg > premiumShippingg and droneShippingg > premiumShippingg: 
        return "You should use premium shipping. It will cost $" +str(premiumShipping(pound))+ "."
    elif groundShippingg > droneShippingg and premiumShippingg > droneShippingg:
        return "You should use drone shipping. It will cost $" +str(droneShippingg(pound))+ "."
    elif premiumShippingg > groundShippingg and droneShippingg > groundShippingg:
        return "You should use ground shipping. It will cost $" +str(groundShipping(pound))+ "."

print(groundShipping(6))
print(comparator(5))