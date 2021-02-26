# https://informatics.msk.ru/mod/statements/view.php?id=2296&chapterid=2956#1

a = str(input())
b = int((a[0:1]))
e = int((a[1:2]))
d = int((a[2:3]))
k = int((a[3:4]))

n = int(b * k + d * e + 1)
m = n - (n - 1)
print(m)




