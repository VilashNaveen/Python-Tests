def printPicnic(itemsDict,leftWidth,rightWidth):
    print('PICNIC ITEMS'.center(leftWidth+rightWidth,'-'))
    for k,v in itemsDict.items():
        print(k.ljust(leftWidth,'.')+str(v).rjust(leftWidth))

picnicItems = {'sandwiches':4,'apples':30,'cups':4,'cookies':8000}
printPicnic(picnicItems,12,5)
printPicnic(picnicItems,20,6)