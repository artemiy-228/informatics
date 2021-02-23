# https://informatics.msk.ru/mod/statements/view.php?id=2296&chapterid=2957#1

n = int(input())
m = int(input())

a = ((n // m) or (m // n) % 2 != 0)
print(True)