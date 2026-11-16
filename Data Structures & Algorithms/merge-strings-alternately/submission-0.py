class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1=len(word1)
        l2=len(word2)
        i=0
        j=0
        ans=""
        while l1>i and l2>j:
            ans+=word1[i]
            i+=1
            ans+=word2[j]
            j+=1
        while l1>i:
            ans+=word1[i]
            i+=1
        while l2>j:
            ans+=word2[j]
            j+=1
        return ans