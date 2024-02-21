
def calculate_fibonacci(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    return calculate_fibonacci(num-1) + calculate_fibonacci(num-2)

fibonacci_result = calculate_fibonacci(5)
print(fibonacci_result)