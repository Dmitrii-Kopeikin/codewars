import operator
from functools import reduce

print(reduce(operator.xor, [1, 2, 1]))
