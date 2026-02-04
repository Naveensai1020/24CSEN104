
def recursive_factorial(n):
    if n == 0:
        return 1
    else:
        return n * recursive_factorial(n - 1)  # n! = n * (n-1)! [web:31][web:35]

number = int(input("Enter a non-negative number: "))

factorial_number = 1

if number < 0:
    print("Entered a negative number. Factorial cannot be determined")
else:
    for i in range(1, number + 1):   # loop from 1 to number inclusive [web:38][web:42]
        factorial_number *= i
    print(f"Factorial of {number} is {factorial_number}")

    # recursive method
    print(f"\nUsing recursive method Factorial of {number} is {recursive_factorial(number)}")

# OUTPUT

Enter a non-negative number: 45
Factorial of 45 is 119622220865480194561963161495657715064383733760000000000

Using recursive method Factorial of 45 is 119622220865480194561963161495657715064383733760000000000

=== Code Execution Successful ===
