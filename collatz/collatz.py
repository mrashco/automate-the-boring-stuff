# https://automatetheboringstuff.com/chapter3/

# The Collatz Sequence

# Ask user input, ints only
# Print int until it equals 1
# Check input is even or odd
# If even, // 2 (I think that means to divide by itself)
# If odd, 3 x int + 1
# Once int equals 1, exit 

def main():
    # Ask user for number
    try: n = int(input('Enter number: ')) 
    # Invoke error message and quit if not
    except ValueError: exit('Must enter an integer') 
    
    # Continue until the number is equal to 1
    while n != 1: 
        # Run the function and assign to the number
        n = collatz(n) 
        print(n)

def collatz(n):
    # If even, use floor division (largest integer less than or equal to the number)
    if n % 2 == 0: n = n // 2 
    # Else i.e. odd, times by 3 and add 1
    else: n = 3 * n + 1 
    return n

main()

