# fantasyGameInventory

# Data structure for game inventory
# Keys = items names/description
# Value = number of items in int

def main(): displayInventory({'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12})

def displayInventory(inventory):
    items_total = 0
    for item in inventory:
        print(inventory[item], item)
        items_total += inventory[item]
    print('Total number of items: ', items_total)

if __name__ == '__main__': main()