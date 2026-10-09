class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            total = numbers[l] + numbers[r]

            if total == target:
                return [l + 1, r + 1]
            elif total < target:
                l += 1
            else:
                r -= 1  
  


        # l, r = 0, 1

        # while l < len(numbers) and r < len(numbers):
        #     if l != r and numbers[l] + numbers[r] == target:
        #         return [l + 1, r + 1]

        #     elif numbers[l] + numbers[r] < target:
        #         r += 1

        #     else:
        #         l += 1
        #         r = l + 1   


        #converging pointers
        # l,r=0,len(numbers)-1
        # while l<r:
        #     if numbers[l]+numbers[r] > target:
        #         r-=1
        #     elif numbers[l]+numbers[r] < target:
        #         l+=1
        #     elif numbers[l]+numbers[r] == target:    
        #         return [l+1,r+1]
   
        