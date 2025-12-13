class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        setbusinessLine = set(["electronics", "grocery", "pharmacy", "restaurant"])
        # have to identify if code is only alphanumeric + _ and bussinessline in setbussinessline isActive = True
        newcode = []
        for i in range(len(code)):
            if isActive[i] == True:
                if businessLine[i] in setbusinessLine:
                    if len(code[i]) > 0 and  all(c.isalnum() or c == "_" for c in code[i] ):
                        newcode.append((code[i], businessLine[i]))
        # print(newcode)
        hi = sorted(newcode, key = lambda x : (x[1], x[0]))
        
        return [_ for _, c in hi]
