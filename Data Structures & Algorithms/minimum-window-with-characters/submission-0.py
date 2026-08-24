class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # count chars in t, and create a total need
        # use l/r substring pointer for s
        # iterate right pointer, decrementing need and counts if char in counts for t
        # when need becomes 0, start moving left rightard
            # increment chars that are t counts, and increment need if the need for that char becomes positive
            # 

        min_window = None
        
        counts = defaultdict(int)
        need = 0
        for char in t:
            counts[char] += 1
            need += 1
        
        l = 0

        for r in range(len(s)):
            
            if s[r] in counts:
                if counts[s[r]] > 0:
                    need -= 1
                counts[s[r]] -= 1
            

            while need == 0:
                if not min_window or r - l < (min_window[1] - min_window[0]):
                    min_window = (l, r)

                if s[l] in counts:
                    counts[s[l]] += 1
                    if counts[s[l]] > 0:
                        need += 1
                
                l += 1
        
        if min_window:
            return s[min_window[0]:min_window[1]+1]
        return ""

                
                
                
            
