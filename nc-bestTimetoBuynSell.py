arr=list(map(int, input().split()))
min_price=float('inf')
max_profit=0
for i in arr:
    min_price=min(i,min_price)
    profit=i-min_price
    max_profit=max(profit,max_profit)
print(max_profit)