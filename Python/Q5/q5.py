'''
# Problem 5

### Smallest multiple

2520 is the smallest number that can be divided by each of the \
numbers from 1 to 10 without any remainder.

**What is the smallest positive number that is evenly divisible \
by all of the numbers from 1 to 20?**
'''
# PROGRAM:

flag = 0
m = 1 
for i in range(1,21):
    m *= i

for i in range(2520,int(m+1)):
    for j in range(11, 21):
        if i % j == 0:
            flag += 1
            continue
            print("checking for number %d") % i
        else:
            flag = 0
            break
            print("Number %d didn't pass the test") % (i)

    if flag > 0:
        print(i)
        break

'''
 This is the only solution that I could come up with at the moment 
 It takes around 3 minutes to run and display the output

 I would be happy if someone helped me to make it better and also explain me how it works
 becaus eit's no use if I myself can't understand it.