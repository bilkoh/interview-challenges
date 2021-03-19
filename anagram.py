import timeit
import time

first_phrase = "Florida"
second_phrase = "rod fail"


def format_phrase(phrase):
    a = phrase.replace(" ", "")
    a = a.lower()
    return a


# first solution to checking anagram using lists
def list_solution(p1, p2):
    p1 = format_phrase(p1)
    p2 = format_phrase(p2)

    for x in list(p1):
        if p2.find(x) == -1:
            return False

    return True


# second solution to checking anagram using sort function
def sort_solution(p1, p2):
    p1 = format_phrase(p1)
    p2 = format_phrase(p2)

    return sorted(p1) == sorted(p2)


def anagram(first_phrase, second_phrase):
    # using sort soltuion because its a wee bit faster
    return sort_solution(first_phrase, second_phrase)


a = "Fourth of July"
b = "Joyful Fourth"
ret = anagram(a, b)
print("Is anagram?", ret)

# Uncomment &run the code below if you want to test between the two solutions
# my results were:
# sort speed: 0.0034900999999999405
# list speed: 0.004490499999999953


def sort_test():
    sort_solution(a, b)


def list_test():
    list_solution(a, b)


print("sort speed:", timeit.Timer(sort_test).timeit(number=1000))
print("list speed:", timeit.Timer(list_test).timeit(number=1000))

