class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(speed)

        posSpeed = [(position[i], speed[i]) for i in range(n)]
        posSpeed.sort()
        posSpeed = posSpeed[::-1]

        timePer = [0] * n

        noFleets = n

        for i in range(n):
            pos, spd = posSpeed[i]
            timefor = (target - pos) / spd

            if i > 0 and timePer[i-1] >= timefor:
                timePer[i] = timePer[i-1]
                noFleets -= 1
            else:
                timePer[i] = timefor

        return noFleets
            