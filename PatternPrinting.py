def print_sequence(n):
    for i in range(1, n+1):
        for j in range(i, n+1):
            print(j , end=' ')
            i = i + 1
        print()
try:
    n = int(input(" Enter the number :"))
    if n <= 0:
        print("Please enter a positive integer greater than 0")
    else:
        print_sequence(n)
except ValueError:
    print("Please enter a positive integer")



