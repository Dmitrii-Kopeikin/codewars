import decimal
import time


def fib_iter(a, b, count):
    if count == 0:
        return b
    return fib_iter(a + b, a, count - 1)


def fib(n):
    is_negative_and_even = n < 0 and n % 2 == 0
    n = abs(n)
    result = 0

    if n > 2000000:
        decimal.getcontext().prec = 420000
        root_5 = decimal.Decimal(5).sqrt()
        phi = ((1 + root_5) / 2)

        result = (phi ** n - ((-phi) ** (-n))) / root_5

    if n >= 2:
        prev = 1
        while n > 0:
            result, prev = prev + result, result
            n -= 1
    elif n == 1:
        result = 1
    else:
        result = 0

    return -result if is_negative_and_even else result


if __name__ == '__main__':
    # print(fib_recursion(-1))
    # print(fib(-1))
    # print(fib_recursion(6))
    # print(fib(6))
    # print(fib_recursion(-6))
    # print(fib(-6))
    # print(int(fib(1491137)))
    start = time.time()
    print(fib(500000))
    print()
    print(fib(500001))
    print(time.time() - start)

    # print(fib_iter(1, 0, 3))
