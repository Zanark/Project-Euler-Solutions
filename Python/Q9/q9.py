'''

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

'''

n = 1000
p = 1

for a in range(3, (n//3)+1):
    b = (n**2 - 2*a*n)//(2*n - 2*a)
    c = n - b - a
    if a**2 + b**2 == c**2:
        p = a*b*c

print(p)
