class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1

        #pivot is the minimum, so we have to the pivot 

        while r>=l:
            mid=(l+r)//2

            #nums[mid]>nums[r] iff pivot lies in right half    
            if nums[mid]>nums[r]:
                l=mid+1
                
            # else pivot is the nums[mid] or lies in first half
            else:
                if nums[mid]<=nums[mid-1]:return nums[mid]
                else: r=mid-1
            

        