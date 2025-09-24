import random

varUserName = input("Hello! What's your name? ")

print(f"Nice to meet you, {varUserName}! Let's generate some lucky numbers for you.")

#generate powerball numbers
num1 = random.randint(1, 69)
num2 = random.randint(1, 69)
num3 = random.randint(1, 69)
num4 = random.randint(1, 69)
num5 = random.randint(1, 69)
num6 = random.randint(1, 26)

print(f"\nYour lucky numbers are:")
print(f"{num1}  {num2}  {num3}  {num4}  {num5}    {num6}")

print("\nGood luck! Hope these numbers bring you some good fortune!")