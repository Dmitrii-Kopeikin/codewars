import decimal


def fib(n):
    is_negative_and_even = n < 0 and n % 2 == 0
    n = abs(n)

    decimal.getcontext().prec = 420000
    root_5 = decimal.Decimal(5).sqrt()
    phi = ((1 + root_5) / 2)

    result = (phi ** n - ((-phi) ** (-n))) / root_5

    return -result if is_negative_and_even else result
