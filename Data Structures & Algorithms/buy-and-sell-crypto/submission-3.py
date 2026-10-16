class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #parallel 2pointers 
        [10,1,5,6,7,1]
        l,r=0,1
        maxp=0
        while r<len(prices):
            if prices[l]<prices[r]:
                total=prices[r]-prices[l]
                maxp=max(maxp,total)
            else:
                l=r
            r+=1    
        return maxp            
      

        # DP
        # maxp=0
        # minbuy=prices[0]
        # for i in prices:
        #     maxp=max(maxp,i-minbuy)
        #     minbuy= min(minbuy,i)
        # return maxp    
