def fizz_buzz(n):
    for i in range(n):
        i = i + 1

        is_fizz = False
        is_buzz = False

        if (i % 3) == 0:
            is_fizz = True
        if (i % 5) == 0:
            is_buzz = True

        if is_fizz and is_buzz:
            print("FizzBuzz")
        elif is_fizz:
            print("Fizz")
        elif is_buzz:
            print("Buzz")
        else:
            print(i)


if __name__ == '__main__':
    n = 15
    fizz_buzz(n)
