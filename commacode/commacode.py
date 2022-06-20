# Comma Code
# Takes list value e.g. ['apples', 'bananas', 'tofu', 'cats']
# Return items as string e.g. 'apples, bananas, tofu, and cats'

def main(): print(makestring(['apples', 'bananas', 'tofu', 'cats']))

def makestring(l):
    # Define blank new string
    s = ''
    # Print out each item in the list as a new string, except the last item
    for i in l[:-1]: s += f'{i}, '
    # Print out last item with 'and '
    s += f'and {l[-1]}'
    return s

if __name__ == '__main__': main()