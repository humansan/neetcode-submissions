class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        
        # a = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

        counts = [0] * len(s)
        counts[0] = 1

        for i in range(1, len(s)):
            
            if 10 <= int(s[i-1:i+1]) <= 26:
                if i == 1:
                    counts[i] = 1
                else:
                    counts[i] = counts[i-2]
            if s[i] != "0":
                counts[i] += counts[i-1]
            # if a number is 10 or 20, counts should be i-2
            # if a number is 11-16, counts should be i-1 + i-2
            # if a number if 1-9 count should be i-1
        
        return counts[-1]