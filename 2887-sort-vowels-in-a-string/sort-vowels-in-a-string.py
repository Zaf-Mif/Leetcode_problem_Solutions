class Solution:
    def sortVowels(self, s: str) -> str:
        

        def isVowel(ch):
            vowel = {'a','e','i','o','u','A','E','I','O','U'}
            if ch in vowel:
                return True
            return False
        temp = []  
        for word in s:
            if isVowel(word):
                temp.append(word)
        
        temp.sort()
        ans, j  = '', 0

        for word in s:
            if isVowel(word):
                ans += temp[j]
                j += 1
            else:
                ans += word

        return ans