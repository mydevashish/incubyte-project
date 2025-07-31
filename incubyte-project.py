import pytest

def add(numbers: str) -> int:
    if not numbers:
        return 0

    delimiter, numbers = _parse_delimiter_and_body(numbers)
    numbers = numbers.replace("\n", delimiter)
    parts = numbers.split(delimiter)
    nums = [int(p) for p in parts if p]

    _check_for_negatives(nums)

    return sum(nums)


def _parse_delimiter_and_body(numbers: str) -> tuple[str, str]:
    if numbers.startswith("//"):
        header, body = numbers.split("\n", 1)
        return header[2:], body
    return ",", numbers


def _check_for_negatives(numbers: list[int]) -> None:
    negatives = [n for n in numbers if n < 0]
    if negatives:
        raise Exception(f"negative numbers not allowed {','.join(map(str, negatives))}")

def test_multiple_negatives_raise_all():
    with pytest.raises(Exception) as exc:
        add("1,-2,-4,3")
    assert str(exc.value) == "negative numbers not allowed -2,-4"


if __name__ == "__main__":
    test_multiple_negatives_raise_all()