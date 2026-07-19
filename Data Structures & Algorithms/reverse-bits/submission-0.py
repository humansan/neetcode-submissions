class Solution:
    def reverseBits(self, n: int) -> int:
        build = 0

        for i in range(31):

            build += n & 1
            
            n >>= 1

            build <<= 1
    
        build += n & 1
        
        return build