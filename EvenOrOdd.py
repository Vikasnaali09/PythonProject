def even_odd(num):
    if num % 2 ==0:
        return 'even'
    else:
        return 'odd'

n = int(input("enter a number: "))
result = even_odd(n)
print(result)