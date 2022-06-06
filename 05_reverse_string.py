def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    csv_phrase = ",".join(phrase)
    list_chars = csv_phrase.split(",")
    list_chars.reverse()
    reversed_phrase = "".join(list_chars)
    return reversed_phrase
    