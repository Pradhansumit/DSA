num_lines = int(input())
css = ""
for _ in range(num_lines):
    css += input()

i = 0
can_search = False
hex_digits = [
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
]
while i < len(css):
    if css[i] == "{":
        can_search = True
    if css[i] == "}":
        can_search = False
    if can_search:
        if css[i] == "#":
            validHex = False
            hex = "#"
            a = 1
            while css[i + a] in hex_digits:
                hex += css[i + a]
                a += 1
            if len(hex) == 4 or len(hex) == 7:
                print(hex)
    i += 1
