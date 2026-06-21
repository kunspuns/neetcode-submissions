class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result=[0]*len(temperatures)
        stack=[]

        for i,temp in enumerate(temperatures):

            while stack and temp>temperatures[stack[-1]]:
                prev_ind = stack.pop()
                result[prev_ind] = i - prev_ind

            stack.append(i)

        return result


        