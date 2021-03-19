import re


def format_phrase(phrase):
    a = phrase
    a = a.casefold()  # replace lower() with casefold() to handle unicode.

    # This inelegant solution is commented out
    # a = a.replace(" ", "")
    # punctuation = [".", "!", "?", ",", ":"]
    # for x in punctuation:
    #     a = a.replace(x, "")

    # regex substitution is a better solution
    a = re.sub("[^a-z]+", "", a.casefold())

    return a


def reverse(phrase):
    return phrase[::-1]


def palindrome(phrase):
    phrase = format_phrase(phrase)
    return phrase == reverse(phrase)

