# Last updated: 8/29/2025, 6:48:37 PM
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res=""
        for i in range(len(strs[0])):
            for s in strs:
                if i==len(s) or s[i]!=strs[0][i]:
                    return res
            res += strs[0][i]
        return res
                
        

        