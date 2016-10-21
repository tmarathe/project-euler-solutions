
# Bertrand industry merger simulation
def calculate_mc_change(m_i, m_j, d_ij, d_ji, p_i, p_j):
    c_change = (m_i*d_ij*d_ji + m_j*d_ji*(p_j/p_i))/((1-m_i)*(1 - d_ij*d_ji))
    return c_change

if __name__ == '__main__':
    m_i = 0.58
    m_j = 0.189
    d_ji = 0.2
    d_ij = 2/15
    p_i = 1500
    p_j = 1850
    c = calculate_mc_change(m_i, m_j, d_ij, d_ji, p_i, p_j)
    print(c, 1-c)
