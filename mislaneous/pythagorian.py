"""
print firt 10 pythagorean triplets
"""


def print_triplets(target):
    import math
    count = 0
    i = 0
    j = 0
    for i in range(1, 1000):
        for j in range(i, 1000):
            if math.sqrt(i ** 2 + j ** 2) % 1 == 0.0:
                print(str(i) + " " + str(j) + " ", end='')
                print(math.sqrt(i ** 2 + j ** 2))
                count += 1
                if count == target:
                    return None

def print_triplets_2(target):
    import math

    list = [[i,j,math.sqrt(i ** 2 + j ** 2)] for i in range(1, 1000) for j in range(i, 1000) if math.sqrt(i ** 2 + j ** 2) % 1 == 0.0]

    for i in range(target):
        print(list[i])


if __name__ == '__main__':
    print_triplets(10)
    print_triplets_2(10)
