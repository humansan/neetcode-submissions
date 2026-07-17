class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
    
        # a = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

        prev2 = 0
        prev = 1
        cur = 0

        for i in range(len(s)-1, -1, -1):
            
            if i < len(s)-1 and 10 <= int(s[i:i+2]) <= 26:
                cur = prev2
            
            if s[i] != "0":
                cur += prev
            
            prev2, prev, cur = prev, cur, 0
        
        return prev