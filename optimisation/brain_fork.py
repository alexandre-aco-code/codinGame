import sys
import math

DEBUG = True

# DEBUG

def debug(*args):
    if DEBUG:
        print(*args, file=sys.stderr)

# INPUTS

def get_data():
    return input()

# GENERAL

#return a nubmer between 1 and 26 which is the order of the letter
def get_letter_ord(s):
    return int(ord(s)-64)

def transform_caracter_to_instruction(c):
    order = get_letter_ord(c)
    choose_letter = ""
    if order > 13: 
        choose_letter = "-" * (27-order)
    #si negatif c'est que c'est un espace
    elif order < 0:
        choose_letter = ""
    #si positif on ajoute jusqu'a trouver la bonne lettre
    else:
        choose_letter = "+" * order
    return choose_letter

def get_last_identical_position(letter) :
    pos = 0
    for rune_pos, rune_let in runes.items():
        if rune_let == letter:
            pos = rune_pos
    return pos

# CODE

magic_phrase = get_data()
instructions = ""
prev_c = ""
rune_position = 1
runes = {}
tour = 0

for c in magic_phrase:

    tour += 1
    instruction = ""

    dif = 1000

    # on regarde l'écart avec la lettre du tour d'avant a partir du tour 2
    if tour >= 2 :
        dif = get_letter_ord(c) - get_letter_ord(prev_c)


    # peu d'écart avec la lettre d'avant
    if abs(dif) < 5 :
        if 0 < dif < 5:
            instruction += "+" * abs(dif) + "."
        elif -5 < dif < 0:
            instruction += "-" * abs(dif) + "."
        else : # cas ou les lettres sont IDENTIQUES
            instruction += "."

    # sinon on avance, et on trouve la lettre
    else :
        if tour == 1 :
            instruction += transform_caracter_to_instruction(c) + "."
        else :
            instruction += ">" + transform_caracter_to_instruction(c) + "."



    # rune_position += instruction.count(">")
    # rune_position -= instruction.count("<")

    # runes[rune_position] = c

    # debug(rune_position,"- letter:",c,"=>", instruction)
    debug("- letter:",c,"=>", instruction)

    #on ajoute l'instruction pour la lettre a tout le reste
    instructions += instruction

    #on save la lettre dans prev_c pour la boucle d'après
    prev_c = c


# debug("NUMBER OF INSTRUCTIONS :",len(instructions))

#pour valider, je dois faire moins de 6500 caractères de sortie
if(len(instructions) >= 6500):
    debug("TROP LONG ;) de :", 6500-len(instructions))

print(instructions)
