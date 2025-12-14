lst = [1,[2,3],[1,2,3],4]

lst1 = []
lst2 = []

for i in lst:
    if isinstance(i,list):
        for j in i:
            lst1.append(j)
    if isinstance(i,int):
            lst1.append(i)
for i in lst1:
     if i not in lst2:
          lst2.append(i)
print((lst2))