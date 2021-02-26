# https://informatics.msk.ru/mod/statements/view.php?id=2296&chapterid=2948#1

n = int(input())
h1 = (n // 86400)
h = (n // 3600)
k = n // 24
mm = (n % 3600) // 60
ss = (n % 60)

mm = ("0" + str(mm))[-2:]
ss = ("0" + str(ss))[-2:]
print((h1 * h), mm, ss, sep=":")
