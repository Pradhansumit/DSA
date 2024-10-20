def count_substring(string, sub_string):
    count = 0
    for i in range(0, len(string)):
        if sub_string[0] == string[i]:
            xyz = string[i : i + len(sub_string)]
            if len(xyz) == len(sub_string) and xyz == sub_string:
                count += 1
    return count


if __name__ == "__main__":
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
