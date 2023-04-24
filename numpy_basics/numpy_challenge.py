import numpy as np


def create_arrays():
    """Creates 3 custom arrays with numpy"""
    x = np.zeros(10)
    y = np.random.randn(100)
    z = np.full(shape=(42, 42, 42), fill_value=42)
    return x, y, z


def multiplication_check(m_list):
    """Checks the list of matrices if it's possible to perform consecutive
    multiplication on them
    :param list m_list: list of numpy arrays
    :returns: True if it's possible to consecutively multiply givveb arrays,
    otherwise - False
    :rtype: bool
    """
    check = True
    for i in range(len(m_list)-1):
        print(m_list[i].shape)
        if m_list[i].shape[1] != m_list[i+1].shape[0]:
            check = False
    return check


def multiply_matrices(m_list):
    """Cosecustively multiplies a list of numpy matrices
    :param list m_list: list of numpy arrays
    :returns: result of multiplication of given matrices. If matrices can't multiplied
    in the given order - returns None
    :rtype: numpy.ndarray, None
    
    """
    if not multiplication_check(m_list):
        return
    res_m = m_list[0]
    for i in range(1, len(m_list)):
        res_m = matrix_multiplication(res_m, m_list[i])
    return res_m


def matrix_multiplication(m1, m2):
    """Mutiplies 2 matrices.
    :param np.ndarray m1: first matrix
    :param np.ndarray m2: second matrix
    :returns: multiplication result of 2 matrices
    :rtype: numpy.ndarray
    """
    return np.matmul(m1, m2)


def compute_2d_distance(a1, a2):
    """Computes distance betwenn two 1D arrays with length equal 2
    (points in 2D space)
    :param np.ndarray a1: first array
    :param np.ndarray a2: second array
    :returns: 2D distances between two points
    :rtype: numpy.float64
    """
    dist = np.linalg.norm(a1-a2)
    return dist


def compute_multidimensional_distance(a1, a2):
    """Computes distance betwenn two 1D arrays of same length
    :param np.ndarray a1: first array
    :param np.ndarray a2: second array
    :returns: distances between two points
    :rtype: numpy.float64
    """
    dist = np.linalg.norm(a1-a2)
    return dist


def compute_pair_distances(arr):
    """Computes pairwise distances for rows of 2D array.
    :param numpy.ndarray: 2D array in wich rows represent
    observations and columns represent features.
    :returns: matrix with pairwise distances for observations
    :rtype: numpy.ndarray
    """
    arr_dim = len(arr)
    dist = np.zeros(shape=(arr_dim, arr_dim))
    for i in range(arr_dim):
        for j in range(arr_dim):
            dist[i, j] = compute_multidimensional_distance(arr[i], arr[j])
    return dist