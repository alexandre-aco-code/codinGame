import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
cardp1 = []
cardp2 = []

n = int(input())  # the number of cards for player 1
for i in range(n):
    cardp_1 = input()  # the n cards of player 1
    cardp1.append(cardp_1)

m = int(input())  # the number of cards for player 2
for i in range(m):
    cardp_2 = input()  # the m cards of player 2
    cardp2.append(cardp_2)



# Write an answer using print


def getValue(card):
    if card[:2] == "10":
        value=10
    elif card[:1] == "A":
        value=14
    elif card[:1] == "K":
        value=13
    elif card[:1] == "Q":
        value=12
    elif card[:1] == "J":
        value=11
    else :
        value=int(card[:1])
    return value

winner = 0
counter = 0
Pat = False

#print("### INITIAL ###")

#print("cardp1",cardp1) #deck p1
#print("cardp2",cardp2) #deck p2

while ( len(cardp1) != 0 or len(cardp2) != 0 ) :

    value1 = getValue(cardp1[0])
    value2 = getValue(cardp2[0])

    counter = counter+1

    #print("TOUR",counter) #tour counter
    #print("value1", value1)
    #print("value2", value2)

    pilep1 = []
    pilep2 = []

    if value1 > value2: #P1 WINS ROUND

        cardp1.append(cardp1[0])
        cardp1.append(cardp2[0])
        cardp1.pop(0)
        cardp2.pop(0)

    elif value1 < value2 : #P2 WINS ROUND

        cardp2.append(cardp1[0])
        cardp2.append(cardp2[0])
        cardp1.pop(0)
        cardp2.pop(0)

    elif value1 == value2 : #BATAILLE

        while value1 == value2 : #BATAILLE OF BATAILLE

            pilep1.extend(cardp1[:4])
            pilep2.extend(cardp2[:4])

            cardp1 = cardp1[4:]
            cardp2 = cardp2[4:]

            if len(cardp1) == 0 or len(cardp2) == 0 :
                Pat = True
                break
            else :
                value1 = getValue(cardp1[0])
                value2 = getValue(cardp2[0])


        if value1 > value2 :

            pilep1.append(cardp1[0])
            pilep2.append(cardp2[0])

            cardp1.extend(pilep1+pilep2)

            cardp1 = cardp1[1:]
            cardp2 = cardp2[1:]

            #print("fin de bataille cardp1",cardp1) #deck p1
            #print("fin de bataille cardp2",cardp2) #deck p2

        if value1 < value2:

            pilep1.append(cardp1[0])
            pilep2.append(cardp2[0])

            cardp2.extend(pilep1+pilep2)

            cardp1 = cardp1[1:]
            cardp2 = cardp2[1:]

            #print("fin de bataille cardp1",cardp1) #deck p1
            #print("fin de bataille cardp2",cardp2) #deck p2


    #print("cardp1",cardp1) #deck p1
    #print("cardp2",cardp2) #deck p2

    #GAGNANT
    if len(cardp1) == 0:
        winner = 2
        break
    elif len(cardp2) == 0:
        winner = 1
        break

    #print('########FIN DE TOUR#############')


if Pat == True:
    print("PAT")
else :
    print(winner, counter)
    

print("Debug messages...", file=sys.stderr, flush=True)

