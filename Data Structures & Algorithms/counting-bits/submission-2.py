class Solution:
    def countBits(self, n: int) -> List[int]:

        dp = [0] * (n+1)
        cur = 1

        for i in range(1, n+1):
            if i==cur*2:
                cur=i

            dp[i] = 1 + dp[i-cur]
            
        return dp



