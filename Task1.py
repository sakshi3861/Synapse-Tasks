from itertools import combinations

# Your Pokédex
pokedex = {
    'Pikachu': ('Electric',),
    'Charizard': ('Fire', 'Flying'),
    'Lapras': ('Water', 'Ice'),
    'Machamp': ('Fighting',),
    'Mewtwo': ('Psychic', 'Fighting'),
    'Hoopa': ('Psychic', 'Ghost', 'Dark'),
    'Lugia': ('Psychic', 'Flying', 'Water'),
    'Squirtle': ('Water',),
    'Gengar': ('Ghost', 'Poison'),
    'Onix': ('Rock', 'Ground')
}

def find_strongest_squads(pokedex, k):
    max_types = 0
    strongest_squads = []

    for squad in combinations(pokedex.keys(), k):
        combined_types = set()
        for mon in squad:
            combined_types.update(pokedex[mon])

        type_count = len(combined_types)

        if type_count > max_types:
            max_types = type_count
            strongest_squads = [(squad, combined_types)]
        elif type_count == max_types:
            strongest_squads.append((squad, combined_types))

    return max_types, strongest_squads

# Example: k = 3
k = 3
max_types, squads = find_strongest_squads(pokedex, k)

print(f"Maximum unique types covered by any {k}-Pokémon squad: {max_types}\n")
print("Strongest squads:")
for squad, types in squads:
    print(f"  Squad: {', '.join(squad):40} → Types ({len(types)}): {', '.join(sorted(types))}")
