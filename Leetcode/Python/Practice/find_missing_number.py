def find_missing_num(lst:list,n:int)->int:
    expected_sum = n*(n+1)//2
    lst_sum = sum(lst)
    return expected_sum - lst_sum

print(find_missing_num([1,2,3,4,5,6,7,9],9))