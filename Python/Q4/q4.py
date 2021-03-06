'''
# Problem 4 

### Largest palindrome product

A palindromic number reads the same both ways. The largest palindrome made from the product of 
two 2-digit numbers is 9009 = 91 × 99.

**Find the largest palindrome made from the product of two 3-digit numbers.**
'''
#PROGRAM:


lpal = []

for i in range(1,1000):
    for j in range(1,1000):
        pal = str(i*j)

        if pal == pal[::-1]:
            lpal.append(int(pal))


print(max(lpal))
#print(lpal)