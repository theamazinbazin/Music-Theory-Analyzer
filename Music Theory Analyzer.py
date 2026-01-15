# Define the notes of the chromatic scale
CHROMATIC_SHARPS = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

CHROMATIC_FLATS = ["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"]

SCALE_INTERVALS = {
    "major": [0, 2, 4, 5, 7, 9, 11],
    "minor": [0, 2, 3, 5, 7, 8, 10],
}

FLAT_TONICS = {
    "F", "Bb", "Eb", "Ab", "Db", "Gb", "D", "G", "C", "F", "Bb", "Eb", "Ab"
}

def get_chromatic_scale(key, scale_type):
    flat_major_keys = {"F", "Bb", "Eb", "Ab", "Db", "Gb", "Cb"}
    flat_minor_keys = {"C", "F", "Bb", "Eb", "Ab"}

    if scale_type == "minor" and key in {"C", "F", "Bb", "Eb", "Ab"}:
        return CHROMATIC_FLATS
    if scale_type == "major" and key in {"F", "Bb", "Eb", "Ab", "Db", "Gb"}:
        return CHROMATIC_FLATS
    
    return CHROMATIC_SHARPS

def build_scale (key, scale_type):
    chromatic = get_chromatic_scale(key, scale_type)
    root_index = chromatic.index(key)

    return [
        chromatic[(root_index + interval) % 12]
        for interval in SCALE_INTERVALS[scale_type]
    ]

def interval(chromatic, root, note):
    return (chromatic.index(note) - chromatic.index(root)) % 12

def to_roman(n):
    return ["I", "II", "III", "IV", "V", "VI", "VII"][n - 1]

def analyze_triad(scale, chromatic, degree):
    root = scale[degree]
    third = scale[(degree + 2) % 7]
    fifth = scale[(degree + 4) % 7]

    i3 = interval(chromatic, root, third)
    i5 = interval(chromatic, root, fifth)

    numeral = to_roman(degree + 1)

    if i3 == 4 and i5 == 7:
        quality = "major"
        numeral = numeral.upper()
    elif i3 == 3 and i5 == 7:
        quality = "minor"
        numeral = numeral.lower()
    elif i3 == 3 and i5 == 6:
        quality = "diminished"
        numeral = numeral.lower() + "°"
    else:
        quality = "unknown"
    
    return numeral, root, quality, [root, third, fifth]

def analyze_key(key, scale_type):
    chromatic = get_chromatic_scale(key, scale_type)
    scale = build_scale(key, scale_type)

    print(f"\nChords in {key} {scale_type.title()}:\n")

    for degree in range(7):
        numeral, root, quality, notes = analyze_triad(scale, chromatic, degree)
        print(f"{numeral}: {root} {quality} → {', '.join(notes)}")


if __name__ == "__main__":
    user_input = input("Enter a key: ").strip()
    key, scale_type = user_input.split()

    analyze_key(key, scale_type.lower())