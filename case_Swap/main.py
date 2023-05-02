# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def swap_case(s):
    output = ""
    for i in s:
        if i.isalpha:
            output = output + i.swapcase()
        else:
            output = output + i
    return output

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = "Asga rd"
    print(swap_case(s))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
