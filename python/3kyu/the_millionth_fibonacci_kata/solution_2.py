from numpy import array
from numpy.linalg import matrix_power


def fib(n):
    if n == 0:
        return 0

    q_matrix = array([[1, 1], [1, 0]], dtype=object)

    sign = 1
    if n < 0 and n % 2 == 0:
        sign = -1

    return (matrix_power(q_matrix, abs(n) - 1))[0, 0] * sign


if __name__ == '__main__':
    print(fib(1000000))
