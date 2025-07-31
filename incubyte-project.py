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

def test_empty_string_returns_zero():
    print(add("") == 0)
    assert add("") == 0

def test_single_number_returns_itself():
    print(add("1") == 1)
    assert add("1") == 1

def test_two_numbers_return_sum():
    print(add("1,5") == 6)
    assert add("1,5") == 6

def test_multiple_numbers_return_sum():
    print(add("1,2,3,4") == 10)
    assert add("1,2,3,4") == 10

def test_newline_and_comma_delimiters():
    print(add("1\n2,3") == 6)
    assert add("1\n2,3") == 6

def test_custom_delimiter_semicolon():
    print(add("//;\n1;2") == 3)
    assert add("//;\n1;2") == 3

def test_custom_delimiter_letter():
    print(add("//x\n4x5x6") == 15)
    assert add("//x\n4x5x6") == 15

def test_negative_number_raises_exception():
    with pytest.raises(Exception) as exc:
        add("1,-2,3")
    assert str(exc.value) == "negative numbers not allowed -2"

def test_multiple_negatives_raise_all():
    with pytest.raises(Exception) as exc:
        add("1,-2,-4,3")
    assert str(exc.value) == "negative numbers not allowed -2,-4"


if __name__ == "__main__":
    test_empty_string_returns_zero()
    test_single_number_returns_itself()
    test_two_numbers_return_sum()
    test_multiple_numbers_return_sum()
    test_newline_and_comma_delimiters()
    test_custom_delimiter_semicolon()
    test_custom_delimiter_letter()
    test_negative_number_raises_exception()
    test_multiple_negatives_raise_all()