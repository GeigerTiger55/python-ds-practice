def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    # .get(search for val, none)
    frequncey_counter = {}
    for char in phrase:
        if char in frequncey_counter.keys():
            frequncey_counter[char] += 1
        else:
            frequncey_counter[char] = 1

    return frequncey_counter
