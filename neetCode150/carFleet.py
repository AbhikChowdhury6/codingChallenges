from types import List
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ocars = [[p, s] for p, s in zip(position, speed)]
        ocars = sorted(ocars, key=lambda x:x[0])

        def ttt(c): #time to target
            distance = target - c[0]
            return distance / c[1]
        
        #ocars is now a stack, we
        numfleets = len(position)
        topcartime = ttt(ocars.pop())
        while ocars:
            nextcartime = ttt(ocars.pop())
            if nextcartime <= topcartime: #it catches up
                numfleets -= 1
            else:
                topcartime = nextcartime
        
        return numfleets



        