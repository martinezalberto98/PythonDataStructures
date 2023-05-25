def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    to_swap = to_swap.lower()
    flipped_phrase = ''
    
    for char in phrase:
        if char.lower() == to_swap.lower():
            if char.islower():
                flipped_phrase += char.upper()
            else:
                flipped_phrase += char.lower()
        else:
            flipped_phrase += char
    return flipped_phrase
    

    
