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

# Bertrand industry merger simulation
def calculate_mc_change(m_i, m_j, d_ij, d_ji, p_i, p_j):
    c_change = (m_i*d_ij*d_ji + m_j*d_ji*(p_j/p_i))/((1-m_i)*(1 - d_ij*d_ji))
    return c_change

if __name__ == '__main__':
    #print(experiment1(100000))
    #print(experiment2(100000))
    m_i = 0.58
    m_j = 0.189
    d_ji = 0.2
    d_ij = 2/15
    p_i = 1500
    p_j = 1850
    c = calculate_mc_change(m_i, m_j, d_ij, d_ji, p_i, p_j)
    print(c, 1-c)
