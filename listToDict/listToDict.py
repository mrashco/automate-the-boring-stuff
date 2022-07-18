def main():
    inv = {'gold coin': 42, 'rope': 1}
    dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    addToInventory(inv, dragonLoot)

def addToInventory(inv, addedItems):
    # Go through each item to be added
    for listItem in addedItems:
        # If the item is already in the inventory, index in and increase amount
        if listItem in inv: inv[listItem] += 1
        # If the item is not in the inventory, add item to dict and increase amount
        else: inv[listItem] = 1
    displayInventory(inv)

def displayInventory(inv):
    itemsTotal = 0
    for dictItem in inv:
        print(inv[dictItem], dictItem)
        itemsTotal += inv[dictItem]
    print('Total number of items: ', itemsTotal)
    
if __name__ == '__main__': main()