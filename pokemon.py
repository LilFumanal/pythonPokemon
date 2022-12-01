from pprint import pprint
from urllib import response
import requests
import argparse


def parseArguments() :
    parser = argparse.ArgumentParser()
    parser.add_argument("-p","--pokemon", help="affiche le nom d'un pokemon", type = str)
    return parser.parse_args()

def getMoves(parsedPokemon):
    url = "https://pokeapi.co/api/v2/pokemon/"+ parsedPokemon.pokemon
    print(url)
    response = requests.get(url)
    dico = response.json()
    moves = dico["moves"]
    int = 0
    OriginalList = []

    for move in moves :
        move = moves[int]
        nameList = move["move"]
        OriginalList.append(nameList["name"])
        int += 1

    OriginalList.sort()
    print(OriginalList)

parsedPokemon = parseArguments()
print("parsed pokemon :" + parsedPokemon.pokemon)
getMoves(parsedPokemon)