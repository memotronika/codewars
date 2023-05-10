# Multiply
def multiply(a, b):
    return a * b

# Counting sheep...
def count_sheeps(sheep):
    number=0
    for every in sheep:
        if every:
            number+=1
    return number

# Gravity Flip
def flip(d, a):
    a.sort()
    if d=='L':
        a.reverse()
    return a

# Basic Mathematical Operations
def basic_op(operator, value1, value2):
    if operator is '+':
        return value1 + value2
    if operator is '-':
        return value1 - value2
    if operator is '/':
        return value1 / value2
    if operator is '*':
        return value1 * value2

# Is it a palindrome?
def is_palindrome(s):
    return s.lower()==''.join(reversed(s)).lower()

# Even or Odd
def even_or_odd(number):
    return 'Even' if number%2==0 else "Odd"

# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
