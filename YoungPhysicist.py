#https://codeforces.com/problemset/problem/69/A
number = int(input())
f_x = 0
f_y = 0
f_z = 0
for n in range(number):
    x,y,z = [int(num) for num in input().split(' ')]
    f_x += x
    f_y += y
    f_z += z

if f_x or f_y or f_z:
    print('NO')
else:
    print('YES')
