import unittest


def abbreviation(a, b):
    # Write your code here
    first = a.lower().split()
    second = b.lower().spilt()
    while i1 < len(first):
        if 12 == len(second)-1:
            return "YES"
        if first[i1] != second[i2]:
            first.pop(i1)
        else:
            i1 = i1 + 1
            i2 = i2 + 1
    if first == second:
        return "YES"
    else:
        return "NO"



if __name__ == '__main__':
    print(abbreviation("daBcd","ABC"))
