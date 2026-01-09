l1 = [1,2,3,4]
if len(l1)%2==1:
    print(l1[len(l1)//2])
else:
    print(((l1[len(l1)//2-1])+(l1[len(l1)//2]))/2)