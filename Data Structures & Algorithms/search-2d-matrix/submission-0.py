class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        columns = len(matrix[0])
        rows = len(matrix)
        top, bot = 0, rows - 1

        while top <= bot:
            mid = (top + bot) // 2
            target_row = -1

            if matrix[mid][-1] == target:
                return True
            elif matrix[mid][-1] < target:
                top = mid + 1                       # row max < target -> go down
            else:
                if mid == 0 or matrix[mid - 1][-1] < target:
                    target_row = mid                # boundary row found
                else:
                    bot = mid - 1                   # go up

            if target_row != -1:
                l, r = 0, columns - 1
                while l <= r:
                    cmid = (l + r) // 2
                    if matrix[target_row][cmid] == target:
                        return True
                    elif target < matrix[target_row][cmid]:
                        r = cmid - 1
                    else:
                        l = cmid + 1
                return False

        return False
        

    



        