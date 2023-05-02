import unittest

def count_substring(string, sub_string):
    num = 0
    i = 0
    while True:
        loc = string.find(sub_string,i)
        if loc == -1:
            break
        else:
            num = num + 1
        i = loc + 1
    return num

if __name__ == '__main__':
    num = count_substring("ABCDCDC","CDC")
    print(num)
