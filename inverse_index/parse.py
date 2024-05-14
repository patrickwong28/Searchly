from pathlib import Path

# Time Complexity is O(n) where n is the number of characters in a file. This is because the
# program reads the entire file byte for byte (or character by character) once until it is finished
# and then returns the tokens.
def tokenize(file_path: Path) -> list[str]:
    """
    Create a list of tokens for the given file
    """
    tokens = []
    with open(file_path, 'r', encoding='utf8') as file:
        word = ''
        while True:
            try:
                current_char = file.read(1).lower()

                # check for end of file
                if not current_char:
                    if len(word) != 0:
                        tokens.append(word)
                    break

                # keep building word if alphanumeric
                elif _is_alphanumeric(current_char):
                    word += current_char

                # append token once it hits non-alphanumeric character
                elif not _is_alphanumeric(current_char) and len(word) != 0:
                    tokens.append(word)
                    word = ''

            except UnicodeDecodeError:
                if len(word) != 0:
                    tokens.append(word)
                    word = ''
    return tokens


# Time Complexity is O(1) as it takes constant time to evaluate this expression. This is because
# the function isalnum and isascii will check a list that is always going to be the same size
# because isalnum has a list of the alphabet and numbers 0 - 9 and isascii has a list of all ascii
# characters. These will always be the same size.

def _is_alphanumeric(character: str) -> bool:
    """
    Helper function to check whether a character is alphanumeric
    """
    if character.isalnum() and character.isascii():
        return True
    else:
        return False

def compute_word_frequency(token_list: list[str]) -> dict:
    """
    Returns the frequency of each token in the token list
    """
    word_frequency = {}
    for token in token_list:
        if token not in word_frequency:
            word_frequency[token] = 1
        else:
            word_frequency[token] += 1
    
    return word_frequency