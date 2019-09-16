'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

'''

import math
import time
start_time = time.time()
def isPrime(n):
    if(n==1 | n%2==0):
        return False
    
    for i in range(3, int(math.sqrt(n)+1), 2):
        if(n%i == 0):
            return False

    return True

n = 2000000
i = 3
s = 2

while i<n:
    if(isPrime(i)):
        s+=i
    i+=2

print(s)

print("---- %s s ----" % (time.time() - start_time))
