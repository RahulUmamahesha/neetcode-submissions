class Solution:

     def hasDuplicate(self, nums:List[int])->bool:
        buc=set()
        for i in nums:
            if i not in buc:
                buc.add(i)
            else:
                return True
        return False    



# #  def hasDuplicate(self, nums:List[int])->bool:
# #         # nums.sort()
# #         # for i in range(len(nums)):
# #         #     if nums[i]==nums[i-1]:
# #         #         return True
# #         # return False   

# #         # return len(nums)!= len(set(nums))   


# # def hasDuplicate(self, nums:List[int])->bool:
# #     for i in range(len(nums)):
# #         for j in range(i+1,len(nums)):
# #             if nums[i]==nums[j]:
# #                 return True
# #     return False

















    
















