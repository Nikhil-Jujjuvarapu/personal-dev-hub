def two_sum(nums: list[int], target: int) -> list[int]:
    seen: dict[int, int] = {}
    for i, num in enumerate(nums):
        if (complement := target - num) in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
print(two_sum([1,2,0,4,5],1))