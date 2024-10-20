if __name__ == "__main__":
    s = input()

    for _s in s:

        if _s.isalnum():
            print(True)
        else:
            print(False)

        if _s.isalpha():
            print(True)
        else:
            print(False)

        if _s.isdigit():
            print(True)
        else:
            print(False)

        if _s.islower():
            print(True)
        else:
            print(False)

        if _s.isupper():
            print(True)
        else:
            print(False)
