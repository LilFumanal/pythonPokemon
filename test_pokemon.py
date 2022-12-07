import pytest
import pokemon


def test_parse_arguments():
    pokemon_arguments = pokemon.parse_arguments(["-p", "pikachu"])
    assert pokemon_arguments.pokemon == "pikachu"
    assert not pokemon_arguments.save_output
    json_arguments = pokemon.parse_arguments(["-p", "pikachu", "-s", "pikachu.json"])
    assert pokemon_arguments.pokemon
    assert json_arguments.save_output == "pikachu.json"


def test_get_moves_in_python():
    pokemon_found = {
        "moves": [{"move": {"name": "Vive attaque"}},
            {"move": {"name": "Coup de pied"}}
        ]
    }
    assert pokemon.get_moves_in_python(pokemon_found) == [
        "Coup de pied",
        "Vive attaque",
    ]

def test_get_moves_in_python_without_moves():
    pokemon_without_moves = { "moves" : []}
    assert pokemon.get_moves_in_python(pokemon_without_moves) == []


def get_label(maisons: dict):
    return maisons["murs"]


def test_get_label():
    maisons = {"murs": "jaune"}
    assert get_label(maisons) == "jaune"
