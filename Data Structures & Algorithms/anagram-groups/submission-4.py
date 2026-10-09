class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # without defaultdict(list)
        res={}
        for s in strs:
            count=[0]*26
            for c in s:
                count[ord(c)-ord('a')]+=1
            if tuple(count) not in res:
                res[tuple(count)] =[]

            res[tuple(count)].append(s)    
                
        return list(res.values())
                 
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         # with defaultdict(list)
#         res=defaultdict(list)
#         for s in strs:
#             count=[0]*26
#             for c in s:
#                 count[ord(c)-ord('a')]+=1
#             res[tuple(count)].append(s)    
                
#         return list(res.values())                 
