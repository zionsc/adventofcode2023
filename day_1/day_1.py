with open('input2.txt', 'r') as ifile:
    sum = 0
    digit_map = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    for line in ifile:
        for word, digit in digit_map.items():
            line = line.replace(word, digit)
        digits = [char for char in line if char.isdigit()]

        first = ""
        last = ""
        if digits:
            first = digits[0]
            last = digits[-1]
            sum += int(first + last)
        print(line)
        print(first, last)

print(sum)
