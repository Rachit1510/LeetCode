# Last updated: 10/1/2025, 11:06:39 PM
from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet= set(wordList)
        if endWord not in wordSet:
            return 0

        queue= deque()
        queue.append((beginWord,1))
        while len(queue)!=0:
            curr_word,level= queue.popleft()
            if curr_word == endWord:
                return level
            
            for i in range(len(curr_word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    if c==curr_word[i]:
                        continue
                    new_word= curr_word[:i]+c+curr_word[i+1:]
                    if new_word in wordSet:
                        queue.append((new_word,level+1))
                        wordSet.remove(new_word)
        return 0
                    
        