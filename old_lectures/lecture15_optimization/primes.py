
def find_primes(n):
    primes = []
    number = 2
    while len(primes) < n:
        if isPrime_upgraded(number,primes):
            primes.append(number)
        number += 1
    return primes

def isPrime(number):
    for i in xrange(2,number):
        if number%i == 0:
            return False
    return True

def isPrime_upgraded(number,primes):
    for prime in primes:
        if number%prime == 0:
            return False
    return True

#n = 10
#print find_primes(n)
