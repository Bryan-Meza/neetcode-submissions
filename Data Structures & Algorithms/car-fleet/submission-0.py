class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Generate pairs of (position, speed)
        pairs = [(p, s) for p, s in zip(position, speed)]
        # Sort by closest position to target
        pairs.sort(reverse = True)
        # Stack to track distances it takes to reach target
        stack = []
        for p, s in pairs:
            # Save the Distance = position / time in Stack
            stack.append((target - p) / s)
            while len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)