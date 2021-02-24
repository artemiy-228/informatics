# https://informatics.msk.ru/mod/statements/view.php?id=2296&chapterid=2947#1

n = int(input())
h = n // 60
n1 = n % 60
c = n // 1440
if c >= 1:
    print(h - (h * c), n1)
else:
    print(h, n1)

