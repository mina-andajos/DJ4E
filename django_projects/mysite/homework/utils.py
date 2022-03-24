from typing import List


def reverse_field(field: str) -> str:
    return field[::-1]


def combine_fields(*fields) -> str:
    reversed_fields: List[str] = [reverse_field(field) for field in fields]

    reversed_fields_reversed=reversed_fields[::-1]

    return " ".join(reversed_fields_reversed)