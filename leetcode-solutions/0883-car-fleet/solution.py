from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        
        # pair each car's position with its speed
        for i in range(len(position)):
            cars.append((position[i], speed[i]))

        # sort cars by position from smallest to largest
        cars.sort()

        fleets = 0
        
        # stores the time of the fleet ahead (closest to target)
        slowest_time_ahead = -1.0

        # iterate from closest car to farthest car
        for pos, spd in reversed(cars):
            time_to_target = (target - pos) / spd

            # if this car cannot catch the fleet ahead, it forms a new fleet
            if time_to_target > slowest_time_ahead:
                fleets += 1
                slowest_time_ahead = time_to_target
            # otherwise it joins the existing fleet ahead

        return fleets

