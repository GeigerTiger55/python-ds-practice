def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    swapped_phrase = ''

    for char in phrase:
        if char == to_swap.lower():
            replace_char = char.upper()
            swapped_phrase = (f"{swapped_phrase}{replace_char}")
        elif char == to_swap.upper():
            replace_char = char.lower()
            swapped_phrase = (f"{swapped_phrase}{replace_char}")
        else:
            swapped_phrase = (f"{swapped_phrase}{char}")
    return swapped_phrase

    

