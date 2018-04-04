# Find the sum of even-valued fibonacci numbers whose values don't 
# exceed four million.

def compute():
    a = 1
    b = 1
    the_sum = 0
    while (a < 4000001):
        if (a % 2 == 0):
            the_sum += a
        a, b = b, a + b

    return str(the_sum)

print(compute())