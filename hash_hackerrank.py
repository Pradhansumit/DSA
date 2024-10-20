if __name__ == "__main__":
    number: int = int(input())
    elements: tuple = tuple(input().strip().split())
    elements = elements[:number]
    print(elements)

    print(hash(elements))
