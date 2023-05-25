def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """

    letter_Count = {}:
    for letter in phrase:
        if letter in letter_Count:
            letter_Count[letter] += 1
        else:
            letter_Count[letter] = 1
        Return letter_Count

        