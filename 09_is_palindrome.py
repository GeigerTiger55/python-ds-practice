def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """

    left = 0
    right = len(phrase) - 1
    phrase_lower = phrase.lower()

    while left < right:
        if phrase_lower[left] == ' ':
            left +=1
        elif phrase_lower[right] == ' ':
            right -=1
        elif not phrase_lower[left] == phrase_lower[right]:
            return False
        else:
            left +=1
            right -=1

    return True

