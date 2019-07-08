lowest = None
highest = None
mean = 0
numbers = []
total = 0
while True:
    line = input("enter a number or Enter to finish: ")
    if not line:
        break
    try:
        number = int(line)
        numbers.append(number)
        total += number
        if lowest is None or number < lowest:
            lowest = number
        if highest is None or number > highest:
            highest = number
    except ValueError as err:
        print(err)


print(f'numbers = {numbers}')
if numbers:
    print(f'count: {len(numbers)} lowest = {lowest}'
          f' sum = {total} highest = {highest}  mean = {total / len(numbers)} ')
