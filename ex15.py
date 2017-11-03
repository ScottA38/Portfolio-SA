def fib(n):
    #test if integer argument input into function is equal to 0 -
    if n == 0:
        # this is the 1st of 2 base cases where the function will not return another fucntion call
        return 0

    #test if integer argument input into function is equal to 0.
    if n == 1:
        #2nd base case with real return value (not returning another function)
        return 1
    else:
        return fib(n-1) + fib(n-2)

#iterate through all terms up to 20 (21 iterations)
for i in range(20):
    #print output of fib() where int argument is the iteration number
    print fib(i)
