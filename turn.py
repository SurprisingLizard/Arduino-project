import re

base_notes = {
    '1': ('C', 4),
    '2': ('D', 4),
    '3': ('E', 4),
    '4': ('F', 4),
    '5': ('G', 4),
    '6': ('A', 4),
    '7': ('B', 4),
    '0': ('REST', None),
}

sharp_map = {
    'C': 'CS',
    'D': 'DS',
    'E': 'E',
    'F': 'FS',
    'G': 'GS',
    'A': 'AS',
    'B': 'B',
}

def apply_sharp(note, octave):
    if note == 'REST':
        return note, octave

    if the_sharp := sharp_map.get(note):
        if note == 'E':
            return 'F', octave
        if note == 'B':
            return 'C', octave + 1
        return the_sharp, octave

    return note, octave

def convert_token(token):
    m = re.findall(r'(#+)?([0-7])([+]+)?', token)
    if not m:
        return []

    results = []
    for sharp_signs, digit, oct_signs in m:
        base_note, base_oct = base_notes[digit]

        if base_note == 'REST':
            results.append("REST")
            continue

        octave = base_oct + (len(oct_signs) if oct_signs else 0)

        if sharp_signs:
            for _ in range(len(sharp_signs)):
                base_note, octave = apply_sharp(base_note, octave)

        results.append(f"{base_note}{octave}")

    return results

def convert_string(s):
    tokens = re.findall(r'[#+0-7]+', s)

    output = []
    for t in tokens:
        output.extend(convert_token(t))
    return output

def format_single_line(demo):
    return ",".join(convert_string(demo)) + ","

with open("02.txt", "r", encoding="utf-8") as f:
    content = f.read()
    
print(format_single_line(content))
