import csv
import numpy as np
import json

def getRole(role, lane):
    if role == "SOLO":
        index = 1
    elif role == "DUO":
        index = 2
    elif role == "DUO_SUPPORT":
        index = 3
    elif role == "DUO_CARRY":
        index = 4
    elif role == "NONE" and lane == "JUNGLE":
        index = 1
    else:
        index = np.nan
    return index

def getLane(role, lane):
    if lane == "TOP":
        index = 1
    elif lane == "MIDDLE":
        index = 2
    elif lane == "BOTTOM":
        index = 3
    elif lane == "JUNGLE":
        index = 4
    #elif role == "DUO_SUPPORT" and lane == "NONE":
    #    index = 3
    #elif role == "DUO" and lane == "NONE":
    #    index = 3
    #elif role == "DUO_CARRY" and lane == "NONE":
    #    index = 3
    else:
        index = np.nan
    return index


def getTeam(participantId):
    if participantId > 5:
        return 2
    else:
        return 1


def saveToCSV(fileName, keyValueObjectList):
    keys = keyValueObjectList[0].keys()
    with open(fileName, 'w', encoding='utf8', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(keyValueObjectList)


def getGameOutcomes():
    with open("gameWinners.txt") as gamesJson:
        games = json.load(gamesJson)
        print(games[0])
        return games


def gameInfoCsv():
    # Getting all of the game information
    with open("fixedGameInfo.txt") as gamesJson:
        gameInfo = json.load(gamesJson)
        print(gameInfo[5])
        #print(gameInfo[1]["participants"][0]["timeline"]["role"])
        #print(gameInfo[1]["participants"][0]["stats"]["perk0"])
        gameList = []
        for game in gameInfo:
            gameDict = {}
            gameDict["gameId"] = game["gameId"]
            teams = game["teams"]
            for participant in game["participants"]:
                # Participant ID
                participantId = "participant_" + str(participant["participantId"])
                timeline = participant["timeline"]
                stats = participant["stats"]
                # Set up dictionary keys
                spell1 = participantId + "_spell1"
                spell2 = participantId + "_spell2"
                champion = participantId + "_champion"
                role = participantId + "_role"
                lane = participantId + "_lane"
                perk0 = participantId + "_perk0"
                perk0Var1 = participantId + "perk0Var1"
                perk0Var2 = participantId + "perk0Var2"
                perk0Var3 = participantId + "perk0Var3"
                perk1 = participantId + "_perk1"
                perk1Var1 = participantId + "perk1Var1"
                perk1Var2 = participantId + "perk1Var2"
                perk1Var3 = participantId + "perk1Var3"
                perk2 = participantId + "_perk2"
                perk2Var1 = participantId + "perk2Var1"
                perk2Var2 = participantId + "perk2Var2"
                perk2Var3 = participantId + "perk2Var3"
                perk3 = participantId
                perk3Var1 = participantId + "_perk3Var1"
                perk3Var2 = participantId + "_perk3Var2"
                perk3Var3 = participantId + "_perk3Var3"
                perk4 = participantId + "_perk4"
                perk4Var1 = participantId + "_perk4Var1"
                perk4Var2 = participantId + "_perk4Var2"
                perk4Var3 = participantId + "_perk4Var3"
                perk5 = participantId + "_perk5"
                perk5Var1 = participantId + "_perk5Var1"
                perk5Var2 = participantId + "_perk5Var2"
                perk5Var3 = participantId + "_perk5Var3"
                perkPrimaryStyle = participantId + "_perkPrimaryStyle"
                perkSubStyle = participantId + "_perkSubStyle"
                statPerk0 = participantId + "_statPerk0"
                statPerk1 = participantId + "_statPerk1 "
                statPerk2 = participantId + "_statPerk2"


                gameDict[spell1] = participant["spell1Id"]
                gameDict[spell2] = participant["spell1Id"]
                gameDict[champion] = participant["championId"]

                gameDict[role] = getRole(timeline["role"], timeline["lane"])
                gameDict[lane] = getLane(timeline["role"], timeline["lane"])
                try:
                    gameDict[perk0] = stats["perk0"]
                    gameDict[perk0Var1] = stats["perk0Var1"]
                    gameDict[perk0Var2] = stats["perk0Var2"]
                    gameDict[perk0Var3] = stats["perk0Var3"]
                    gameDict[perk1] = stats["perk1"]
                    gameDict[perk1Var1] = stats["perk1Var1"]
                    gameDict[perk1Var2] = stats["perk1Var2"]
                    gameDict[perk1Var3] = stats["perk1Var3"]
                    gameDict[perk2] = stats["perk2"]
                    gameDict[perk2Var1] = stats["perk2Var1"]
                    gameDict[perk2Var2] = stats["perk2Var2"]
                    gameDict[perk2Var3] = stats["perk2Var3"]
                    gameDict[perk3] = stats["perk3"]
                    gameDict[perk3Var1] = stats["perk3Var1"]
                    gameDict[perk3Var2] = stats["perk3Var2"]
                    gameDict[perk3Var3] = stats["perk3Var3"]
                    gameDict[perk4] = stats["perk4"]
                    gameDict[perk4Var1] = stats["perk4Var1"]
                    gameDict[perk4Var2] = stats["perk4Var2"]
                    gameDict[perk4Var3] = stats["perk4Var3"]
                    gameDict[perk5] = stats["perk5"]
                    gameDict[perk5Var1] = stats["perk5Var1"]
                    gameDict[perk5Var2] = stats["perk5Var2"]
                    gameDict[perk5Var3] = stats["perk5Var3"]
                except:
                    gameDict[perk0] = np.nan
                    gameDict[perk0Var1] = np.nan
                    gameDict[perk0Var2] = np.nan
                    gameDict[perk0Var3] = np.nan
                    gameDict[perk1] = np.nan
                    gameDict[perk1Var1] = np.nan
                    gameDict[perk1Var2] = np.nan
                    gameDict[perk1Var3] = np.nan
                    gameDict[perk2] = np.nan
                    gameDict[perk2Var1] = np.nan
                    gameDict[perk2Var2] = np.nan
                    gameDict[perk2Var3] = np.nan
                    gameDict[perk3] = np.nan
                    gameDict[perk3Var1] = np.nan
                    gameDict[perk3Var2] = np.nan
                    gameDict[perk3Var3] = np.nan
                    gameDict[perk4] = np.nan
                    gameDict[perk4Var1] = np.nan
                    gameDict[perk4Var2] = np.nan
                    gameDict[perk4Var3] = np.nan
                    gameDict[perk5] = np.nan
                    gameDict[perk5Var1] = np.nan
                    gameDict[perk5Var2] = np.nan
                    gameDict[perk5Var3] = np.nan
            for team in teams:
                try:
                    bans = team['bans']
                    teamId = "team_" + str(team['teamId'])
                    ban1 = teamId + "_ban1"
                    ban2 = teamId + "_ban2"
                    ban3 = teamId + "_ban3"
                    ban4 = teamId + "_ban4"
                    ban5 = teamId + "_ban5"

                    gameDict[ban1] = bans[0]['championId']
                    gameDict[ban2] = bans[1]['championId']
                    gameDict[ban3] = bans[2]['championId']
                    gameDict[ban4] = bans[3]['championId']
                    gameDict[ban5] = bans[4]['championId']
                except:
                    gameDict[ban1] = np.nan
                    gameDict[ban2] = np.nan
                    gameDict[ban3] = np.nan
                    gameDict[ban4] = np.nan
                    gameDict[ban5] = np.nan
            for team in teams:
                try:
                    if team['win'] == 'Win':
                        gameDict['winner'] = team['teamId']
                except:
                    team['win'] = ""
            gameList.append(gameDict)
        print(gameList[20])
        # Same game info CSV
        saveToCSV('gamesInfo.csv', gameList)


def timeLineCsv():
    # Getting all of the game timeline info
    with open("fixedGameTimeline.txt") as gamesJson:
        gameTimelines = json.load(gamesJson)
        gameOutcomes = getGameOutcomes()
        print(gameTimelines[0])
        #print(gameTimeline[1]["participants"][0]["timeline"]["role"])
        #print(gameTimeline[1]["participants"][0]["stats"]["perk0"])
        index = 0
        gameTimeLineList = []
        for gameTimeline in gameTimelines:
            #gameOutcome = gameOutcomes[index]
            frames = gameTimeline['frames']
            for frame in frames:
                gameDict = {}
                #gameDict['gameId'] = gameOutcome['gameId']
                #gameDict['winner'] = gameOutcome['winner']
                gameDict['timestamp'] = frame['timestamp']

                participantsFrames = frame['participantFrames']
                for key in participantsFrames:
                    participantsFrame = participantsFrames[key]
                    participantId = "participant_" + str(participantsFrame["participantId"])
                    x = participantId + "_x"
                    y = participantId + "_y"
                    currentGold = participantId + "_currentGold"
                    totalGold = participantId + "_totalGold"
                    level = participantId + "_level"
                    xp = participantId + "_xp"
                    minionsKilled = participantId + "_minionsKilled"
                    jungleMinionsKilled = participantId + "_jungleMinionsKilled"
                    dominionScore = participantId + "_dominionScore"
                    teamScore = participantId + "_teamScore"
                    team = participantId + "_team"
                    try:
                        gameDict[x] = participantsFrame['position']['x']
                        gameDict[y] = participantsFrame['position']['y']
                    except:
                        gameDict[x] = np.nan
                        gameDict[y] = np.nan

                    gameDict[currentGold] = participantsFrame['currentGold']
                    gameDict[totalGold] = participantsFrame['totalGold']
                    gameDict[level] = participantsFrame['level']
                    gameDict[xp] = participantsFrame['xp']
                    gameDict[minionsKilled] = participantsFrame['minionsKilled']
                    gameDict[jungleMinionsKilled] = participantsFrame['jungleMinionsKilled']
                    gameDict[team] = getTeam(participantsFrame["participantId"])
                    try:
                        gameDict[dominionScore] = participantsFrame['dominionScore']
                    except:
                        gameDict[dominionScore] = np.nan
                    try:
                        gameDict[teamScore] = participantsFrame['teamScore']
                    except:
                        gameDict[teamScore] = np.nan

                gameTimeLineList.append(gameDict)
            index += 1
        # Save game timeline CSV
        saveToCSV('gamesTimelineTeam.csv', gameTimeLineList)


def gameTimelineTeams():
    # Getting all of the game timeline info
    with open("fixedGameTimeline.txt") as gamesJson:
        gameTimelines = json.load(gamesJson)
        gameOutcomes = getGameOutcomes()
        print(gameTimelines[0])
        #print(gameTimeline[1]["participants"][0]["timeline"]["role"])
        #print(gameTimeline[1]["participants"][0]["stats"]["perk0"])
        index = 0
        gameTimeLineList = []
        for gameTimeline in gameTimelines:
            #gameOutcome = gameOutcomes[index]
            frames = gameTimeline['frames']
            for frame in frames:

                participantsFrames = frame['participantFrames']
                for key in participantsFrames:
                    gameDict = {}
                    gameDict['timestamp'] = frame['timestamp']

                    participantsFrame = participantsFrames[key]
                    participantId = participantsFrame["participantId"]
                    gameDict["participantId"] = participantId
                    gameDict['team'] = getTeam(participantId)


                    try:
                        gameDict["x"] = participantsFrame['position']['x']
                        gameDict["y"] = participantsFrame['position']['y']
                    except:
                        gameDict["x"] = np.nan
                        gameDict["y"] = np.nan

                    gameDict["currentGold"] = participantsFrame['currentGold']
                    gameDict["totalGold"] = participantsFrame['totalGold']
                    gameDict["level"] = participantsFrame['level']
                    gameDict["xp"] = participantsFrame['xp']
                    gameDict["minionsKilled"] = participantsFrame['minionsKilled']
                    gameDict["jungleMinionsKilled"] = participantsFrame['jungleMinionsKilled']
                    try:
                        gameDict["dominionScore"] = participantsFrame['dominionScore']
                    except:
                        gameDict["dominionScore"] = np.nan
                    try:
                        gameDict["teamScore"] = participantsFrame['teamScore']
                    except:
                        gameDict["teamScore"] = np.nan

                    gameTimeLineList.append(gameDict)
            index += 1
        # Save game timeline CSV
        saveToCSV('gamesTimelineV2Team.csv', gameTimeLineList)
