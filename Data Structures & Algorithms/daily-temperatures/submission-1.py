class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures) == 1:
            return [0]

        stack = []
        stack.append((0, temperatures[0])) # Keep track of index and temperature
        ret_list = [0] * len(temperatures)

        for i in range(1, len(temperatures)):
            temp = temperatures[i]
            while stack and stack[-1][1] < temp:
                val = stack.pop()
                ret_list[val[0]] = (i - val[0]) # Distance between temps
            
            stack.append((i, temp)) # Append for processing

        return ret_list
