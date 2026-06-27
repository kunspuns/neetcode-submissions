class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #first finding the maximum pile 
        m=-1

        for val in piles:
            if val>m: m=val

        #now by performing BS on 1,..,m, we will find minimum k

        l=1
        r=m
        k=m

        while r>=l:
            mid=(r+l)//2
            #now counting numbers that mid rate would take

            hrs=sum(-(-val//mid) for val in piles)
            if hrs<=h and mid<k:
                k=mid
                r=mid-1

            else:
                l=mid+1

        else: return k
        

