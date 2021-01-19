#https://codeforces.com/problemset/problem/266/A
length = int(input())
colors = input()
removals = 0
for i in range(1,length):
    if colors[i] == colors[i-1]:
        removals += 1

print(removals)
