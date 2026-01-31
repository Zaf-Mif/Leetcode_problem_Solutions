class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        target = ord(target)
        mn = 123

        for s in letters:
            if ord(s) > target and mn > ord(s):
                mn = ord(s)
        return chr(mn) if mn != 123 else letters[0]