class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #first we find the pivot
        n=len(nums)
        r=n-1
        l=0

        while r>l:
            mid=(l+r)//2
            if nums[mid]>nums[r]:
                l=mid+1

            else: r=mid

        pivot=l

        #now we find the target resetting l=0, r=n-1

        l=0
        r=n-1

        while r>=l:
            mid=((l+r)//2)%n
            if nums[(mid+pivot)%n]==target: return (mid+pivot)%n
            if target>nums[(mid+pivot)%n]: l=mid+1
            else:r=mid-1

        return -1


        