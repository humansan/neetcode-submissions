class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dp = [False] * (len(s) + 1)
        dp[0] = True
        
        for i in range(len(s)):
            if dp[i]:
                for word in wordDict:
                    l = len(word)

                    if i+l <= len(s) and s[i:i+l] == word:
                        dp[i+l] = True
        
        return dp[len(s)]