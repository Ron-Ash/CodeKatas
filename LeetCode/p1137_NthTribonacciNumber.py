# The Tribonacci sequence Tn is defined as follows: 
# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
# Given n, return the value of Tn.

class Solution(object):
    Tribonacci = None
    def __init__(self):
        self.Tribonacci = {0:0, 1:1, 2:1}

    def tribonacci(self, n):
        if n < 0:
            return 1
        elif self.Tribonacci.get(n, None) == None:
            self.Tribonacci[n] = self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
        print(self.Tribonacci)
        return self.Tribonacci[n]

# O(n) time and O(n) space
