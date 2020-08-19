import requests

def requestSummonorData(region, summonerName, APIKey):
    url = "https://" + region + ".api.pvp.net/api/lol/na/v4/summoner/by-name/" + summonerName + "?api_key=" + APIKey
    response = requests.get(url)
    return response.json()

def requestRankedData(region, ID, APIKey):
    url = "https://" + region + ".api.pvp.net/api/lol/na/v2.5/league/by-summoner/" + ID + "/entry?api_key=" + APIKey
    print(url)
    response = requests.get(url)
    return response.json()

APIKey = "RGAPI-e1239dcb-6450-45c3-b9e1-5fc465ebcdfb"

print(requestSummonorData("NA1", "PhilopThePanda", APIKey))

