""" Récupération de toutes les attaques du Pokemon entré, et tri par ordre alphabétique"""

import json
import logging
import sys
import argparse

import requests
import jmespath


def parse_arguments(argument):
    """Nous demandons à ArgParser d'attendre la saisie d'un nom de Pokemon en entrée."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-p", "--pokemon", help="affiche le nom d'un pokemon", type=str, required=True
    )
    parser.add_argument(
        "-s",
        "--save-output",
        help="Prend le fichier json entré",
        type=str,
        required=False,
        dest="save_output",
    )
    return parser.parse_args(argument)


def appel_api(argument):
    """Nous prenons le lien à la page du bon pokemon, et vérifions si la connexion se fait."""
    url = "https://pokeapi.co/api/v2/pokemon/" + argument.pokemon
    try:
        logging.info("Nous récupérons les infos de ce Pokemon.")
        response = requests.get(url, timeout=20)
        pokemon_found = response.json()
        return pokemon_found
    except requests.exceptions.RequestException:
        logging.error("L'api ne semble pas fonctionner")
        sys.exit("Erreur de l'api")


def write_json(argument, pokemon_found):
    """Nous regardons si nous avons récupéré un paramètre pour le fichier Json"""
    if argument.save_output:
        future_json = get_moves_in_python(pokemon_found)
        with open(argument.save_output, "w", encoding="utf-8") as json_file:
            json.dump(future_json, json_file)
    else:
        print("Sorry guys!")


def get_moves_in_python(pokemon_found):
    """Nous récupérons le nom de toutes les attaques du dit pokemon, puis faisons
    une boucle pour rajouter les noms à la name_list"""
    moves = pokemon_found["moves"]
    final_list = []

    for move in moves:
        name_list = move["move"]
        final_list.append(name_list["name"])

    print(final_list)
    return sorted(final_list)


def get_moves_with_jmespath(pokemon_found):
    """Nous prenons le lien de l'API du bon Pokemon, puis nous demandons à Jmespath de
    prendre le noms de toutes ses attaques. Nous n'avons pas besoin de boucle."""
    search = "moves[*].move.name"
    return jmespath.search(search, pokemon_found)


def main():
    """ Main """
    logging.basicConfig(encoding="utf-8", level=logging.DEBUG)
    data = appel_api(parse_arguments(sys.argv[1:]))
    get_moves_in_python(data)
    get_moves_with_jmespath(data)
    write_json(parse_arguments(sys.argv[1:]), data)


if __name__ == "__main__":
    main()
