example = 'It\'s a me, Mario' 
# ================================ 
# ============CODES===============
# ================================
# -- MORSE -- 
morse = {    
             'a': '.- ',
             'b': '-... ',
             'c': '-.-. ',
             'd': '-.. ',
             'e': '. ',
             'f': '..-. ',
             'g': '--. ',
             'h': '.... ',
             'i': '.. ',
             'j': '.--- ',
             'k': '-.- ',
             'l': '.-.. ',
             'm': '-- ',
             'n': '-. ',
             'o': '--- ',
             'p': '.--. ',
             'q': '--.- ',
             'r': '.-. ',
             's': '... ',
             't': '- ',
             'u': '..- ',
             'v': '...- ',
             'w': '.-- ',
             'x': '-..- ',
             'y': '-.-- ',
             'z': '--.. ',
             ',': '--..-- ',
             '.': '.-.-.- ',
             '\'': '.----. '
        }

def encode_morse(text: str):
    """
        NAME
            encode_morse

        DESCRIPTION
            Function used to encode the given text into morse code using the google_api
            and the predetermined dictionary.

        EXAMPLE
           It's a me, Mario
           .. - .----. ...  \ .-  \ -- . --..--  \ -- .- .-. .. --- 

    """
    
    # Here is where the encoding happens
    message = ''
    for letter in text:
        if letter == ' ':
            message += ' \ '
        else:
            message += morse[letter.lower()]

    return message

def encode_bin(text: str):
    """
        NAME
            encode_bin

        DESCRIPTION
            Function used to encode the spoken text into binary using the google_api
            and the combination of pythons built-in bin() and ord() function to get the desired
            byte-strings
        
        EXAMPLE
            It's a me, Mario
            0b10010010b11101000b1001110b11100110b1000000b11000010b1000000b1101101
            0b11001010b1011000b1000000b10011010b11000010b11100100b11010010b1101111           
    """

    message = '' 
    for letter in text:
        message += bin(ord(letter))

    return message

if __name__ == "__main__":
    print(example, '\n', encode_morse(example))
    print(example, '\n', encode_bin(example))
