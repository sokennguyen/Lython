def collatz(number):
    if number % 2 == 0:
        number = number // 2
        print(number, end=', ')
        return number
    else:
        number = number * 3 + 1
        print(number, end=', ')
        return number


inpIsIncor = False

while inpIsIncor is not True:
    print('enter number:')
    global n
    n = int(input())
    if n < 1:
        continue
    inpIsIncor = True

print(n, end=', ')
while n != 1:
    n = collatz(n)
