def maxProfit(price):
        
        profit=0
        i=0
        size=len(price)
        
        while i<size:
            
            j=i+1
            value = price[i]-price[j]
            
            if value > profit:
                profit += value
                i+=1
                    
        return profit

prices=[10,22,5,75,65,80]
profit=maxProfit(prices)
print(f'Profit is {profit}')