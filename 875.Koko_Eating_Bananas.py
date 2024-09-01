def minEatingSpeed(self, piles: List[int], h: int) -> int:
        upper = max(piles)
        lower = 1 
        current_max = upper
        while upper >= lower:
            mid = (upper + lower) // 2
            rate = self.calchours(piles, mid)
            if rate <= h:
                current_max = mid
                upper = mid - 1 
            else:
                lower = mid + 1 
        return current_max 

    def calchours(self, bananas, rate):
        counter = 0
        for i in bananas:
            counter += math.ceil(float(i) / rate)
        return counter