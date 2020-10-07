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
            bkwd_x=int(str(x)[::-1])

            if bkwd_x!=x:
                for m in range(2, bkwd_x):
                    if bkwd_x % m == 0:
                        bkwdprime = False
                        break
                if bkwdprime:
                    lst.append(x)

    return lst

