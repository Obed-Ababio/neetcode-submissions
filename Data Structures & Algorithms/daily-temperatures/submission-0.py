class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:


        # Loop through temps

        # if current temp is hotter than top of stack pop and note index

        result = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                j = stack.pop()
                result[j] = i - j
            stack.append(i)
    
        return result
                  



      
        