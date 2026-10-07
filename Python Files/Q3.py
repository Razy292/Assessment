def Prime_numbers(n):
    if n < 0:
        return "Input must be a positive integer"
    elif n == 0:
        return []

    number_list = [2]
    count = 3

    while len(number_list) < n:
        divisible = 0

        for i in range(2, count): #from 2 to count-1, as 1 and the number itself will always % = 0
            if count % i == 0: #if any numbers divides evenly
                divisible += 1

        if divisible == 0:
            number_list.append(count)

        count += 1

    return number_list

Input = 10
print(Prime_numbers(Input))