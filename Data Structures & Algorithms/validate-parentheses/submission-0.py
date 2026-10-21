class Solution:
    def isValid(self, s: str) -> bool:
        a=[]
        b={"(":')','[':']',"{":"}"}
        for i in s:
            if i in b:
                a.append(i)
            elif a and b[a.pop()]==i:
                continue 
            else:
                return False
        return not a