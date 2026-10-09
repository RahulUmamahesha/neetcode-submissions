class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        countS, countT={},{}    
        for i in range(len(s)):
            countS[s[i]]= countS.get(s[i],0)+1
            countT[t[i]]= countT.get(t[i],0)+1
        if countS == countT:
            return True
        return False        



# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         #hashmap using arrays
#         if len(s)!=len(t):
#             return False
#         count=[0]*26
#         for i in range(len(s)):
#             count[ord(s[i])-ord('a')]+=1
#             count[ord(t[i])-ord('a')]-=1
#         for val in count:
#             if val !=0:
#                 return False
#         return True            
        




        # #hashmap
        # if len(s)!=len(t):
        #     return False
        # countT,countS={},{}
        # for i in range(len(s)):
        #     countT[t[i]]=1+countT.get(t[i],0)    
        #     countS[s[i]]=1+countS.get(s[i],0)   
        # return countT == countS

    


        
        
        
        
        
        
    

