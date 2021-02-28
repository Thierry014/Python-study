 def largestAltitude(self, gain) -> int:
        alt = [0]
        
        for i in range(len(gain)):
            res = alt[i]+gain[i]
            alt.append(res)
        
        return max(alt)