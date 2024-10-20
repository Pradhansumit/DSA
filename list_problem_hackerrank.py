if __name__ == "__main__":
    lines: int = int(input())
    actions: list[list] = []
    _my_list: list = []

    for _ in range(lines):
        _input: list = list(input().strip().split())
        actions.append(_input)

    for i in range(len(actions)):

        if actions[i][0] == "insert":
            _my_list.insert(int(actions[i][1]), int(actions[i][2]))

        elif actions[i][0] == "print":
            print(_my_list)

        elif actions[i][0] == "remove":
            _my_list.remove(int(actions[i][1]))

        elif actions[i][0] == "append":
            _my_list.append(int(actions[i][1]))

        elif actions[i][0] == "sort":
            _my_list.sort()

        elif actions[i][0] == "pop":
            _my_list.pop()

        elif actions[i][0] == "reverse":
            _my_list.reverse()
