def get_soundex_code(char):
    char = char.upper()
    mapping = {
        'B': '1', 'F': '1', 'P': '1', 'V': '1',
        'C': '2', 'G': '2', 'J': '2', 'K': '2', 'Q': '2', 'S': '2', 'X': '2', 'Z': '2',
        'D': '3', 'T': '3',
        'L': '4',
        'M': '5', 'N': '5',
        'R': '6'
    }
    # Return the corresponding number or '0' for vowels and other characters not in the mapping
    return mapping.get(char, '0')

def comparison(ch, prev_code):
    # Return the current code only if it's not '0' and different from the previous code
    if ch != '0' and ch != prev_code:
        return ch
    else:
        return ""

def num_map(name, prev_code):
    soundex = ""
    for char in name[1:]:
        ch = get_soundex_code(char)
        code = comparison(ch, prev_code)
        if code:  # Append non-empty code to soundex and update prev_code
            soundex += code
            prev_code = code
    return soundex

def generate_soundex(name):
    if not name:
        return ""
    
    # Start with the first letter capitalized
    soundex = name[0].upper()
    prev_code = get_soundex_code(soundex)

    # Append the rest of the soundex code derived from the remaining characters
    soundex += num_map(name, prev_code)

    # Tr
