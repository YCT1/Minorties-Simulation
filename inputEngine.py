import random


def checkCommand (a):
    nmb=0
    i = 0
    if "-" not in a:
        return "FAILED"
    while i<len(a):
        if a[i] == "-":
            nmb = i
        i += 1
    rtrnTxt = ""
    i = 0
    while i<nmb:
        rtrnTxt += a[i]
        i += 1
    return rtrnTxt


def checkNumber (a):
    nmb = 0
    i = 0
    if "-" not in a:
        return "FAILED"
    while i < len(a):
        if a[i] == "-":
            nmb = i
        i += 1
    rtrnTxt = [""]*3
    i = nmb+1
    b = 0
    while i < len(a):
        if a[i] == ",":
            b += 1
        else:
            rtrnTxt[b] += a[i]
        i += 1
    return rtrnTxt


class Men:
    def __init__(self,ishappy,race):
        self.ishappy = ishappy
        self.race = race

scene = []
randomit = random
while True:
    txt = input("Enter Your Command: ")
    command = checkCommand(txt)
    commandNum = checkNumber(txt)

    if command == "FAILED":
        print("You have entered wrong command ")
    if command == "exit":
        exit()
    if command == "gen":
        scene = [[0] * int(commandNum[0]) for _ in range(int(commandNum[1]))]
        i = 0
        while i < len(scene):
            satir = ""
            j = 0
            while j < len(scene[0]):
                scene[i][j] = "[" + commandNum[2] + "]"
                satir += scene[i][j]
                j += 1
            print(satir)
            i += 1

    if command == "test":
        print(commandNum[0])
    if command == "create":
        i = 1
        scene = [[0] * int(commandNum[0]) for _ in range(int(commandNum[1]))]
        while i < len(scene)-1:
            j = 1
            while j < len(scene[0])-1:
                a = randomit.randint(0, 5)
                if a < 3:
                    newman = Men(False, "o")
                    scene[i][j] = newman
                if a >= 3:
                    newman = Men(False, "Y")
                    scene[i][j] = newman
                j += 1
            i += 1
        myMen = scene

    if command == "render":
        i = 0
        while i < len(scene):
            row = ""
            j = 0
            while j < len(scene[1]):
                if scene[i][j] == 0:
                    row += "[ ]"
                else:
                    row += "[" + scene[i][j].race + "]"
                j += 1
            print(row)
            i += 1
    if command == "run":
        i = 0
        while i < int(commandNum[0]):
            x = 1
            while x < len(scene)-1:
                y = 1
                while y < len(scene[0])-1:
                    happymeter = 0
                    scene[x][y].ishappy = False
                    j = -1
                    while j < 2:
                        k = -1
                        while k < 2:
                            if scene[x+j][y+k] != 0:
                                if scene[x+j][y+k].race == scene[x][y].race:
                                    happymeter += 1
                            k += 1
                        j += 1
                    if happymeter > 3:
                        scene[x][y].ishappy = True
                    if scene[x][y].ishappy == False:
                        a = randomit.randint(1, len(scene)-2)
                        b = randomit.randint(1, len(scene[0])-2)
                        memory = scene[a][b]
                        scene[a][b] = scene[x][y]
                        scene[x][y] = memory
                    y += 1
                x += 1
            i += 1
