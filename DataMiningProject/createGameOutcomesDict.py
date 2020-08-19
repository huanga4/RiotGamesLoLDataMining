import json
# Getting all of the game information
with open("fixedGameInfo.txt") as gamesJson:
    gameInfo = json.load(gamesJson)
    print(gameInfo[5])
    #print(gameInfo[1]["participants"][0]["timeline"]["role"])
    #print(gameInfo[1]["participants"][0]["stats"]["perk0"])
    gameList = []
    for game in gameInfo:
        gameDict = {}
        teams = game['teams']
        gameDict['gameId'] = game["gameId"]
        for team in teams:
            try:
                if team['win'] == 'Win':
                    gameDict['winner'] = team['teamId']
            except:
                gameDict['winner'] = ""
        gameList.append(gameDict)
    print(gameList)
    # Save game outcomes
    gameOutcomes = open('gameOutcomes.txt', 'w')
    gameOutcomes.write(str(gameList))
    gameOutcomes.close()
