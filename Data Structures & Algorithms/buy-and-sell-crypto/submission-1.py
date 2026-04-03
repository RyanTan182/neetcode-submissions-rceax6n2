class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)):
            print("Chnaged I")
            for j in range(i+1, len(prices)):
                print("I price:", prices[i])
                print("J price:", prices[j])
                calculateProfit = prices[j] - prices[i]
                print("Profit Calculated:", calculateProfit)

                if profit < calculateProfit:
                    print("Yess")
                    profit = calculateProfit
                    print("Final profit so far:", profit)
        
        return profit
        