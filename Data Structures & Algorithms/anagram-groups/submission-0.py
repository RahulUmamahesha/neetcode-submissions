class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a=defaultdict(list)
        for s in strs:
            c=[0]*26
            for i in s:
                c[ord(i)-ord('a')]+=1
            a[tuple(c)].append(s)    


        return list(a.values())
        
        