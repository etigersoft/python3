# Input
# 10000
# Expected
# 1229


import timeit

# Version 1
# def countPrimes(n):
#     if n < 3: 
#         return 0        ###// No prime number less than 2
    
#     lst = [1] * n       ###// create a list for marking numbers less than n
#     lst[0] = lst[1] = 0 ###// 0 and 1 are not prime numbers
#     m = 2
    
#     while m * m < n:       ###// we only check a number (m) if its square is less than n
        
#         if lst[m] == 1:    ###// if m is already marked by 0, no need to check its multiples.
#             ###// If m is marked by 1, we mark all its multiples from m * m to n by 0. 
#             ###// 1 + (n - m * m - 1) // m is equal to the number of multiples of m from m * m to n
#             lst[m * m: n: m] = [0] *(1 + (n - m * m - 1) // m)
            
#         ###// If it is the first iteration (e.g. m = 2), add 1 to m (e.g. m = m + 1; 
#         ### // which means m will be 3 in the next iteration), 
#         ###// otherwise: (m = m + 2); This way we avoid checking even numbers again.	
#         m += 1 if m == 2 else 2
    
#     return sum(lst)


# algorithm Sieve of Eratosthenes is
#     input: an integer n > 1.
#     output: all prime numbers from 2 through n.

#     let A be an array of Boolean values, indexed by integers 2 to n,
#     initially all set to true.
    
#     for i = 2, 3, 4, ..., not exceeding √n do
#         if A[i] is true
#             for j = i2, i2+i, i2+2i, i2+3i, ..., not exceeding n do
#                 A[j] := false

#     return all i such that A[i] is true.

# Version 2 - This one is slow because of the extra For 
def countPrimes(n):
    if n < 3:
        return 0

    prime = [True for i in range(n)]
    prime[0] = prime[1] = 0
    p = 2
    
    while (p * p < n):
         
        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):         
            # Update all multiples of p
            # prime[m * m: n: m] = [0] *(1 + (n - m * m - 1) // m) ## This will improve the time dramatically
            for i in range(p ** 2, n, p):
                prime[i] = 0
        
        p += 1
    
    # Print all prime numbers
    # for p in range(n):
    #     if prime[p]:
    #         print (p,end=' ')
    return sum(prime)

#timeit.timeit(print(countPrimes(10))) # TODO: Test speed
print(countPrimes(25))