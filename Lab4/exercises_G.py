def get_main_and_min_values(numbers:list):
    """Gives the max and min value in a list with numbers"""
    min_value = None
    max_value = None
    for number in numbers:
        if min_value is None or min_value > number:
            min_value = number
        if max_value is None or max_value < number:
            max_value = number
    return min_value, max_value

def is_word_palindrome(word: str):
    """Sanitizes the word and tells the user if the word is a palindrome or not"""
    sanitized_word = word.strip().lower()
    if sanitized_word == sanitized_word[::-1]:
        return True
    return False

def character_frequencies(text: str):
    """Returns a dictionary with all letters in the word and how many times it apers in the given word"""
    freq = {}
    for char in text:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    return freq

def numbers_dictionary(numbers: list):
    """Returns a dictionary with index as key"""
    dictionary = {}
    for index, number in enumerate(numbers):
        dictionary[index] = number
    return dictionary

def separator(separator: str = '-'):
    """Returns a line separator repeated 20 times. Defaults to '-'."""
    return separator*20


# --- Main like section ---
list_with_numbers = [0, 9, 134, 90, 67]
print(get_main_and_min_values(list_with_numbers))
print(separator('*'))
print(is_word_palindrome('Abba '))
print(separator('+'))
print(is_word_palindrome('Sill'))
print(separator())
print(character_frequencies('mint glassar är goda'))
print(separator())
print(numbers_dictionary(list_with_numbers))