def find_outlier(integers):
    odd = False
    count = 0
    for i in range(3):
        if(integers[i]%2 != 0): count+=1
    if count >= 2: odd = True 
    for i in integers:
        if((i%2 == 0 and odd) or (i%2 != 0 and not odd)): return i
    

print(find_outlier([2, 4, 6, 8, 10, 3]))