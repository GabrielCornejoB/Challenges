def to_jaden_case(string):
    list = string.split(' ')
    list2 = []
    for s in list:
        list2.append(s.capitalize())
    return(' '.join(list2))  

print(to_jaden_case("el mono baila"))