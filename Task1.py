



from itertools import combinations

# Pokédex: each Pokémon mapped to its types
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

def find_strongest_squads(k):
    max_types = 0
    best_squads = []

    # Loop through all squads of size k
    for squad in combinations(pokedex, k):
        # Collect all unique types in this squad
        types = set()
        for mon in squad:
            types.update(pokedex[mon])
        
        # Count the types
        tcount = len(types)
        
        # Update best squads
        if tcount > max_types:
            max_types = tcount
            best_squads = [(squad, types)]
        elif tcount == max_types:
            best_squads.append((squad, types))
    
    return max_types, best_squads

if __name__ == "__main__":
    n = len(pokedex)
    k = int(input(f"Enter squad size k (1 to {n}): "))
    
    max_types, squads = find_strongest_squads(k)
    
    print(f"\nStrongest squads of size {k} cover {max_types} unique types:")
    for squad, types in squads:
        print(f"• Squad: {', '.join(squad)} → Types ({len(types)}): {', '.join(sorted(types))}")


