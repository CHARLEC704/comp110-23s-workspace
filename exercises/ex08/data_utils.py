"""EX08 - Data Warngling: Data utils"""

__author__ = "730461000"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read csv file and return as a list of dicts with header keys."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result

def column_values(table: list[dict[str, str]], header: str) -> list[str]:
    """Returns values in a table column under a specific header."""
    result: list[str] = []
    #step through table
    for row in table:
        #save every value under key "header"
        result.append(row[header])
    return result

def columnar(table: list[dict[str, str]]) -> dict[str,list[str]]:
    """Reformats data so that it's a dictionary with column headers."""
    result: dict[str, list[str]] = {}
    #loop through keys of one row of table
    first_row: dict[str, str] = table[0]
    for key in first_row:
        #for each key, make a dictionary entry with all column values
        result[key] = column_values(table, key)
    return result


def head(column_based: dict[str,list[str]], num_rows: int) -> dict[str, list[str]]:
    """Reformats data so that it is a column-based table with only the first N rows of data for each column."""
    return_dict: dict[str, list[str]] = {}
    if num_rows >= len(column_based):
        return column_based
    for key in column_based:
        sub_list: list[str] = []
        idx: int = 0
        while idx < num_rows:
            sub_list.append(column_based[key][idx])
            idx += 1
        return_dict[key] = sub_list
    return return_dict


def select(given_dict: dict[str, list[str]], given_list: list[str]) -> dict[str, list[str]]:
    """Given whole dictionary, look at two columns and their associated values."""
    return_dict_2: dict[str, list[str]] = {}
    for idx in given_list:
        return_dict_2[idx] = given_dict[idx]
    return return_dict_2


def concat(first_given_dict: dict[str, list[str]], second_given_dict: dict[str, list[str]]) -> dict[str, list[str]]:
    """Given two column-based table entries, combine them into a single column-based table."""
    new_dict: dict[str, list[str]] = {}
    for idx in first_given_dict:
        new_dict[idx] = first_given_dict[idx]
    for idx in second_given_dict:
        if idx in new_dict:
           new_dict[idx] += second_given_dict[idx] 
        else:
            new_dict[idx] = second_given_dict[idx]
    return new_dict


def count(given_list: list[str]) -> dict[str, int]:
    "Given a list, this function will return a dictionary of the value and its frequency."
    return_dict: dict[str, int] = dict()
    for race in given_list:
        if race in return_dict:
            return_dict[race] += 1
        else:
            return_dict[race] = 1
    return return_dict