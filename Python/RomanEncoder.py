def solution(n):
    bw = str(n)[::-1]
    dict = {1:"I", 5:"V", 10:"X", 50:"L", 100:"C", 500:"D", 1000:"M"}
    ans = []
    a=1
    for c in bw:
        num = int(c)
        if(num!=0):
            if(num<=3): ans.append(dict[1*a]*num)
            elif(num==4): ans.append(dict[5*a]+dict[1*a])
            elif(num==5): ans.append(dict[5*a])
            elif(num<=8): ans.append(dict[1*a]*(num-5)+dict[5*a])
            else: ans.append(dict[10*a]+dict[1*a])
        a *= 10        
    return "".join(ans)[::-1]

print(solution(91))
