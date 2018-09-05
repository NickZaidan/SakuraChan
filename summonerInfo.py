import requests
import json
import sys

def userExist(response):
    if response.status_code == 404:
        return False
    else:
        return True

def rankExist(response):
    checker = response.json()
    if not checker:
        return False
    else:
        return True


def requestSummonersData(region, name, key):
    URL = "https://" + region + ".api.riotgames.com/lol/summoner/v3/summoners/by-name/" + name + "?api_key=" + key
    response = requests.get(URL)
    if userExist(response)==True:
        return response.json()
    else:
        print("Summoner does not exist")
        exit()

def requestRankedData(region, id, key):
    URL = "https://" + region + ".api.riotgames.com/lol/league/v3/positions/by-summoner/" + id + "?api_key=" + key
    response = requests.get(URL)
    if rankExist(response)==True:
        return response.json()
    else:
        print("Summoner has no rank")
        exit()

def main():
    with open('api.txt') as f:
        mylist = [line.rstrip('\n') for line in f]
    apiKey = mylist[0]
    inputName = sys.argv[1]
    inputRegion = sys.argv[2]

    if inputRegion == "OCE" or inputRegion=="oce":
        inputRegion = "oc1"
    else:
        print("Not a compatible region")
        exit()

    responseJSON = requestSummonersData(inputRegion, inputName, apiKey)

    id = responseJSON['id']
    id = str(id)

    responseRankedJSON = requestRankedData(inputRegion, id, apiKey)

    summonerName = responseRankedJSON[0]['playerOrTeamName']
    summonerName = str(summonerName)

    leagueName = responseRankedJSON[0]['leagueName']
    leagueName = str(leagueName)

    tier = responseRankedJSON[0]['tier']
    tier = str(tier)
    tier = tier.title()

    rank = responseRankedJSON[0]['rank']
    rank = str(rank)
    if rank == "I":
        rank = "1"
    elif rank == "II":
        rank = "2"
    elif rank == "III":
        rank = "3"
    elif rank =="IV":
        rank = "4"
    elif rank == "V":
        rank = "5"

    leaguePoints = responseRankedJSON[0]['leaguePoints']
    leaguePoints = str(leaguePoints)
    printStatement = (summonerName + "\n" + leagueName + "\n" + tier + " " + rank + ": " + leaguePoints + " lp")
    print(printStatement)
    sys.stdout.flush()

main()
