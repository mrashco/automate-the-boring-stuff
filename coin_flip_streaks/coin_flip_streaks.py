# Coin Flip Streaks - Track streaks of six heads or tails in random coin tosses

# Enter number of flips
# Toss a coin per number of flips
# Track result
# Store result in a list
# Check list for a streak
#   If current toss is equal to the previous toss, add +1 streak
#   If streak equals six, add +1 streaks
# Output streak

from random import randint

def main(): print('Streaks: ' + str(flip(input('Number of flips: ')))) # Prints output to terminal

def flip(number):
    coin_list = [] # Create empty list to store coin tosses
    for i in range(int(number)): # Loop thourgh number provided by user
        coin = randint(0,1) # Each loop give random 0 or 1
        coin_list.append(coin) # Add random 0 or 1 to list
    return streak(coin_list) # Pass list through streak function

def streak(l):
    streaks, streak = 0, 0 # Create counters for a single streak, and the overal amount of streaks
    # Loop through the list of coin tosses
    for i in range(1, len(l)):
        if l[i] == l[i-1]: # Check if the current toss is equal to the last toss
            streak += 1 # If so, count up on the streak
        else: streak = 0 # Otherwise, set the streak back
        if streak == 6: # Now check for a total of six in a row
            streaks += 1 # Add to the overal amount of streaks
            streak = 0 # Reset the streak counter back to nothing
    return streaks

if __name__ == '__main__': main()

# Credits
# https://www.reddit.com/r/learnpython/comments/6m8o4d/if_i_have_a_list_of_numbers_how_do_i_get_the/