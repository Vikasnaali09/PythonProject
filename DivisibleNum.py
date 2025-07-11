
def Printing_num(start, end):
    for i in range(start, end + 1):
        if i%3 != 0 and i%5 != 0:
            print(i, end=" ")
start = int(input("start number: "))
end = int(input("end number: "))
result = Printing_num(start, end)
print(result, end = " ")