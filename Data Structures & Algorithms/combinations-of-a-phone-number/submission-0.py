class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        letters = [0, 0, "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        
        res = []
        cur = ""

        def backtrack(i):
            nonlocal cur
            if i == len(digits):
                res.append(cur)
                return
            
            for c in letters[int(digits[i])]:
                cur += c
                backtrack(i+1)
                cur = cur[:-1]
        
        backtrack(0)
        return res