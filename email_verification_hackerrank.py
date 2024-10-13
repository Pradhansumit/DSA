import email.utils, re


for i in range(int(input())):
    str = email.utils.parseaddr(input())
    if re.search(r"^[A-Za-z][\.\w\d-]+@[A-Za-z]+\.[A-Za-z]{1,3}$", str[1]):
        print(email.utils.formataddr(str))
