import numpy as np


def create_arrays():
    x = np.zeros(10)
    y = np.random.randn(100)
    z = np.full(shape=(42, 42 ,42), fill_value=42)
    return x, y, z


def multiply_matrices(m_list):
    if not multiplication_check(m_list):
        return
    res_m = m_list[0]
    for i in range(1, len(m_list)):
        res_m = matrix_multiplication(res_m, m_list[i])
    return res_m


def matrix_multiplication(m1, m2):
    return np.matmul(m1, m2)


def multiplication_check(m_list):
    check = True
    for i in range(len(m_list)-1):
        print(m_list[i].shape)
        if m_list[i].shape[1] != m_list[i+1].shape[0]:
            check = False
    return check


def compute_2d_distance(a1, a2):
    dist = np.linalg.norm(a1-a2)
    return dist


def compute_multidimensional_distance(a1, a2):
    dist = np.linalg.norm(a1-a2)
    return dist


def compute_pair_distances(a):
    a_dim = len(a)
    dist = np.zeros(shape=(a_dim, a_dim))
    for i in range(a_dim):
        for j in range(a_dim):
            dist[i, j] = np.linalg.norm(a[i]-a[j])
    return dist
