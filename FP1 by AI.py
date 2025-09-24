import random
import time

# ANSI escape codes for colors
RED = '\033[91m'
RESET = '\033[0m'

# Get the user's name
varUserName = input("Hello! What's your name? ")

# Greet the user
print(f"Nice to meet you, {varUserName}! Let's generate some lucky numbers for you.")

# Generate random numbers
num1 = random.randint(1, 69)
num2 = random.randint(1, 69)
num3 = random.randint(1, 69)
num4 = random.randint(1, 69)
num5 = random.randint(1, 69)
num6 = random.randint(1, 26)

# Print the numbers with a delay and color the last one
print(f"\nYour lucky numbers are:")

# Print numbers 1 through 5 with a delay
for num in [num1, num2, num3, num4, num5]:
    print(f"{num}  ", end='', flush=True)
    time.sleep(0.25)

# Print the last number in red with the specified spacing
print(f"  {RED}{num6}{RESET}")

# Farewell message
print("\nGood luck! Hope these numbers bring you some good fortune!")