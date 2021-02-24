# https://informatics.msk.ru/mod/statements/view.php?id=2296&chapterid=2948#1

n = int(input())
h = (n // 3600)
k = h % 23
h = h - k
mm = (n % 3600) // 60
ss = (n % 60)

mm = ("0" + str(mm))[-2:]
ss = ("0" + str(ss))[-2:]
print(h, mm, ss, sep=":")
