def factorize():
    num = int(input("Input a positive integer: "))
    print("Factors:")
    while num % 2 == 0:
        print("2")
        num = num / 2
    for i in range(3, int(num ** .5) + 1, 2):
        if num % i == 0:
            print(i)
            num = num / i
    if num > 2:
        print(int(num))
    cont = input("Continue (y/n)? ")
    while cont == "y":
        num = int(input("Input a positive integer: "))
        print("Factors:")
        while num % 2 == 0:
            print("2")
            num = num / 2
        for i in range(3, int(num ** .5) + 1, 2):
            if num % i == 0:
                print(i)
                num = num / i
        if num > 2:
            print(int(num))
        cont = input("Continue (y/n)? ")
