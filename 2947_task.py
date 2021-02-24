# https://informatics.msk.ru/mod/statements/view.php?id=2296&chapterid=2947#1

n = int(input())

h = n // 60 % 24

m = n % 60

print(h, m)

# c = n // 1440
# if c >= 1:
#     print(h - (h * c), n1)
# else:
#     print(h, n1)

