def Fibonacci(n):
    sequence = [0, 1]

    if n < 0:
        return "Input must be a positive integer"
    elif n == 0:
        return []
    elif n == 1:
        return [0]

    for i in range(n - 2): # -2 because 2 digits are already in there
        x = sequence[i] + sequence[i + 1]
        sequence.append(x)
    return sequence

print(Fibonacci(13))