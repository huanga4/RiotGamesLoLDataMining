import json

def cleanGameInfoJson():
    with open("gameInfo.txt") as gameInfoJson:
        gameInfoString = gameInfoJson.read()
        #print(gameInfoString[:100])
        gameInfoString = gameInfoString.replace('""', '')
        #print(gameInfoString)
        gameInfoString = gameInfoString[1:-2]
        gameInfoString = "[" + gameInfoString + "]"
        gameInfoString = gameInfoString.replace("'", "\"")
        gameInfoString = gameInfoString.replace("False,", "\"False\",")
        gameInfoString = gameInfoString.replace("True,", "\"True\",")

        #print(gameInfoString[32446:32451])

        newgame = open("fixedGameInfo.txt","w")
        newgame.write(gameInfoString)
        newgame.close()
        gameInfo = json.loads(gameInfoString)
        print(len(gameInfo))
        #data = json.load(open("gameinfosmallcopy.txt", "r"))
        #print(len(gameInfo))

def cleanGameTimeLineJson():
    with open("gameTimeline.txt") as gametljson:
        gametlString = gametljson.read()
        #print(gameInfoString[:100])
        gametlString = gametlString.replace('""', '')
        #print(gameInfoString)
        gametlString = gametlString[1:-2]
        gametlString = "[" + gametlString + "]"
        gametlString = gametlString.replace("'", "\"")
        gametlString = gametlString.replace("False,", "\"False\",")
        gametlString = gametlString.replace("True,", "\"True\",")

        #print(gametlString)

        newgame = open("fixedGameTimeline.txt", "w")
        newgame.write(gametlString)
        newgame.close()
        gametlInfo = json.loads(gametlString)
        print(len(gametlInfo))