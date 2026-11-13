class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        stack = []
        pairs = [[p, s] for p, s in zip(position, speed)]

        for p, s in sorted(pairs, reverse=True):

            time = (target-p)/s
            if stack:
                if time <= stack[-1]:
                    continue
            stack.append(time)

        return len(stack)               


        