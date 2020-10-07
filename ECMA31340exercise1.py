
#Find all Backwards Read Primes between two positive given numbers (both inclusive), the second one always being greater than or equal to the first one.
# The resulting array or the resulting string will be ordered following the natural order of the prime numbers.

def backwardsPrime(lb, ub):
    lst=[]

    for x in range(lb, ub+1):
        bkwdprime=True

        #determine whether x is a prime number

        for y in range(2, x):
            if x%y==0:
                bkwdprime=False
                break

        #if x is a prime number, determine whether the backward of x is not equal to x, if no, determine whether it is a prime number
        if bkwdprime:
            digits = len(str(x))
            bkwd_x = 0
            for i in range(0, digits):
                bkwd_x = bkwd_x + int(str(x)[i]) * 10 ** i

            if bkwd_x!=x:
                for m in range(2, bkwd_x):
                    if bkwd_x % m == 0:
                        bkwdprime = False
                        break

            else:
                bkwdprime=False

        if bkwdprime:
            lst.append(x)


    return lst

#test function

prime=backwardsPrime(9900,10000)

print(prime)