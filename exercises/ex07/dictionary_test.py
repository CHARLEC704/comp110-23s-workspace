"""EX07 - Dictionary Functions - Unit Tests."""

__author__ = "730461000"

from exercises.ex07.dictionary import invert, favorite_color, count


def test_invert_empty() -> None:
    """Given an emply dict, return empty dict for edge case."""
    test_dict: dict[str, str] = dict()
    assert invert(test_dict) == {}


def test_invert_few() -> None:
    """Given a dict with two keys, invert values with respective keys for use case."""
    test_dict: dict[str, str] = {'heels': 'tar', 'Carolina': 'North'}
    assert invert(test_dict) == {'tar': 'heels', 'North': 'Carolina'}


def test_invert_many() -> None:
    """Given a dict with many keys, invert values with respective keys for use case."""
    test_dict: dict[str, str] = {'420': 'ECON', '428': 'GEOG', '427': 'PHYA', '233': 'MATH', '110': 'COMP'}
    assert invert(test_dict) == {'ECON': '420', 'GEOG': '428', 'PHYA': '427', 'MATH': '233', 'COMP': '110'}


def test_favorite_color_empty() -> None:
    """Given an emply dict, return empty string for edge case."""
    test_dict: dict[str, str] = dict()
    assert favorite_color(test_dict) == ""


def test_favorite_color_many() -> None:
    """Given a dict with many keys, return most frequent color for use case."""
    test_dict: dict[str, str] = {'Mike': 'red', 'Ozzie': 'black', 'Charles': 'blue', 'Sebastian': 'blue'}
    assert favorite_color(test_dict) == "blue"


def test_favorite_color_few() -> None:
    """Given a dict with many keys but no repeats, return number most frequent color that appears first for use case."""
    test_dict: dict[str, str] = {'Mike': 'red', 'Ozzie': 'black'}
    assert favorite_color(test_dict) == "red"


def test_count_empty() -> None:
    """Given an empty list of colors, return empty dict for edge case."""
    test_list: list[str] = []
    assert count(test_list) == {}


def test_count_single() -> None:
    """Given an list of colors(each only appearing once), return dict with values 1 for use case."""
    test_list: list[str] = ["green", "red", "orange", "blue"]
    assert count(test_list) == {'green': 1, 'red': 1, 'orange': 1, 'blue': 1}


def test_count_repeat() -> None:
    """Given an list of colors(some repeating), return dict with differing values for use case."""
    test_list: list[str] = ["green", "red", "orange", "blue", "red", "red", "orange", "red"]
    assert count(test_list) == {'green': 1, 'red': 4, 'orange': 2, 'blue': 1}
