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
    return mapping.get(char, '0')

def comparison(ch, prev_code):
    return ch if ch != '0' and ch != prev_code else ""

def num_map(name, prev_code):
    soundex = ""
    for char in name[1:]:
        ch = get_soundex_code(char)
        code = comparison(ch, prev_code)
        if code:
            soundex += code
            prev_code = code
    return soundex

def get_initial_soundex(name):
    if not name:
        return "", "0"
    initial = name[0].upper()
    return initial, get_soundex_code(initial)

def pad_soundex(soundex):
    return soundex[:4].ljust(4, '0')

def generate_soundex(name):
    initial, prev_code = get_initial_soundex(name)
    if not initial:
        return ""
    return pad_soundex(initial + num_map(name, prev_code))

# Unit testing the Soundex generation
if __name__ == '__main__':
    print(generate_soundex(""))           # Output: ""
    print(generate_soundex("A"))          # Output: "A000"
    print(generate_soundex("Ashcraft"))   # Output: "A261"
    print(generate_soundex("Tymczak"))    # Output: "T522"
    print(generate_soundex("McDonald"))   # Output: "M235"
    print(generate_soundex("Van Helsing"))# Output: "V542"
    print(generate_soundex("O'Connor"))   # Output: "O256"
