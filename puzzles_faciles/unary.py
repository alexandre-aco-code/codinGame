import sys
# from itertools import groupby

DEBUG = True

def debug(*args):
    if DEBUG:
        print(*args, file=sys.stderr)

# result = ""

# message = input()
# debug("message",message)


# #1

# bin_message = ""

# for c in message :
#     # c_bin = bin(int.from_bytes(c.encode(), 'big'))
#     c_bin = bin(ord(c)) 
#     debug(c,"=> c_bin",c_bin)
#     bin_message += c_bin.replace('0b', '')

# debug("bin_message",bin_message)

# #2

# # bin = bin(ord(message))
# # debug("bin",bin)

# #3

# # test = bin(reduce(lambda x, y: 256*x+y, (ord(c) for c in message), 0))





# res = [''.join(g) for _, g in groupby(bin_message)]

# # debug("res", res)

# for c in res:

#     char = ""

#     if int(c[0]) == 1:
#         char = "0 " + "0" * len(c) + " "

#     elif int(c[0]) == 0:
#         char = "00 " + "0" * len(c) + " "

#     # debug("char",char)

#     result += char

# print(result[:-1])


#####################################


def to_binary(text) -> str:
    binary_text = ""
    for character in text:

        binary_element = bin(int.from_bytes(character.encode(), 'big')).replace("0b", "")
        # binary_element2 = "{0:{fill}7b}".format(ord(character), fill="0")
        binary_element2 = "{0:07b}".format(ord(character))
        # binary_element2 = "{0:07b}".format(ord(character))
        # binary_element2 = "{0:07x}".format(ord(character))
        debug(ord(character))

        debug(character,"=>",binary_element)
        debug(character,"=>",binary_element2)

        binary_text += binary_element2

    debug("binary_text",binary_text)
    return binary_text


def to_unary(text) -> str:
    unary_text = ""
    prev_digit = False  # False = 0, True = 1
    # handle first character
    if len(text) >= 1:
        if text[0] == "0":
            unary_text += "00 0"
        else:
            unary_text += "0 0"
            prev_digit = True

    for i in range(1, len(text)):
        if text[i] == "0" and prev_digit:
            unary_text += " 00 0"  # switch from 1 to 0
            prev_digit = False
        elif text[i] == "1" and not prev_digit:
            unary_text += " 0 0"  # switch from 0 to 1
            prev_digit = True
        else:
            unary_text += "0"  # repeat digit
    return unary_text


if __name__ == "__main__":
    text = input()
    debug(text)
    binary_text = to_binary(text)
    unary_text = to_unary(binary_text)
    print(unary_text)
