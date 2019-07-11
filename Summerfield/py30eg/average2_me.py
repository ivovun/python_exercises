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

was_changed = True
count = 0
while was_changed:
    was_changed = False
    while True:
        if count < len(numbers) - 1:
            if numbers[count] > numbers[count + 1]:
                temp = numbers[count]
                numbers[count] = numbers[count + 1]
                numbers[count + 1] = temp
                was_changed = True
            count += 1
        else:
            count = 0
            break
if numbers:
    if len(numbers) / 2 == int(len(numbers) / 2):
        median = (numbers[int(len(numbers) / 2 - 1)] + numbers[int(len(numbers) / 2)]) / 2
    else:
        median = numbers[int(len(numbers) / 2)]

if numbers:
    print(f'median = {median}')
    print(f'numbers = {numbers}')

    print(f'count: {len(numbers)} lowest = {lowest}'
          f' sum = {total} highest = {highest}  mean = {total / len(numbers)} ')
