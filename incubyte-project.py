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

def test_custom_delimiter_semicolon():
    print(add("//;\n1;2") == 3)
    assert add("//;\n1;2") == 3

if __name__ == "__main__":
    test_custom_delimiter_semicolon()