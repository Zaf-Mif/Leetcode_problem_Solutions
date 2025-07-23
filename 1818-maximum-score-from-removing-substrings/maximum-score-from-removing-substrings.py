class Solution:
    def removeString(self, w, pri):
        self.stack = []
        for word in w:
            if (word == pri[1] and self.stack and self.stack[-1] == pri[0]) :
                self.stack.pop()
            else:
                self.stack.append(word)
        return "".join(self.stack)

    def maximumGain(self, s: str, x: int, y: int) -> int:
        total = 0 
        high = "ab" if x >= y else "ba"
        low = "ab" if high != "ab" else "ba"
        
        #call it for high
        word = self.removeString(s,high)
        removed = (len(s) - len(word)) // 2
        total += removed * (x if x >= y else y)

        # call it for low
        final = self.removeString(word,low)
        removed = (len(word) - len(final)) // 2
        total += removed * (min(x,y))

        return total
        