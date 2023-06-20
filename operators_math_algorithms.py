# Here in this seciton i will tell you about the math library for python and its usefulness.
# The first step is to import python's inbuilt math library
# (This is probably the only thing you may ever need to import in python)
# The syntax for importing the library is to do the following.
import math

# Now that the math library has been imported. You can use its various useful functions in your prgrams
# To access to functions you do the following syntax math.<function>
# It has some useful functions that will round up a number to its ceiling or to its floor such as:
temp = 42.5
tempFloor = math.floor(temp)
tempCeil = math.ceil(temp)
print('Floor', tempFloor)
print('Ceil', tempCeil)

# Another useful function is the pow() function which performs the same action as the ** operator but in
# The form of a function that takes parameter x(value) and parameter y(power):
x = 2
y = 8
result = math.pow(x, y)
print('Math - Pow:', result)

# Math has other useful functions that may come in handy such as the ability to perform pythagorian calcuations
# Use these where you see fit

# Here in this section i will tell you about various operators that you might see yourself
# Using in your programs

# The + operator
# You use it to add two different values like
add1 = 69
add2 = 68
add = add1 + add2
print('add: ', add)


# The - operator
# You use it to subtract two different values
sub1 = 69
sub2 = 68
sub = sub1 - sub2
print('sub: ', sub)


# The + operator
# You use it to multiply two different values
mult1 = 4
mult2 = 8
mult = mult1 * mult2
print('multiplication: ', mult)


# The ** operator
# You use it to divide two different values
pow1 = 10
pow2 = 3
pow = pow1 ** pow2
print('pow: ', int(pow))


# The / operator
# You use it to divide two different values
division1 = 20
division2 = 5
division = division1 / division2
print('division: ', int(division))


# The // operator
# You use it to divide two different values and only return the whole number part of the result
div1 = 13
div2 = 6
div = div1 // div2
print('div: ', div)


# The % operator
# You use it to divide two different values and only return the modulus/remainder part of the result
mod1 = 13
mod2 = 6
mod = mod1 % mod2
print('mod: ', int(mod))
