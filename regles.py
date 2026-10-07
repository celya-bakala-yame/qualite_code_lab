#tTYPAGE 

#❌
def somme(a, b):
    return a + b

#✅

def somme(a: int | float, b: int | float) -> float:
    a, b = float(a), float(b)
    return a + b

#Self explanatory code

#❌
def ca(w, h):
    return w * h

#✅

def calculate_rectangle_area(width: float, height: float) -> float:
    return width * height

# Docstrings 

#❌

def multiply(a, b):
    return a * b

#✅

def multiply(a: float, b: float) -> float:
    """
    Multiplies two numbers.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The product of the two numbers.
    """
    return a * b

#Multi lignes : 

#❌

def calcTotal(price,taxRate=0.05): return price*(1+taxRate)

#✅

def calculate_price_with_taxes(
    base_price: float,
    tax_rate: float = 0.05
    ) -> float:
    return base_price * (1 + tax_rate)

#Responsabilité unique

#❌
def process(numbers):
    cleaned = [number for number in numbers if number >= 0]
    return sum(cleaned)

#✅
def clean_data(numbers: list[int]) -> list[int]:
    return [number for number in numbers if number >= 0]

def calculate_total(numbers: list[int]) -> int:
    return sum(numbers)

#Gestion des exceptions

#❌
def divide_numbers(a, b):
    return a / b

#✅
def divide_numbers(a: float, b: float) -> float | None:
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: can't divide by zero")
        
#Tests intégrés

#❌
def greet(name):
    print(f"Hello, {name}!")
    
#✅
def greet(name: str) -> str:
    return f"Hello, {name}!"

def test_greet():
    assert greet("Alice") == "Hello, Alice!"
    
#algorithmique 

#❌

from time import perf_counter

def fibonacci_of(n):
    if n in {0, 1}:
        return n
    return fibonacci_of(n - 1) + fibonacci_of(n - 2)

start = perf_counter()
[fibonacci_of(n) for n in range(35)]  # Generate 35 Fibonacci numbers
end = perf_counter()

print(f"Execution time: {end - start:.2f} seconds")

#✅
from time import perf_counter

cache = {0: 0, 1: 1}

def fibonacci_of(n):
    if n in cache:
        return cache[n]
    cache[n] = fibonacci_of(n - 1) + fibonacci_of(n - 2)
    return cache[n]

start = perf_counter()
[fibonacci_of(n) for n in range(35)]  # Generate 35 Fibonacci numbers
end = perf_counter()

print(f"Execution time: {end - start:.2f} seconds")

#Variables inutiles

#❌

def sum_even_numbers(numbers):
    even_numbers = [number for number in numbers if number % 2 == 0]
    return sum(even_numbers)

#✅

def sum_even_numbers(numbers):
    return sum(number for number in numbers if number % 2 == 0)