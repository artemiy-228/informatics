# https://informatics.msk.ru/mod/statements/view.php?id=2296&chapterid=2948#1

time = int(input())

h = (time // 3600)
m = ((time % 3600) // 60)
s = (time % 60)

if m < 10:
    m = ('0' + str(m))

if s < 10:
    s = ('0' + str(s))

if h >= 24:
    h = (h % 24)


print(h, m, s, sep=":")


