def frequent_letter(words):
    letters = list(words.upper()) #capitalize everything and turns to list
    new_list = []

    for i in letters:
        if i.strip(): #removes whitespaces, if something is still there = True, if empty = False
            new_list.append(i)

    lettters = new_list
    common_letter = ''
    highest_count = 0

    for i in lettters:
        if lettters.count(i) > highest_count: #go through each letters inside list
            highest_count = lettters.count(i)
            common_letter = i

    return common_letter
print(frequent_letter("Hello World"))
