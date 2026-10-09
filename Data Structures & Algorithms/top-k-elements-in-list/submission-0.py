class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        frequency=[[] for i in range(len(nums)+1)]
        for i in nums:
            count[i]=1+count.get(i,0)
        for n, c in count.items():
            frequency[c].append(n)
        res=[]
        for i in range(len(frequency)-1,0,-1):
            for num in frequency[i]:
                res.append(num)
                if len(res)==k:
                    return res





    # Sorting

    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     count = {}
    #     for num in nums:
    #         count[num] = 1 + count.get(num, 0)

    #     arr = []
    #     for num, cnt in count.items():
    #         arr.append([cnt, num])
    #     arr.sort()

    #     res = []
    #     while len(res) < k:
    #         res.append(arr.pop()[1])
    #     return res        
            

    # Min heap
    
    #  def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     count = {}
    #     for num in nums:
    #         count[num] = 1 + count.get(num, 0)

    #     heap = []
    #     for num in count.keys():
    #         heapq.heappush(heap, (count[num], num))
    #         if len(heap) > k:
    #             heapq.heappop(heap)

    #     res = []
    #     for i in range(k):
    #         res.append(heapq.heappop(heap)[1])
    #     return res       


        
        