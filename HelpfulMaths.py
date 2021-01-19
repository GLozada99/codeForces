operation = input()
numbers = [int(num) for num in operation.split('+')]
numbers.sort()
numbers_string = [str(num) for num in numbers]
output = '+'.join(numbers_string)
print(output)
