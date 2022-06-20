# Coin Flip Streaks - Track streaks of six heads or tails in random coin tosses

# Enter number of flips
# Toss a coin per number of flips
# Track result
# Store result in a list
# Check list for a streak
# Output streak

from random import randint

def main(): print(flip(input('Number of flips: ')))

def flip(number):
    coin_list = []
    for i in range(int(number)):
        coin = randint(0,1)
        coin_list.append(coin)
    return coin_list

if __name__ == '__main__': main()