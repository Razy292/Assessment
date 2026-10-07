def vowels_and_consonants(sentence):
    sentence = sentence.lower() #to avoid case sensitive
    vowels = 0
    consonants = 0

    for i in sentence:
        if i in "aeiou":
            vowels += 1
        elif i == " ":
            pass
        else:
            consonants += 1

    return str(vowels) + " Vowels and " + str(consonants) + " Consonants"

Input = "Hello my name is John Doe"
print(vowels_and_consonants(Input))