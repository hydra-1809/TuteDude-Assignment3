def fact(n):
    factorial = 1

    if n == 1:
        return 1
    else:
        factorial=n*fact(n-1)
        return factorial

num=int(input("Enter a number:"))
result=fact(num)
print(f"Factorial of {num} is :{result}")


