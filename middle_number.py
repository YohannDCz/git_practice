#Write your function here
def middle_element(lst):
    if len(lst) % 2 == 1:
        return lst[len(lst) / 2]
    elif len(lst) % 2 == 0:
        average = lst[len(lst) / 2] 
        average += lst[len(lst) / 2 + 1] 
        average /= 2
        return average
                                        
#Uncomment the line below when your function is done
print(middle_element([5, 2, -10, -4, 4, 5]))
