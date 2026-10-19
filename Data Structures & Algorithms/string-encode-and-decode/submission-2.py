class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        res=[]
        for s in strs:
            res.append(str(len(s)))   
            res.append("#")
            res.append(s)
        return ''.join(res)    

        # if not strs:
        #     return ""
        # size, res=[], []
        # for s in strs:
        #     size.append(len(s))
        # for sz in size:
        #     res.append(str(sz))
        #     res.append(",")
        # res.append("#")
        # res.extend(strs)
        # return ''.join(res)            

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        res, i=[],0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j

        return res
        # if not s:
        #     return []
        # sizes, res, i=[], [], 0
        # while s[i]!='#':
        #     j=i
        #     while s[j]!=",":
        #         j+=1        
        #     sizes.append(int(s[i:j]))       
        #     i=j+1
        # i=i+1
        # for sz in sizes:
        #     res.append(s[i:(i+sz)])
        #     i=i+sz
        # return res        



