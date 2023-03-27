def add(n):
    class Number(int):
        def __call__(self, num):
            return Number(self + num)

    return Number(n)


if __name__ == '__main__':
    addTwo = add(2)
    print(addTwo + 5)
    print(addTwo(3)(3)(3))
    print(addTwo)
