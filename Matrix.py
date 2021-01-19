lis = []
changes = 0
final_len = 5
for i in range(final_len):
    row = input('')
    lis.append(row)
    if row.count('1') == 1:
        position_x = len(lis) - 1
        distance_x = abs(position_x - final_len//2)
        position_y = row.split(' ').index('1')
        distance_y = abs(position_y - final_len//2)
        changes = distance_x + distance_y
print(changes)

