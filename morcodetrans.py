morse_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}

def to_morse_code(text):
    morse_code = ''
    for char in text:
        if char.upper() in morse_dict:
            morse_code += morse_dict[char.upper()] + ' '
        else:
            morse_code += char + ' '
    return morse_code

def to_text(morse_code):
    text = ''
    words = morse_code.split('  ')
    for word in words:
        chars = word.split()
        for char in chars:
            for key, value in morse_dict.items():
                if value == char:
                    text += key
        text += ' '
    return text

# example usage
text = "HELLO WORLD"
morse_code = to_morse_code(text)
print(morse_code) # prints ".... . .-.. .-.. ---  .-- --- .-. .-.. -.. "
converted_text = to_text(morse_code)
print(converted_text) # prints "HELLO WORLD"
