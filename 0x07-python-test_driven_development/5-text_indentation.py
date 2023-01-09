"""Module containing function to print string
by line. It contains no directly executable code
It should be imported as a module
"""

def text_indentation(text):
    """Print a given text by indenting
    when there is one of a given delimeters

    Args:
        text (string): parameter to process

    Raises:
        TypeError: if text is other than string
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    previous = ""
    for ch in text:
        # leading whitesapces
        if ch is " " and ch is text[0] and previous is "":
            previous = "\n"
            continue
        # whitespace after newline
        if ch is " " and previous is "\n":
            continue
        # getting the delimeter, print it and new anewline
        if ch is "." or ch is "?" or ch is ":":
            print(ch)
            print()
            previous = "\n"
        else:
            print(ch, end="")
            previous = ch
