# https://informatics.msk.ru/mod/statements/view.php?id=2296&chapterid=2951#1

a, b, n = int(input()), int(input()), int(input())
c = b * n % 100
d = (b * n - c) / 100
e = int(a * n + d)
print(e, c)

