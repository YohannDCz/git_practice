#Write your function here
def remove_middle(lst, start, end):
    if start == 0:
         lst = lst + lst[0] + lst[end:]
    if end == len(lst) - 1:
        lst = lst + lst[:start] + lst[-1]
        lst = lst[:start] + lst[end:]
    return lst

#Uncomment the line below when your function is done
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))