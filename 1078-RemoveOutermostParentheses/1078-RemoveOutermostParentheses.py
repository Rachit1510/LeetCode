# Last updated: 11/3/2025, 9:24:48 PM
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res=""
        count=0
        for ch in s:
            if ch=='(':
                count+=1
                if count>1:
                    res+=ch
            else:
                count-=1
                if count>0:
                    res+=ch
        return res