# Project Euler solutions
# tmarathe

from collections import Counter

def problem1():
    total = sum(range(0,1000,3)) + sum(range(0,1000,5)) - sum(range(0,1000,15))
    print(total)

def problem2():
    #gr = (1 + 5 ** 0.5)/2 # golden ration
    # closed form of fibonacci series might yield a faster solution
    #fib_term = int(((gr ** i) - (-gr)**-i)/5**0.5)
    i, j = 0, 1
    total = 0
    while i < 4000000:
        i, j = j, i+j
        if i%2 == 0:
            total += i
    print(total)

def problem3(): # can be improved using quadratic sieve, etc
    target = 600851475143
    divisor = 2
    while target > divisor:
        if target % divisor == 0:
            target = target/divisor
        divisor += 1
    print(divisor)

def problem4():
    for t in range(999**2, (100**2)-1, -1):
        if str(t) == str(t)[-1::-1]: # palindrome check
            for i in range(100, 1000):
                if t%i == 0 and t/i < 999:
                    print(t)
                    # print(i)
                    return
def problem5():
    required_primes = Counter()
    for i in range(2, 21):
        primes = Counter(problem5_prime_factors(i))
        required_primes = required_primes | primes # union of counters
    prime_counts = list(required_primes.items())
    total = 1
    for tup in prime_counts:
        total *= tup[0]**tup[1] # prime number ** number of occurences
    print(total)

def problem5_prime_factors(n):
    if n == 1:
        return []
    relevant_primes = [2, 3, 5, 7, 11, 13, 17, 19]
    for p in relevant_primes:
        if n%p == 0:
            return [p] + problem5_prime_factors(n/p)

def problem6():
    sum_of_nums = 100*(100+1)/2 # n(n+1)/2
    sum_of_sqs = 100*(100+1)*(200+1)/6 # n(n+1)(2n+1)/6
    print(sum_of_nums**2 - sum_of_sqs)


if __name__ == '__main__':
    problem6()
