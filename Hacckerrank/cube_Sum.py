import unittest


def cubeSum(n, operations):
    cube = [[[0 for k in range(n)] for j in range(n)] for i in range(n)]
    arr = []
    for i in operations:
        op = i.split()
        op =list(map(eval,op))
        if op[0] == "UPDATE":
            cube[(op[1]) - 1][(op[2]) - 1][(op[3]) - 1] = (op[4])
        else:
            sum = 0
            for i in range((op[1]) - 1, (op[4])):
                for j in range((op[2]) - 1, (op[5])):
                    for k in range((op[3]) - 1, (op[6])):
                        sum += cube[i][j][k]
            arr.append(sum)

    return arr




if __name__ == '__main__':

