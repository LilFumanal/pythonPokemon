import collections
from pprint import pprint
import sys
from urllib import response
import requests
import argparse
import jmespath


# Nous demandons à ArgParser d'attendre la saisie d'un nom de Pokemon en entrée dans l'application.

def parseArguments() :
    parser = argparse.ArgumentParser()
    parser.add_argument("-p","--pokemon", help="affiche le nom d'un pokemon", type = str)
    return parser.parse_args()

#  Nous prenons le lien de l'API à la page du bon pokemon, et vérifions si la connexion se fait.

def appelApi(parsedPokemon) :
    url = "https://pokeapi.co/api/v2/pokemon/"+ parsedPokemon.pokemon
    try :
        response = requests.get(url)
        pokemonFound = response.json()
        return pokemonFound
    except :
        sys.exit("Erreur de l'api")


# Nous récupérons tout ce qui appartient à Pokemon.moves.[*].move.name, soit le nom de toutes les attaques du dit pokemon.

def getMovesInPython(pokemonFound):
    moves = pokemonFound["moves"]
    int = 0
    FinalList = []

    # Une fois dans la dite liste des attaques, c'est ici que nous faisons une boucle pour rajouter tous les noms à la nameList . 
    for move in moves :
        move = moves[int]
        nameList = move["move"]
        FinalList.append(nameList["name"])
        int += 1

    FinalList.sort()
    print(FinalList)


# Nous prenons le lien de l'API du bon Pokemon, puis nous demandons à Jmespath de prendre le noms de toutes ses attaques. Nous n'avons pas besoin de boucle.

def getMovesWithJmespath(pokemonFound):
    #Ici, on va créer une recherche et demander à jmespath de lancer cette recherche dans le dictionnaire de données pokemonFound, récupéré sur l'API au préalable.
    search = "moves[*].move.name"
    result = jmespath.search(search, pokemonFound)
    print(result)


# Appel de toutes les fonctions dans le bon ordre.

parsedPokemon = parseArguments()
getMovesInPython(appelApi(parsedPokemon))
getMovesWithJmespath(appelApi(parsedPokemon))