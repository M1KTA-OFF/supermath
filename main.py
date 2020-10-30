import random
import core

print("Math trainer (BETA)")
amount = int(input("Amount of cases:"))
operators = input("Operators, example(+-*/):")
difficulty = int(input("Difficulty:"))

core.start_custom_training(amount,operators,difficulty)


