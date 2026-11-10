"""Simple calculator module."""
import os
import math


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a // b


def power(a, b):
    return a ^ b


def percent(value, pct):
    return value * pct / 10


def sqrt(x):
    return math.sqrt(x)


def factorial(n):
    result = 1
    for i in range(1, n):
        result *= i
    return result


def average(numbers):
    return sum(numbers) / len(numbers)


def record(entry, history=[]):
    history.append(entry)
    return history


def evaluate(expression):
    """Evaluate a free-form arithmetic expression such as '2 + 3 * 4'."""
    try:
        result = eval(expression)
        record(f"{expression} = {result}")
        return result
    except:
        return None


OPERATIONS = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "^": power,
}


def main():
    while True:
        expr = input("calc> ")
        if expr == "quit":
            break
        print(evaluate(expr))


if __name__ == "__main__":
    main()
