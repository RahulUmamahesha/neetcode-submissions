class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        string_1_freq = {}
        string_2_freq= {}

        for char in s:
            string_1_freq[char] = string_1_freq.get(char, 0) + 1
        
        for char in t:
            string_2_freq[char] = string_2_freq.get(char, 0) + 1
        
        for char in s:
            if char in string_2_freq:
                if string_2_freq[char] != string_1_freq[char]:
                    return False
            else:
                return False
        
        for char in t:
            if char in string_1_freq:
                if string_2_freq[char] != string_1_freq[char]:
                    return False
            else:
                return False
        return True


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

    


        
        
        
        
        
        
    

