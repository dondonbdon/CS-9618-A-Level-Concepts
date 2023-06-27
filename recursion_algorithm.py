import math
# The term Recursion can be defined as the process of defining something in terms of itself.
# In simple words, it is a process in which a function calls itself directly or indirectly.

# Create a method to find the factorial of a number iteratively
def iterative_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i

    return result


# Create a method to find the factorial of a number recursively
def recursive_factorial(n):
    if n <= 1:
        return n
    else:
        return n * recursive_factorial(n - 1)


def iterative_fibonacci(n):
    a, b = 0, 1

    for i in range(n):
        a, b = b, a + b

    return a


def recursive_fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)


def iterative_compound_interest(p, r, t):

    for i in range(t):
        p *= (1 + r)

    return p


def recursive_compound_interest(p, r, t):
    if t == 0:
        return p
    else:
        return recursive_compound_interest(p + p * r, r, t - 1)


# Print the 10 factorial iteratively and recursively in the form:
# iterative factorial <answer>
# recursive factorial <answer>
n = 10
print('iterative factorial', iterative_factorial(n))
print('recursive factorial', recursive_factorial(n))
print('iterative fibonacci', iterative_fibonacci(n))
print('recursive fibonacci', recursive_fibonacci(n))

p = 1_000
r = 0.01
t = 10
print('iterative compound interest', f'{(math.ceil(iterative_compound_interest(p, r, t))): }')
print('recursive compound interest', f'{(math.ceil(recursive_compound_interest(p, r, t))): }')


