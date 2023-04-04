"""EX05 - Directory - List Utility Functions."""

__author__ = "730461000"


def only_evens(listed_integers: list[int]) -> list[int]:
    """Given a list of integers, return even components of the list."""
    even_outputs: list[int] = []
    list_idx: int = 0
    while list_idx < len(listed_integers):
        if listed_integers[list_idx] % 2 == 0 and listed_integers[list_idx] != 0:
            even_outputs.append(listed_integers[list_idx])
        list_idx += 1
    return even_outputs
    

def concat(first_list: list[int], second_list: list[int]) -> list[int]:
    """Given two lists, combine into one large lists of first list's components followed by the second list's."""
    idx_list_two: int = 0
    combined_list: list[int] = [] 
    while idx_list_two < len(first_list):
        combined_list.append(first_list[idx_list_two])
        idx_list_two += 1
    idx_list_two = 0
    while idx_list_two < len(second_list):
        combined_list.append(second_list[idx_list_two])
        idx_list_two += 1
    return combined_list


def sub(given_list: list[int], first_num: int, second_num: int) -> list[int]:
    """Given a list, return a subset of that list inbetween two integer indices."""
    subseted_list: list[int] = []
    if len(given_list) == 0 or first_num >= len(given_list) or second_num <= 0:
        return subseted_list
    else:
        if first_num < 0:
            start_idx: int = 0
        else:
            start_idx: int = first_num
    while start_idx <= second_num - 1 and start_idx < len(given_list):
        subseted_list.append(given_list[start_idx])
        start_idx += 1
    return subseted_list