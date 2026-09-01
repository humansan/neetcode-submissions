class Solution:
    def isHappy(self, n: int) -> bool:

        current_number = n
        stored = set()

        while True:
            if current_number == 1:
                return True
            if current_number in stored:
                return False
            
            stored.add(current_number)
            current_number = self.sumSquareDigits(current_number)



    
    def sumSquareDigits(self, n):
        sum = 0
        while n:
            sum += pow(n % 10, 2)
            n //= 10
        return sum