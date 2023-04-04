"""CQ04 -- dictionary functions."""


def zip(a_listed_strings: list[str], b_listed_numbers: list[int]) -> dict[str, int]:
    result_dict: dict[str, int] = dict()
    idx: int = 0
    if len(a_listed_strings) != len(b_listed_numbers):
        return {}
    if len(a_listed_strings) == 0 or len(b_listed_numbers) == 0:
        return {}
    for letters in a_listed_strings:
        result_dict[letters] = b_listed_numbers[idx]
        idx += 1
    return result_dict

print(zip(("x","y","z"), (3,2,1)))