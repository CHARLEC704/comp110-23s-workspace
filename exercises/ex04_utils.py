"""EX04 - Utils - List Utility Functions."""
__author__ = "730461000"


def all(listed_values: list[int], single_number: int) -> bool:
    """Discerning whether integers in list are same as given integer."""
    idx_check: int = 0
    matched_value: bool = False
    while idx_check <= len(listed_values) - 1:
        matched_value = True
        if single_number != listed_values[idx_check]:
            matched_value = False
            return matched_value
        else:
            idx_check += 1
    return matched_value


def max(given_list: list[int]) -> int:
    """Given a list, return the largest number."""
    if len(given_list) == 0:
        raise ValueError("max() arg is an empyty List")
    idx_of_list: int = 0
    max_found: int = given_list[idx_of_list]
    while idx_of_list < len(given_list):
        if given_list[idx_of_list] >= max_found:
            max_found = given_list[idx_of_list]
        idx_of_list += 1
    return max_found
    
    
def is_equal(list_one: list[int], list_two: list[int]) -> bool:
    """Discern whether lists are deepy equivalent."""
    idx_equivalent_lists: int = 0
    equal_lists: bool = True
    if len(list_one) == len(list_two):
        while idx_equivalent_lists < len(list_one):
            if list_one[idx_equivalent_lists] == list_two[idx_equivalent_lists]:
                equal_lists = True
                idx_equivalent_lists += 1
            else:
                equal_lists = False
                return equal_lists
        return equal_lists
    else: 
        equal_lists = False
        return equal_lists