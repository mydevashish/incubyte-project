import pytest

def add(numbers: str) -> int:
    if not numbers:
        return 0

    delimiter = ","
    if numbers.startswith("//"):
        header, numbers = numbers.split("\n", 1)
        delimiter = header[2:]

    numbers = numbers.replace("\n", delimiter)
    parts = numbers.split(delimiter)
    return sum(int(p) for p in parts)

def test_negative_number_raises_exception():
    with pytest.raises(Exception) as exc:
        add("1,-2,3")
    assert str(exc.value) == "negative numbers not allowed -2"

if __name__ == "__main__":
    test_negative_number_raises_exception()