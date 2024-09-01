def calculate_factorial(n):
    if n > 0:
        product = 1
        for num in range(1,n+1):
            product *= num
        return product
    elif n == 0 or n == 1:
        return 1
    else:
        return "Invalid input. Please enter a non-negative integer."