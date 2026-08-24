class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # keep a set of characters representing the current window
        # constraint is that every window has no repeating characters
        # we move the right pointer and add character to set if that char doesn't exist
        # if char already exists, it means that we have a repeating character
        # we remove the char at left and move left rightward until the right char is gone
        # add right character to set

        l = 0
        longest_without_repeating = 0

        char_set = set()

        for r in range(len(s)):
            while s[r] in char_set:
                char_set.discard(s[l])
                l += 1

            char_set.add(s[r])
            longest_without_repeating = max(longest_without_repeating, r - l + 1)
        
        return longest_without_repeating

