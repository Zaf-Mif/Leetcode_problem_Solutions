class Solution:
    def countVowels(self, word: str) -> int:
        ans = 0
        vowel = {"a", 'e', 'i', 'o', 'u'}
        n = len(word)
        for i in range(n):
            temp = 0
            if word[i] in vowel:
                temp = ((i+1) * (n-i))
                # print(temp)
                ans += temp 
        return ans 
