class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            target = -nums[i]

            while l < r:
                total = nums[l] + nums[r]

                if total > target:
                    r -= 1
                elif total < target:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    # need to increment one pointer
                    l += 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        return res