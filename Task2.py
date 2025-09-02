def earliest_step_to_form_lumos(runes: str) -> int:
    required = set("lumos")  # We need one of each: L, U, M, O, S
    seen = set()

    for index, ch in enumerate(runes, start=1):
        if ch.lower() in required:
            seen.add(ch.lower())
        # Check if we've collected all required runes
        if seen == required:
            return index
    return -1

if __name__ == "__main__":
    sequence = input("Enter the sequence of runes Hermione pulls (e.g., xLuZmOasL): ")
    result = earliest_step_to_form_lumos(sequence)

    if result != -1:
        print(f" Hermione can form 'LUMOS' by step {result}.")
    else:
        print(" She cannot form 'LUMOS' from the given runes.")
