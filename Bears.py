#https://codeforces.com/problemset/problem/791/A
limark, bob = [int(x) for x in input().split(' ')]
years = 0
while bob >= limark:
    limark *= 3
    bob *= 2
    years += 1

print(years)
