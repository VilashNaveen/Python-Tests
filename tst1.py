# fantasy game inventory manager
stuff = {'rope':'1','torch':'6','gold':'42','dagger':'1','arrow':'12'}
loot = ['gold','dagger','gold','gold','ruby']

def displayInventory(inventory):
    l=0
    for i in inventory:
        print('{0} {1}'.format(str(i), str(inventory[i])))
        l=l+int(inventory[i])
    print('total items '+str(l))

def addToInventory(inventory,loot):
    for i in loot:
        if i in inventory:
            inventory[i]=int(inventory[i])+1
        else:
            inventory[i]=1

addToInventory(stuff,loot)
displayInventory(stuff)

