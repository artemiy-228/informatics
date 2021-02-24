# https://informatics.msk.ru/mod/statements/view.php?id=2296&chapterid=2948#1

n = int(input())
h = (n // 3600)
mm = (n % 60)
ss = (n % 60)
print(h, mm, ss, sep=":")
