import string
from random import randint


def hello_func(arg):
    print("Hello, {0}!".format(arg))


def sum_of_array(arr):
    s = 1
    for i in arr:
        s += i
    return s


def multiply(arr):
    m = 1
    for i in arr:
        m *= i
    return m


def reverse(arg):
    str_rev = ""
    for i in arg[::-1]:
        str_rev += i
    return str_rev


def is_palindrom(arg):
    if arg == reverse(arg):
        return True
    return False


def histogram(arr):
    for i in arr:
        print("*" * i)


def caesar_cipher(arg, key):
    e_str = ""
    for i in arg:
        if not i.isalpha():
            e_str += i
        else:
            j = string.ascii_lowercase.index(i.lower())
            if j+key < 26:
                if i.isupper():
                    e_str += string.ascii_uppercase[j + key]
                else:
                    e_str += string.ascii_lowercase[j+key]
            else:
                if i.isupper():
                    e_str += string.ascii_uppercase[j + key-26]
                else:
                    e_str += string.ascii_lowercase[j+key-26]
    return e_str


def diagonal_reverse(matr):
    len_matr = len(matr)
    new_matr = []
    for i in range(len_matr):
        new_matr.append([])
        for j in range(len_matr):
            new_matr[i].append(matr[j][i])
    return new_matr


def game():
    a, b = 0, 3
    while True:
        if int(input("Input your digit from {0} to {1}: ".format(a, b))) == randint(a, b):
            print("Congratulation! You win!")
            break
        print("Try again!")


def brackets(arg):
    o_brackets = len(arg)/2
    c_brackets = len(arg)/2
    if arg[0] in ")}]":
        print("NOT OK")
    else:
        for i in arg:
            if i in "([{":
                o_brackets -= 1
            elif i in ")]}":
                c_brackets -= 1
            if c_brackets < o_brackets:
                print("NOT OK")
                break
        if o_brackets == 0 and c_brackets == 0:
            print("OK")


def char_freg(arg):
    container = {}
    for i in arg:
        if i not in container.keys():
            container[i] = 1
        else:
            container[i] += 1
    return container


def dec_to_bin(arg):
    print("{0:b}".format(arg))


if __name__ == "__main__":
    hello_func("DevOpd")
    print(sum_of_array([1, 2, 3, 4]))
    print(multiply([1, 2, 3, 4]))
    print(reverse("reverse"))
    print(is_palindrom("radar"))
    histogram([3, 7, 2])
    print(caesar_cipher("Test 12", 3))
    print(diagonal_reverse([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    game()
    brackets("[[]]")
    print(char_freg("aaacccbbb"))
    dec_to_bin(37)
