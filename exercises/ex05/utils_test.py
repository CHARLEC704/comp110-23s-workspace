"""EX05 - Unit Testing Cases - List Utility Functions."""

__author__ = "730461000"

from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens_empty() -> None:
    """Given an emply list without evens, return empty list for edge case."""
    assert only_evens([]) == []


def test_only_evens_one_element() -> None:
    """Given a one-element list without evens, return empty list for use case."""
    test_only_evens_list: list[int] = [1]
    assert only_evens(test_only_evens_list) == []


def test_only_evens_many() -> None:
    """Given a list with evens and odds, return evens-only list for use case."""
    test_only_evens_list: list[int] = [1, 2, 3]
    assert only_evens(test_only_evens_list) == [2]


def test_only_evens_many_with_negatives() -> None:
    """Given a list with negative evens and odds, return evens-only list for edge case."""
    test_only_evens_list: list[int] = [1, -2, 1]
    assert only_evens(test_only_evens_list) == [-2]


def test_concat_empty() -> None:
    """Given two emply lists, return empty list for edge case."""
    test_concat_list_one: list[int] = []
    test_concat_list_two: list[int] = []
    assert concat(test_concat_list_one, test_concat_list_two) == []


def test_concat_many() -> None:
    """Given two lists, each with multiple components, return concatenated list for use case."""
    test_concat_list_one: list[int] = [1, 2, 3]
    test_concat_list_two: list[int] = [4, 5, 6]
    assert concat(test_concat_list_one, test_concat_list_two) == [1, 2, 3, 4, 5, 6]


def test_concat_one() -> None:
    """Given two lists, each with single components, return concatenated list for use case."""
    test_concat_list_one: list[int] = [1]
    test_concat_list_two: list[int] = [2]
    assert concat(test_concat_list_one, test_concat_list_two) == [1, 2]


def test_concat_many_with_negatives() -> None:
    """Given two lists, each with multiple components and some negative, return concatenated list for edge case."""
    test_concat_list_one: list[int] = [1, -2, 1]
    test_concat_list_two: list[int] = [-3, -5, -7]
    assert concat(test_concat_list_one, test_concat_list_two) == [1, -2, 1, -3, -5, -7]


def test_sub_empty() -> None:
    """Given an empty list and a index range, return empty list for edge case."""
    test_sub_list: list[int] = []
    test_sub_num1: int = 1
    test_sub_num2: int = 3
    assert sub(test_sub_list, test_sub_num1, test_sub_num2) == []


def test_sub_many() -> None:
    """Given a list of many components and a range, return list of components in index range for use case."""
    test_sub_list: list[int] = [10, 20, 30, 40]
    test_sub_num1: int = 1
    test_sub_num2: int = 3
    assert sub(test_sub_list, test_sub_num1, test_sub_num2) == [20, 30]


def test_sub_one() -> None:
    """Given a list with one component and a range, return empty list for edge case."""
    test_sub_list: list[int] = [1]
    test_sub_num1: int = 3
    test_sub_num2: int = 4
    assert sub(test_sub_list, test_sub_num1, test_sub_num2) == []


def test_sub_many_with_negatives() -> None:
    """Given a list with negative components and a range, return a list for edge case."""
    test_sub_list: list[int] = [-10, -20, -30, -40]
    test_sub_num1: int = 1
    test_sub_num2: int = 3
    assert sub(test_sub_list, test_sub_num1, test_sub_num2) == [-20, -30]