#https://codeforces.com/problemset/problem/236/A
text = input()
chars = set(text)
if len(chars) % 2 == 0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')
