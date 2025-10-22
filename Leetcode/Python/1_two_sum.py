class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dum_dict = {}
        for i,v in enumerate(nums):
            num = target-v
            if num in dum_dict:
                return [dum_dict[num],i]
            dum_dict[v]=i

ex = Solution()
print(ex.twoSum([2,7,11,15],9))