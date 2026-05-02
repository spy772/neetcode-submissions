class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if target == 0:
            return len(position) # By def. all positions are unique at the start
        
        cars = [list(car) for car in zip(position, speed)]
        cars.sort(reverse=True)
        stack = []

        for pos, spd in cars:
            stack.append((target - pos) / spd)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop() # Cars will finish at the same time or one "overtakes" the other

        return len(stack)