def add(numbers: str) -> int:
    if not numbers:
        return 0
    numbers = numbers.replace("\n", ",")
    parts = numbers.split(",")
    return sum(int(p) for p in parts)

def test_newline_and_comma_delimiters():
    print(add("1\n2,3") == 6)
    assert add("1\n2,3") == 6

if __name__ == "__main__":
    test_newline_and_comma_delimiters()