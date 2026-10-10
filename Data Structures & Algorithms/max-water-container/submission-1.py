class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r=0,len(heights)-1
        maxarea,curarea=0,0
        while (l < r):
            mindis=min(heights[l],heights[r])
            curarea=mindis*(r-l)
            if curarea > maxarea:
                maxarea=curarea
            if heights[l] > heights[r]:
                r -=1
            else:
                l+=1
        return maxarea
        