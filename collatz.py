try:
    print('input any number')
    num = int(input())

except ValueError:
    print("You must input integer value!")


def collatz(num):
    print(num)
    while num != 1:
        if num % 2 == 0:
            num = num // 2
        elif num % 2 == 1:
            num = num * 3 + 1
        else:
            print(1)
        return collatz(num)


collatz(num)
