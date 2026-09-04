from collections import Counter, deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        # create counts of tasks
        # store in max heap
        # in each iteration, pop off heap, decrement, add to queue, move top of queue

        q = deque()
        max_heap = []

        counts = Counter(tasks)
        counts = {}
        for task in tasks:
            if task in counts:
                counts[task] += 1
            else:
                counts[task] = 1
        
        for value in counts.values():
            heapq.heappush(max_heap, -value)

        cycles = 0

        while max_heap or q:
            cycles += 1
            if max_heap:
                cur = heapq.heappop(max_heap)
                # pop from max heap
                # check if it's zero, and if it's greater, add to queue
                # check if the top of the queue is ready to be scheduled -> add to heap
                if cur + 1 < 0:
                    q.append((cur + 1, cycles + n))
            
            if q and q[0][1] <= cycles:
                move_to_heap = q.popleft()
                heapq.heappush(max_heap, move_to_heap[0])
        
        return cycles


        
