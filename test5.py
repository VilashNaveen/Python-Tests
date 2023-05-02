tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

dLen=[]
for x in range(0,3):
    a=0
    for y in range(0,4):
        if a<len(tableData[x][y]):
            a=len(tableData[x][y])
            dLen.append(a)
for i in range(0,4):
    for z in range(0,3):
        print(tableData[z][i].ljust(dLen[z])+'/')
        print('/n')
