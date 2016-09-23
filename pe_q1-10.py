# Project Euler solutions - Question 1-10
# tmarathe

from collections import Counter
import math

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

def problem7():
    # use nth prime approximation
    # known: for n>6, n*(ln(n)+ln(ln(n) − 1)) < p_n < n(ln(n) + ln(ln(n))
    target = 10001
    lower_bound = math.ceil(target*(math.log(target) + math.log(math.log(target)) - 1))
    upper_bound = int(target*(math.log(target) + math.log(math.log(target))))
    i = 0
    for p in range(lower_bound, upper_bound+1):
        if problem7_is_prime(p):
            i+=1
            if i == 39: # 39th prime after our lower bound is the one we want
                # yeah, I know this is really lazy
                print(p)

def problem7_is_prime(p):
    for i in range(2, int(math.sqrt(p))+1):
        if p%i == 0:
            return False
    return True

def problem8():
    x = '73167176531330624919225119674426574742355349194934\
96983520312774506326239578318016984801869478851843\
85861560789112949495459501737958331952853208805511\
12540698747158523863050715693290963295227443043557\
66896648950445244523161731856403098711121722383113\
62229893423380308135336276614282806444486645238749\
30358907296290491560440772390713810515859307960866\
70172427121883998797908792274921901699720888093776\
65727333001053367881220235421809751254540594752243\
52584907711670556013604839586446706324415722155397\
53697817977846174064955149290862569321978468622482\
83972241375657056057490261407972968652414535100474\
82166370484403199890008895243450658541227588666881\
16427171479924442928230863465674813919123162824586\
17866458359124566529476545682848912883142607690042\
24219022671055626321111109370544217506941658960408\
07198403850962455444362981230987879927244284909188\
84580156166097919133875499200524063689912560717606\
05886116467109405077541002256983155200055935729725\
71636269561882670428252483600823257530420752963450'
    greatest = []
    for i in range(0, 988):
        segment = [int(s) for s in list(x[i:i+13])]
        if 0 not in segment:
             if problem8_product(segment) >= problem8_product(greatest):
                 greatest = segment
    print(problem8_product(greatest))

def problem8_product(l):
    prod = 1
    for j in l:
        prod *= j
    return prod

def problem9():
    # Euclid's formula: given arbitrary +ve ints m, n with m>n,
    # a = m**2 - n**2, b = 2mn, c = m**2 + n**2 form a Pythagorean triple
    for i in range(1000):
        for j in range(i, 1000):
            a = j**2 - i**2
            b = 2*j*i
            c = j**2 + i**2
            if a+b+c == 1000:
                print(a*b*c)
                return

def problem10():
    # need to find an efficient prime sieve
    # sieve of erastothenes implemented here
    ceiling = 2000000
    sieve = [True]*ceiling
    for i in range(2, int(math.sqrt(ceiling))):
        if sieve[i]:
            for j in range(i**2, ceiling, i):
                sieve[j] = False
    total = 0
    for k in range(2, ceiling):
        if sieve[k]:
            total+= k
    print(total)


if __name__ == '__main__':
    problem10()
