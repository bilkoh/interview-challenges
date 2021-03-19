def fizz_buzz(start, end):
    ret = list()
    for x in range(start, end + 1):
        res = str(x)
        is_divisible_by_three = x % 3 == 0
        is_divisible_by_five = x % 5 == 0
        if is_divisible_by_three & is_divisible_by_five:
            res = "FizzBuzz"
        elif is_divisible_by_three:
            res = "Fizz"
        elif is_divisible_by_five:
            res = "Buzz"

        ret.append(res)
    return ret


# Modulo operator: It performs integer division, but instead of giving you
# the quotient (the result of a division), it gives you the remainder.

print(fizz_buzz(1, 100))

