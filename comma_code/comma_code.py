# Comma Code
# Takes list value e.g. ['apples', 'bananas', 'tofu', 'cats']
# Return items as string e.g. 'apples, bananas, tofu, and cats'

def main(): print(makestring(['apples', 'bananas', 'tofu', 'cats']))

def makestring(l):
    s = '' # Define blank new string
    for i in l[:-1]: s += f'{i}, ' # Print out each item in the list as a new string, except the last item
    s += f'and {l[-1]}' # Print out last item with 'and '
    return s

if __name__ == '__main__': main()