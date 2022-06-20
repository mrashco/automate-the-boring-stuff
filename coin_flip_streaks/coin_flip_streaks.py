# Coin Flip Streaks - Track streaks of six heads or tails in random coin tosses

# Enter number of flips
# Toss a coin per number of flips
# Track result
# Store result in a list
# Check list for a streak
#   If current toss is the same six times in a row, add that to list of streaks
# Output streak

from random import randint

def main(): print(flip(input('Number of flips: ')))

def flip(number):
    coin_list = []
    for i in range(int(number)):
        coin = randint(0,1)
        coin_list.append(coin)
    return streak(coin_list)

def streak(l):
    streak_total = 0
    for i in l:
        if l[i] == l[i]

if __name__ == '__main__': main()

# Credits

# https://www.reddit.com/r/learnpython/comments/6m8o4d/if_i_have_a_list_of_numbers_how_do_i_get_the/