def small_to_large(input):
    while True:
        changed_pos = False

        for i in range(len(input) - 1): #go through the list, -1 because exceed limit
            if input[i] > input[i+1]: #checks if next number bigger
                input[i], input[i+1] = input[i+1], input[i] #chage the position
                changed_pos = True

        if changed_pos == False: #if no changes then stop loo
            break

    return input


Input = [23, 7, 42, 19, 36, 12, 4, 45, 29, 31]
print(small_to_large(Input))

