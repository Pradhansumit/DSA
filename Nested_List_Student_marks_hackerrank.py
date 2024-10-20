if __name__ == "__main__":
    number: int = int(input())
    item: list = []
    array: list = []
    for i in range(number):
        item.append(input())
        item.append(input())
        array.append(item)
        item = []

    for i in range(len(array)):
        if array[0][i] > array[0][i + 1]:
            c = 0
            c = array[0][i]
            item[0][i] = item[0][i + 1]
            item[0][i + 1] = c

    count: int = 0
    xyz: int = 0

    for x in range(len(array) - 1):
        if array[0][x] == array[0][x + 1]:
            count += 1
            xyz = array
        else:
            count = 0
            xyz = 0

    for i in xyz:
        print(i)
