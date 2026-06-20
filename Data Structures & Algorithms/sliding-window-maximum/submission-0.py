class Solution:
    def maxSlidingWindow(self, nums, k):
        result = []
        max_ind = 0
        for i in range(1, k):
            if nums[i] > nums[max_ind]:
                max_ind = i
        result.append(nums[max_ind])

        for r in range(k, len(nums)):
            l = r - k + 1                    # left edge of current window

            if max_ind < l:                  # old max fell out of window
                max_ind = l
                for i in range(l, r + 1):    # rescan whole window
                    if nums[i] > nums[max_ind]:
                        max_ind = i
            elif nums[r] > nums[max_ind]:    # new element is bigger
                max_ind = r

            result.append(nums[max_ind])

        return result

                
            



        