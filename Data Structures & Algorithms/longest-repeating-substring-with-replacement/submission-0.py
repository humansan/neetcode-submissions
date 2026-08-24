class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # keep l/r substring pointers
        # iterate right pointer and keep count of characters in a map
        # every time a character is incremented, check if that's the new most common (keep a most common counter) by checking count map
        # if length of substring - most common is up to k, check if max window
        # after a max window is set, we don't need to check smaller windows (which k + max_freq does)
            # most common will go stale but doesn't matter, we just need to keep char counts map true
            # if the k constraint becomes invalid, move l rightward until window is as large as max window

        
        l = 0
        char_map = defaultdict(int)
        max_freq = 0
        longest = 0

        for r in range(len(s)):

            char_map[s[r]] += 1
            max_freq = max(max_freq, char_map[s[r]])

            while (r - l + 1) - max_freq > k:
                char_map[s[l]] -= 1
                l += 1
            
            longest = max(longest, r - l + 1)
        
        return longest
            

        