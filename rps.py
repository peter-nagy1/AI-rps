import random
from datetime import date

history = [] # [User input, Ai input, User won(T/F)]
userScore = 0
aiScore = 0
SCORE_LIMIT = 5
strategies = [1, 1, 1, 1, 1, 1]
# 6 possible strategies: Win-Same, Win-Opposite, Win-Other, Loss-Same, Loss-Opposite, Loss-Other

f = open("data.txt", "a")
f.write("Date: " + str(date.today()))


def updateStrategies(userInput):
    WEIGHT = 3
    LIGHT_WEIGHT = 1
    if history[-1][2]:
        if history[-1][0] == userInput:
            strategies[0] += WEIGHT
            strategies[1] -= LIGHT_WEIGHT
            strategies[2] -= LIGHT_WEIGHT
        elif history[-1][1] == userInput:
            strategies[1] += WEIGHT
            strategies[0] -= LIGHT_WEIGHT
            strategies[2] -= LIGHT_WEIGHT
        else:
            strategies[2] += WEIGHT
            strategies[0] -= LIGHT_WEIGHT
            strategies[1] -= LIGHT_WEIGHT
    else:
        if history[-1][0] == userInput:
            strategies[3] += WEIGHT
            strategies[4] -= LIGHT_WEIGHT
            strategies[5] -= LIGHT_WEIGHT
        elif history[-1][1] == userInput:
            strategies[4] += WEIGHT
            strategies[3] -= LIGHT_WEIGHT
            strategies[5] -= LIGHT_WEIGHT
        else:
            strategies[5] += WEIGHT
            strategies[3] -= LIGHT_WEIGHT
            strategies[4] -= LIGHT_WEIGHT

    for i in range(len(strategies)):
        if strategies[i] < 1:
            strategies[i] = 1

def getStrategy():
    hat = []
    if history[-1][2]:
        for i in range(3):
            for _ in range(strategies[i]):
                hat.append(i)
    else:
        for i in range(3, 6):
            for _ in range(strategies[i]):
                hat.append(i)

    return random.choice(hat)

def getOpposite(choice):
    if choice == 'r':
        return 'p'
    if choice == 'p':
        return 's'
    if choice == 's':
        return 'r'

def aiPlay():
    if len(history) > 0:
        strategy = getStrategy()

        if strategy == 0:
            return getOpposite(history[-1][0])
        if strategy == 1:
            return history[-1][0]
        if strategy == 2:
            return history[-1][1]
        if strategy == 3:
            return history[-1][1]
        if strategy == 4:
            return getOpposite(history[-1][1])
        if strategy == 5:
            return history[-1][0]
            
    else:
        return random.choice(['r', 'p', 's'])
    
def result(input1, input2):
    if (input1 == 'r' and input2 == 'p') or (input1 == 'p' and input2 == 'r'):
        return 'p'
    if (input1 == 'r' and input2 == 's') or (input1 == 's' and input2 == 'r'):
        return 'r'
    if (input1 == 'p' and input2 == 's') or (input1 == 's' and input2 == 'p'):
        return 's'
    return None


while not (userScore == SCORE_LIMIT or aiScore == SCORE_LIMIT):

    userInput = ''
    while not (userInput == 'r' or userInput == 'p' or userInput == 's' or userInput == 'q'):
        userInput = input("Play r-p-s: ")
    if userInput == 'q':
        quit()

    aiInput = aiPlay()
    print("AI plays:", aiInput)
    

    if len(history) > 0:
        updateStrategies(userInput) # After the AI chose

    f.write("\n" + str(strategies))

    if result(userInput, aiInput) == userInput:
        print("WIN")
        userScore += 1
        history.append([userInput, aiInput, True])
            
    elif result(userInput, aiInput) == aiInput:
        print("LOSS")
        aiScore += 1
        history.append([userInput, aiInput, False])
    else:
        print("DRAW")

    print("(USER)", userScore, "-", aiScore, "(AI)")

f.write("\n\n")