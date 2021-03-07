# https://informatics.msk.ru/mod/statements/view.php?id=276#1

a = int(input())
b = int(input())
if b > a:
    a, b = b, a
print(a)