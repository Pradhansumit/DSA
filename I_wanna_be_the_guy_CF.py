if __name__ == "__main__":
    level: int = int(input())

    abc = input().strip()
    p = int(abc[:1])
    X = abc.split()[2:]

    xyz = input().strip()
    q = int(xyz[:1])
    Y = xyz.split()[2:]

    levels: list = []
    for i in range(level):
        levels.append(i)

    for lvl in levels:
        for x in X:
            if lvl == x:
                levels.pop(lvl)

    for lvl in levels:
        for y in Y:
            if lvl == y:
                levels.pop(lvl)

    if len(levels) > 0:
        print("Oh, my keyboard!")
    else:
        print("I become the guy.")
