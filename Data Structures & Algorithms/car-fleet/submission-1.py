class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        vals = list(zip(position, speed))
        vals.sort(reverse = True)

        for pos, sp in vals:
            time_left = (target-pos) / sp
            if not stack or stack and time_left>stack[-1]:
                stack.append(time_left)

        return len(stack)   
        
        # diff = [target-pos for pos in position]
        # res = []

        # for idx,dist in enumerate(diff):
        #     res.append((dist/speed[idx],position[idx]))
        # res.sort(key=lambda x:x[1])

        # cur = res[-1][0]
        # fleets = 1
        # res.reverse()
        # for time, _ in res[1:]:
        #     if time>cur:
        #         fleets+=1
        #         cur = time
        
        # return fleets