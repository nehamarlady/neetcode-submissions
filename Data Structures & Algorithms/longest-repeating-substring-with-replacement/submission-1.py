class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,maxf,res=0,0,0
        charset={}

        for r in range(len(s)):
            charset[s[r]]=1+charset.get(s[r],0)
            maxf=max(maxf,charset[s[r]])

            while ((r-l+1)-maxf>k):
                charset[s[l]]-=1
                l+=1
            res=max(res,r-l+1)
        return res

        