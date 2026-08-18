class Solution:
    def isRobotBounded(self, arr: str) -> bool:
        mp = {"L": 0, "R": 0}
        x = 0
        y = 0
        for ch in arr:
            if ch == "L":
                if mp["R"] > 0:
                    mp["R"] -= 1
                else:
                    mp["L"] += 1
            elif ch == "R":
                if mp["L"] > 0:
                    mp["L"] -= 1
                else:
                    mp["R"] += 1
            else:
                if mp["R"] > 0:
                    if mp["R"] % 4 == 0:
                        y += 1
                    elif mp["R"] % 4 == 1:
                        x += 1
                    elif mp["R"] % 4 == 2:
                        y -= 1
                    elif mp["R"] % 4 == 3:
                        x -= 1
                elif mp["L"] > 0:
                    if mp["L"] % 4 == 0:
                        y += 1
                    elif mp["L"] % 4 == 1:
                        x -= 1
                    elif mp["L"] % 4 == 2:
                        y -= 1
                    elif mp["L"] % 4 == 3:
                        x += 1
                else:
                    y += 1
        if x == 0 and y == 0:
            return True
        if mp["L"] % 4 != 0 or mp["R"] % 4 != 0:
            return True

        return False