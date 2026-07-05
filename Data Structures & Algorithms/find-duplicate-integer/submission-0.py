class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        fast = slow = 0
        
        n = len(nums)
        
        while 1:
                
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        fast = 0

        while fast != slow:
            slow=nums[slow]
            fast=nums[fast]

        return slow


        