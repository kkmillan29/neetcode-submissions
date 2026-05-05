class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strdict=dict()
        for i in range(len(strs)):
            sortedstr=''.join(sorted(strs[i]))
            if sortedstr in strdict:
                sortedstrarr=strdict.get(sortedstr)
                sortedstrarr.append(strs[i])
                strdict[sortedstr]=sortedstrarr
            else:
                strdict[sortedstr]=[strs[i]]
        outputarr=[]
        for key,val in strdict.items():
            outputarr.append(val)
        return outputarr