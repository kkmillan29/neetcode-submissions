class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2==1:
            return False
        bracarr=[]
        for i in range(len(s)):
            if s[i] in ["[","(","{"]:
                bracarr.append(s[i])
            else:
                if len(bracarr)==0:
                    return False
                obrac=bracarr.pop()
                if obrac=="[" and s[i]=="]":
                    continue
                elif obrac=="(" and s[i]==")":
                    continue
                elif obrac=="{" and s[i]=="}":
                    continue
                else:
                    return False 
        if len(bracarr)==0:
            return True
        else:
            return False