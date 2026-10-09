class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s={}
        for i, n in enumerate(nums):
            dif= target -n
            if dif in s:
                return [s[dif],i]
            s[n]=i    




        # Not working becz if same number restur is giving 1st index and complexity is o(n^2)
        # for i in range(len(nums)):
        #     dif =target-nums[i]
        #     if dif in nums:
        #         return [i, nums.index(dif)]
        