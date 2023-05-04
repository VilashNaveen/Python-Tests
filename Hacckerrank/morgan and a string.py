import unittest

def morganAndString(a, b):
   first = list(a)
   second = list(b)
   i = 0
   j = 0
   string_out = ""
   while i < len(a) and j < len(b):
       if ord(first[i]) > ord(second[j]):
           string_out = string_out + second[j]
           j = j + 1
       else:
           string_out = string_out + first[i]
           i = i + 1
   while i < len(a):
       string_out = string_out + first[i]
       i = i + 1
   while j < len(b):
       string_out += second[j]
       j += 1

   return string_out


if __name__ == '__main__':
    l = morganAndString("ABACABA","ABACABA")
    print(l)
