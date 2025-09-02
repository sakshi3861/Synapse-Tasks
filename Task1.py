



from itertools import combinations

# Your Pokédex dictionary
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

def get_valid_integer(prompt):
    """Prompt until the user enters a valid integer."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def find_strongest_squads(pokedex, k):
    """
    Return the max unique types any squad of size k can cover,
    along with all squads that achieve that max.
    """
    max_types = 0
    strongest_squads = []

    for squad in combinations(pokedex.keys(), k):
        types_union = set()
        for mon in squad:
            types_union.update(pokedex[mon])
        type_count = len(types_union)

        if type_count > max_types:
            max_types = type_count
            strongest_squads = [(squad, types_union)]
        elif type_count == max_types:
            strongest_squads.append((squad, types_union))

    return max_types, strongest_squads

if __name__ == "__main__":
    total_pokemon = len(pokedex)
    print(f"You have {total_pokemon} Pokémon available.")

    # Prompt user for k until it is valid
    while True:
        k = get_valid_integer(f"Enter squad size k (1 to {total_pokemon}): ")
        if 1 <= k <= total_pokemon:
            break
        else:
            print(f"Please enter a number between 1 and {total_pokemon}.")

    max_types, squads = find_strongest_squads(pokedex, k)

    print(f"\nMaximum unique types for k = {k}: {max_types}\n")
    print("Strongest squad(s):")
    for squad, types in squads:
        print(f"  Squad: {', '.join(squad):40} → Types ({len(types)}): {', '.join(sorted(types))}")

