#https://codeforces.com/problemset/problem/546/A
cost, money, bananas = [int(x) for x in input().split(' ')]
total_cost = cost * sum(range(1,bananas + 1))
money_borrow = total_cost - money
money_borrow = money_borrow if money_borrow >= 0 else 0
print(money_borrow)
