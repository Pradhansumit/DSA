if __name__ == "__main__":
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    i: int = 0
    j: int = 0
    k: int = 0

    combinations: list[list[int, int, int]] = [
        [i, j, k]
        for i in range(x + 1)
        for j in range(y + 1)
        for k in range(z + 1)
        if i + j + k != n
    ]

    sum = 0

    # output: list[list[int, int, int]] = [[i, j, k] for items in combinations sum=0 for item in items sum+=item if sum !=n]

    # xyz = []
    # for items in combinations:
    #     sum = 0
    #     for item in items:
    #         sum += item
    #     if sum != n:
    #         xyz.append(items)
    # print(xyz)
    print(combinations)
