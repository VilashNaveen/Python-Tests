
def abbreviation(a, b):
    # Write your code here
    first = list(a)
    second = list(b)
    i1 = 0
    i2 = 0
    i = ""
    while i1 < len(first) and i2 < len(second):
        if first[i1] == second[i2]:
            i1 = i1 + 1
            i2 = i2 + 1

        elif first[i1].upper() == second[i2]  and first[i1].islower():
            first[i1] = first[i1].upper()
            i1 = i1 + 1
            i2 = i2 + 1
        elif first[i1].islower():
            first.pop(i1)
        else:
            return "NO"



    while i1 < len(first):
        if first[i1].islower():
            first.pop(i1)
        else:
            i1 = i1 + 1


    if first == second:
        i =  "YES"
    else:
        i = "NO"

    if i == "YES":
        return "YES"
    else:
        return "NO"



if __name__ == '__main__':
    print(abbreviation("abAAbacD","AAA"))