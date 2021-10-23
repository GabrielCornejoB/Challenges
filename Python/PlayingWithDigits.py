def dig_pow(n, p):
    sum = 0
    for i in str(n):
        sum += pow(int(i), p)
        p += 1
    ans = sum/n
    return int(ans) if ans.is_integer() else -1
