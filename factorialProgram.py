def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter a number: "))

if num < 0:
    print("Factorial of a negative number doesn't exist.")
else:
    print("Factorial of", num, "=", factorial(num))
