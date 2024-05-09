import random

def get_numbers_ticket(min, max, quantity):
    # Check if the input parameters are within valid ranges
    if min < 1 or max > 1000 or quantity > (max - min + 1):
        return []  # Return an empty list if parameters are invalid
    
    # Generate 'quantity' unique random numbers within the specified range
    random_numbers = random.sample(range(min, max + 1), quantity)

    # Sort the generated numbers in ascending order
    random_numbers.sort()

    # Return the sorted list of random numbers
    return random_numbers

# Generate a lottery ticket with 6 random numbers between 1 and 49
lottery_numbers = get_numbers_ticket(1, 49, 6)

# Print the generated lottery numbers
print("Ваші лотерейні числа:", lottery_numbers) 