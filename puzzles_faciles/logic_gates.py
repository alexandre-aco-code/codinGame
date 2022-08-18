import sys
import math

DEBUG = True
TRUE = "-"
FALSE = "_"

def debug(*args):
    if DEBUG :
        print(*args, file=sys.stderr)

signals = {}

## inputs 

n = int(input())
m = int(input())

for i in range(n):
    input_name, input_signal = input().split()
    signals[input_name] = input_signal

# debug(signals)

for i in range(m):
    output_name, _type, input_name_1, input_name_2 = input().split()

    debug(output_name, _type, input_name_1, input_name_2)

    sig1 = signals[input_name_1]
    sig2 = signals[input_name_2]
    sig3 = ''

    length = range(len(sig1))

    debug(input_name_1, sig1)
    debug(input_name_2, sig2)


    if _type == "AND":

        for j in length :
            if sig1[j] == TRUE and sig2[j] == TRUE :
                sig3 += TRUE
            else :
                sig3 += FALSE

    elif _type == "OR" :

        for j in length :
            if sig1[j] == TRUE or sig2[j] == TRUE :
                sig3 += TRUE
            else :
                sig3 += FALSE

    elif _type == "XOR" :

        for j in length :
            if sig1[j] == TRUE and sig2[j] == FALSE or sig1[j] == FALSE and sig2[j] == TRUE :
                sig3 += TRUE
            else :
                sig3 += FALSE

                
    elif _type == "NAND" :

        for j in length :
            if not (sig1[j] == TRUE and sig2[j] == TRUE) :
                sig3 += TRUE
            else :
                sig3 += FALSE

                
    elif _type == "NOR" :

        for j in length :
            if sig1[j] == FALSE and sig2[j] == FALSE :
                sig3 += TRUE
            else :
                sig3 += FALSE


    elif _type == "NXOR" :

        for j in length :
            if sig1[j] == TRUE and sig2[j] == TRUE or sig1[j] == FALSE and sig2[j] == FALSE :
                sig3 += TRUE
            else :
                sig3 += FALSE

    # debug(output_name, sig3)

    print(output_name, sig3)
