num, times = [int(x) for x in input().split(' ')]

for n in range(times):
    if num % 10 == 0:
        num //= 10
    else:
        num -= 1

print(num)
