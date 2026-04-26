class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def charCount(s):
            smap=dict()
            for i in range(len(s)):
                if s[i] in smap.keys():
                    smap[s[i]]=smap.get(s[i],0)+1
                else:
                    smap[s[i]]=1
            return smap
        if len(s)!=len(t):
            return False 

        smap=charCount(s)
        tmap=charCount(t)
        for key,value in smap.items():
            if key in tmap.keys():
                tval=tmap.get(key)
                if value!=tval:
                    return False
            else:
                return False
        return True

        