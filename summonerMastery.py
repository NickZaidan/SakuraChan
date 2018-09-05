import requests
import json
import sys

def userExist(response):
    if response.status_code == 404:
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

def requestChampionId(region, id, key):
    URL = "https://" + region + ".api.riotgames.com/lol/static-data/v3/champions" + id + "locale=en_US&api_key=" + key
    response = requests.get(URL)
    return response.json()

def requestMasteryList(region, id, key):
    URL = "https://" + region + ".api.riotgames.com/lol/champion-mastery/v3/champion-masteries/by-summoner/" + id + "?api_key=" + key
    response = requests.get(URL)
    if userExist(response)==True:
        return response.json()
    else:
        print("Summoner does not exist")
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

    responseMasteryJson = requestMasteryList(inputRegion, id, apiKey)
    print(responseMasteryJson)

main()
