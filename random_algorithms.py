# Write a function called isPrime() to confirm if a number is a prime number or not, returns true or false.
# Test with values from 1 to 10
def isPrime(num):
    myArr = []
    for i in range(2, num // 2 + 1):
        myArr.append(i)

    for val in myArr:
        if num % val == 0:
            return False

    return True

for i in range(1, 11):
    print(f'{i}: {isPrime(i)}')
