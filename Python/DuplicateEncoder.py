def duplicate_encode(word):
    l = list(word.lower())
    s = ""
    for i in l:
        if(l.count(i) > 1): s = s + ")"
        else: s = s + "("       
    return s
