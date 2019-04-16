#Write your function here

def middle_element(lst):
    if len(lst) % 2 == 1:
        index = (len(lst) - 1) / 2
        return lst[index]
    
    elif len(lst) % 2 == 0:
        average = lst[len(lst) / 2] 
        average += lst[len(lst) / 2 + 1] 
        average /= 2
        return average
                                        
print(middle_element([5, 2, -10, -4, 4, 5, 6]))