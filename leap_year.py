def is_leap(year: int) -> bool:
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        return True
    else:
        return False


if __name__ == "__main__":
    year: int = int(input())
    print(is_leap(year))
