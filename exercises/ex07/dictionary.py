"""EX07 - Dictionary Functions."""

__author__ = "730461000"


def invert(given_dict: dict[str, str]) -> dict[str, str]:
    """Given a dictionary, function inverts the keys and the values to return an inverted dictionary."""
    invert_dict: dict[str, str] = dict()
    for keys in given_dict:
        new_key: str = given_dict[keys]
        if new_key in invert_dict:
            raise KeyError("You cannot have two of the same key value.")
        invert_dict[new_key] = keys
    return invert_dict
        

def favorite_color(orig_dict: dict[str, str]) -> str:
    """Given a dictionary, find the value that occurs most frequently."""
    freq_color: str = ""
    freq_num: int = 0
    color_dict: dict[str, int] = dict()
    for keys in orig_dict:
        color_key: str = orig_dict[keys]
        if color_key in color_dict:
            color_dict[color_key] += 1
        else:
            color_dict[color_key] = 1
    for keys in color_dict:
        if color_dict[keys] > freq_num:
            freq_num = color_dict[keys]
            freq_color = keys
    return freq_color

        
def count(given_list: list[str]) -> dict[str, int]:
    """Given a list of colors, this function will produce a dictionary of colors that appeared in list as keys and number of times as the values."""
    return_dict: dict[str, int] = dict()
    for color in given_list:
        if color in return_dict:
            return_dict[color] += 1
        else:
            return_dict[color] = 1
    return return_dict