import random

def experiment1(times):
    countA = 0
    countB = 0
    for i in range(times):
        rollA = random.randint(1,6)
        if rollA == 6:
            countA += 1
            rollB = random.randint(1,6)
            if rollB == 6:
                countB += 1
    return(countB, countA, countB/countA)

def experiment2(times):
    n, k = 0, 0
    for i in range(times):
        rollA, rollB =  random.randint(1,6), random.randint(1,6)
        if rollA == 6 or rollB == 6:
            n += 1
            if rollA == 6 and rollB == 6:
                k += 1
    return(k, n, k/n)

if __name__ == '__main__':
    print(experiment1(100000))
    print(experiment2(100000))
   
