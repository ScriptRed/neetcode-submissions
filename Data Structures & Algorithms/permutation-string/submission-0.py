class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freqs1 = {}
        for item in s1:
            freqs1[item] = freqs1.get(item, 0 ) + 1
        
        freqs2 = {}
        k = len(s1)
        for i in range(len(s2)):
            if k>0:
                freqs2[s2[i]] = freqs2.get(s2[i], 0) + 1
                k -= 1
            else:
                if freqs2[s2[i-len(s1)]] == 1:
                    del freqs2[s2[i-len(s1)]]
                else:
                    freqs2[s2[i-len(s1)]] -= 1
                freqs2[s2[i]] = freqs2.get(s2[i], 0) + 1
            print(freqs2)
            if freqs2 == freqs1:
                return True
        return False