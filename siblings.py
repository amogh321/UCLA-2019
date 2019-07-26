siblings = int(input("How many siblings do you have"))
lst = []
if siblings == 0:
    print("Nice to know you")
else:
    i = 0
    while i < siblings:
        siblings_age = int(input("Type in your siblings ages"))
        lst.append(siblings_age)
        i = i + 1
    oldest = lst[0]
    youngest = lst[0]
    for x in lst:
        if youngest > x:
            youngest = x
        if oldest < x:
            oldest = x
    print("Your oldest sibling is", oldest, "years old")
    print("Your youngest sibling is", youngest, "years old")
    
            
    

