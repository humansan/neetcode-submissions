from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1
        
        heap = []
        
        for num in counts:
            heapq.heappush(heap, (-counts[num], num))
        
        results = []
        for i in range(k):
            neg_count, num  = heapq.heappop(heap)
            results.append(num)

        return results


        
        
