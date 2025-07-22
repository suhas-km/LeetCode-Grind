class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        #Time: O(n*log n)
        #space: O(1)
        asteroids.sort()
        for i in asteroids:
            if i <= mass:
                mass = mass + i
            
            else:
                return False
        return True
