players = input()
zeroes = players.split('1')
ones = players.split('0')
result = False
for el in zeroes:
    if len(el) >= 7:
        result = True
        break
else:
    for el in ones:
        if len(el) >= 7:
            result = True
            break

if result:
    print('YES')
else:
    print('NO')


