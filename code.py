s = int(input("Enter the start of range: "))
e = int(input("Enter the end of range: "))

print("All even numbers are :")
for i in range(s , e + 1):
    if i % 2 == 0:
        print(f'{i:2}' , end=' ')
print(' ')                

print("All odd numbers are :")
for i in range(s , e + 1):
    if i % 2 == 1:
        print(f'{i:2}' , end=' ')
