# Last updated: 8/29/2025, 6:48:15 PM
class Solution:
    def reverseWords(self, s: str) -> str:
        b=s.split()
        b.reverse()
        reverse_word= " ".join(b)
        return reverse_word