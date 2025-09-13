class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        hash = defaultdict(int)
        for word in words:
            for c in word:
                hash[c] += 1
        
        n = len(words)
        for val in hash.values():
            if val % n != 0:
                return False
        
        return True
