import requests

def pegar_habilidades(poke):
    nome = poke['name']
    forca = next((stat['base_stat'] for stat in poke['stats'] if stat['stat']['name'] == 'attack'), None)

    print(f"\nNome: {nome}")
    print(f"Força (Attack): {forca}")
    return nome, forca

#Nomes dos pokemons
nome_pokemon_1 = input("Digite o nome do primeiro pokemon: ").lower().strip()
nome_pokemon_2 = input("Digite o nome do segundo pokemon: ").lower().strip()

#Dados do pokemon 1
resposta_pokemon_1 = requests.get(f'https://pokeapi.co/api/v2/pokemon/{nome_pokemon_1}')
dados_pokemon_1 = resposta_pokemon_1.json()
nome_1_pokemon, forca_pokemon_1 = pegar_habilidades(dados_pokemon_1)

#Dados do pokemon 2
resposta_pokemon_2 = requests.get(f'https://pokeapi.co/api/v2/pokemon/{nome_pokemon_2}')
dados_pokemon_2 = resposta_pokemon_2.json()
nome_2_pokemon, forca_pokemon_2 = pegar_habilidades(dados_pokemon_2)


print("\nResultado da Batalha")
if forca_pokemon_1 > forca_pokemon_2:
    print(f"{nome_1_pokemon} venceu a batalha contra o {nome_2_pokemon}!")
elif forca_pokemon_2 > forca_pokemon_1:
    print(f"{nome_2_pokemon} venceu a batalha contra o {nome_1_pokemon}!")
else:
    print(f"A batalha terminou empatada entre {nome_1_pokemon} e {nome_2_pokemon}!")