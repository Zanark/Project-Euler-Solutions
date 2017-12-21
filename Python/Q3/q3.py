'''
# Problem 3 

### Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.

**What is the largest prime factor of the number 600851475143 ?**
'''

#PROGRAM:

from math import sqrt

prime_list = []

def prime_factor(n):
    
    for j in range(2, int(sqrt(n))):
        if n % j == 0:
            while(n % j == 0):
                n /= j
            prime_list.append(j)
    print (max(prime_list))


prime_factor(600851475143)

