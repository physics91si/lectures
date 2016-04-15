
def find_primes(n):
    primes = []
    cdef int number = 2
    while len(primes) < n:
        if isPrime_upgraded(number,primes):
            primes.append(number)
        number += 1
    return primes

cdef isPrime_upgraded(int number,primes):
    cdef int i = 0
    for i in range(len(primes)):
        if number%primes[i] == 0:
            return False
    return True

#n = 10
#print find_primes(n)
